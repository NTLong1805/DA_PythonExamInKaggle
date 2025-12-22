import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kneed import KneeLocator
from mlxtend.frequent_patterns import fpgrowth, association_rules
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from xgboost import XGBRegressor
import shap

# Cấu hình hiển thị pandas
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_colwidth', None)

# --- 1. LOAD & CLEAN DATA ---
data = pd.read_csv('python_learning_exam_performance.csv')

# Xử lý dữ liệu
data.fillna('unknown', inplace=True)
data['passed_exam'] = data['passed_exam'].apply(lambda x: 'Passed' if x == 1 else 'Failed')

# Tách nhóm Passed/Failed
pass_group = data[data['passed_exam'] == 'Passed']
fail_group = data[data['passed_exam'] == 'Failed'].copy()

feature = ['hours_spent_learning_per_week',
           'practice_problems_solved',
           'projects_completed',
           'tutorial_videos_watched',
           'debugging_sessions_per_week']

# --- 2. CLUSTERING (K-MEANS) ---
# Log Transform & Scale cho Clustering
data_loga = pd.DataFrame()
for col in feature:
    data_loga[col] = np.log1p(fail_group[col])

scaler = StandardScaler()
data_scaler = scaler.fit_transform(data_loga)
data_scaled = pd.DataFrame(data_scaler, columns=feature, index=fail_group.index)

# Tìm K tối ưu
K_range = range(1, 11)
wcss = []
for k in K_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)

kl = KneeLocator(K_range, wcss, curve='convex', direction='decreasing')
optimal_k = kl.elbow
print(f'Số cụm tối ưu: {optimal_k}')

# Chạy KMeans Final
kmeansFinal = KMeans(n_clusters=3, init='k-means++', random_state=42, n_init=10)
kmeansFinal.fit(data_scaled)
fail_group['Cluster'] = kmeansFinal.labels_

# Gộp Cluster vào data gốc
data['Cluster'] = 'Passed' # Mặc định là Passed
data.loc[fail_group.index, 'Cluster'] = fail_group['Cluster'] # Cập nhật cho nhóm Failed

# --- 3. REGRESSION (DỰ BÁO ĐIỂM SỐ - XGBoost) ---
feature_prediction = feature
experience_map = {'Unknown': 0, 'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}

# Chuẩn bị dữ liệu train regression
# Lưu ý: Cần scale lại từ đầu cho tập X này hoặc dùng data_scaled đã có
X_reg = data_scaled[feature_prediction].copy()
X_reg['Experience_Programming'] = fail_group['prior_programming_experience'].map(experience_map)
X_reg['Cluster'] = fail_group['Cluster']
y_reg = fail_group['final_exam_score']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

print(f'Kích thước tập train: {X_train_r.shape}')
print(f'Kích thước tập Test: {X_test_r.shape}')

reg_model = XGBRegressor(
    n_estimators=1000, learning_rate=0.01, max_depth=5,
    early_stopping_rounds=50, random_state=42, n_jobs=-1
)

reg_model.fit(X_train_r, y_train_r, eval_set=[(X_test_r, y_test_r)], verbose=False)
y_predict_r = reg_model.predict(X_test_r)

print("=== KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH REGRESSION ===")
print(f"MAE: {mean_absolute_error(y_test_r, y_predict_r):.2f}")
print(f"RMSE: {root_mean_squared_error(y_test_r, y_predict_r):.2f}")
print(f"R2: {r2_score(y_test_r, y_predict_r):.2f}")

feature_importance = pd.DataFrame({
    'Feature': X_reg.columns,
    'Importance': reg_model.feature_importances_
}).sort_values(by='Importance', ascending=False)
print(feature_importance)

# --- 4. CLASSIFICATION (LOGISTIC REGRESSION) ---
# Chuẩn bị dữ liệu: Loại bỏ các cột không cần thiết
# Lưu ý: Lúc này data đã có cột Cluster, cần drop nếu không muốn dùng làm feature
cols_to_drop = ['student_id', 'final_exam_score', 'passed_exam', 'Cluster']
x_logis = data.drop(columns=cols_to_drop, axis=1)

target = data['passed_exam'].apply(lambda x: 1 if x == 'Passed' else 0)
x_logis = pd.get_dummies(x_logis, columns=['country', 'prior_programming_experience'], drop_first=True)

# Log transform
for col in feature:
    x_logis[col] = np.log1p(x_logis[col])

# Scale (Giữ index để map lại sau này)
x_scaler_logis = scaler.fit_transform(x_logis)
x_scaled_logis = pd.DataFrame(x_scaler_logis, columns=x_logis.columns, index=x_logis.index)

X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(x_scaled_logis, target, test_size=0.2, random_state=42)

logis_model = LogisticRegression(solver='liblinear', random_state=42)
logis_model.fit(X_train_l, y_train_l)
y_pred_l = logis_model.predict(X_test_l)

print(f"Logistic Regression Accuracy: {accuracy_score(y_test_l, y_pred_l):.2%}")

coef_df = pd.DataFrame({
    'Feature': x_logis.columns,
    'Coefficient': logis_model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)
print("\nCác yếu tố ảnh hưởng nhất (Logistic):")
print(coef_df.head())

# Dự báo rủi ro cho TOÀN BỘ dataset
data['Predicted_Status'] = logis_model.predict(x_scaled_logis)
data['Pass_Probability'] = logis_model.predict_proba(x_scaled_logis)[:, 1]

conditions = [
    (data['Pass_Probability'] < 0.5),
    (data['Pass_Probability'] >= 0.5) & (data['Pass_Probability'] < 0.8),
    (data['Pass_Probability'] >= 0.8)
]
choices = ['High Risk', 'Medium Risk', 'Safe']
data['Risk_Level'] = np.select(conditions, choices, default='Unknown')

comparison = data[['student_id', 'passed_exam', 'Predicted_Status', 'Pass_Probability', 'Risk_Level']]
print("=== BẢNG KẾT QUẢ DỰ BÁO ===")
print(comparison.head())

# --- 5. RANDOM FOREST & SHAP ANALYSIS (CHẠY TRÊN TOÀN BỘ DỮ LIỆU) ---

# Bước 1: Chuẩn bị dữ liệu (Giữ nguyên phần xử lý x_tree)
cols_to_drop_rf = [
    'student_id', 'final_exam_score', 'passed_exam',
    'Cluster', 'Predicted_Status', 'Pass_Probability', 'Risk_Level'
]
x_tree = data.drop(columns=cols_to_drop_rf, axis=1, errors='ignore')
x_tree = pd.get_dummies(x_tree, columns=['country', 'prior_programming_experience'], drop_first=True)

for col in feature:
    x_tree[col] = np.log1p(x_tree[col])

x_scaler_tree = scaler.fit_transform(x_tree)
# x_scaled_tree chứa TOÀN BỘ 3000 dòng dữ liệu đã chuẩn hóa
x_scaled_tree = pd.DataFrame(x_scaler_tree, columns=x_tree.columns, index=x_tree.index)

# Bước 2: Huấn luyện mô hình (Vẫn train trên tập Train để tránh Overfitting)
X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(x_scaled_tree, target, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train_rf, y_train_rf)

# In độ chính xác (Vẫn dùng tập test để đánh giá độ chính xác)
y_pred_test = rf_model.predict(X_test_rf)
print(f"Random Forest Accuracy (trên tập Test): {accuracy_score(y_test_rf, y_pred_test):.2%}")

# --- BƯỚC QUAN TRỌNG: ÁP DỤNG SHAP CHO TOÀN BỘ DỮ LIỆU (FULL DATASET) ---
print("Đang tính toán SHAP cho toàn bộ dữ liệu (có thể mất vài giây)...")

explainer = shap.TreeExplainer(rf_model)
# Thay X_test_rf bằng x_scaled_tree (Toàn bộ dữ liệu)
shap_values = explainer.shap_values(x_scaled_tree)

# Xử lý định dạng đầu ra của SHAP
if isinstance(shap_values, list):
    shap_vals_class_1 = shap_values[1] # List [class_0, class_1]
else:
    shap_vals_class_1 = shap_values[:, :, 1] # Array 3D

# Tìm nguyên nhân chính
feature_names = x_scaled_tree.columns.tolist()
min_shap_indices = np.argmin(shap_vals_class_1, axis=1)

# --- TẠO DATAFRAME KẾT QUẢ CHO TOÀN BỘ SINH VIÊN ---
# Tạo khung sườn dựa trên index của toàn bộ dữ liệu
analyst_df = pd.DataFrame(index=x_scaled_tree.index)

# 1. Gán Student ID
analyst_df['student_id'] = analyst_df.index.map(data['student_id'].to_dict())

# 2. Gán xác suất (Dự báo cho toàn bộ dữ liệu)
analyst_df['Pass_Probability'] = rf_model.predict_proba(x_scaled_tree)[:, 1]

# 3. Gán lý do
analyst_df['Main_Reason_Technical'] = [feature_names[i] for i in min_shap_indices]

# --- PHẦN MAP LÝ DO & HÀNH ĐỘNG (GIỮ NGUYÊN) ---
conditions_rf = [
    (analyst_df['Pass_Probability'] < 0.5),
    (analyst_df['Pass_Probability'] >= 0.5) & (analyst_df['Pass_Probability'] < 0.8),
    (analyst_df['Pass_Probability'] >= 0.8)
]
choices = ['High Risk', 'Medium Risk', 'Safe']
analyst_df['Risk_Level'] = np.select(conditions_rf, choices, default='Unknown')

# Map Lý do & Hành động
reason_action_map = {
    'projects_completed': {'Reason': 'Thiếu dự án thực tế', 'Action': 'Giao thêm 1 Mini-Project'},
    'debugging_sessions_per_week': {'Reason': 'Ít thực hành Debug', 'Action': 'Yêu cầu tham gia session sửa lỗi'},
    'hours_spent_learning_per_week': {'Reason': 'Thiếu giờ học', 'Action': 'Kiểm tra nhật ký học tập'},
    'practice_problems_solved': {'Reason': 'Làm quá ít bài tập', 'Action': 'Giao bài tập LeetCode'},
    'tutorial_videos_watched': {'Reason': 'Hổng kiến thức nền', 'Action': 'Xem lại Video bài giảng'},
    'participates_in_forums': {'Reason': 'Thiếu tương tác', 'Action': 'Đặt câu hỏi trên Forum'}
}

def get_readable_reason(col_name):
    for key in reason_action_map:
        if key in col_name:
            return reason_action_map[key]['Reason']
    return 'Các yếu tố khác'

def get_action(col_name):
    for key in reason_action_map:
        if key in col_name:
            return reason_action_map[key]['Action']
    return 'Phỏng vấn trực tiếp'

analyst_df['Main_Reason'] = analyst_df['Main_Reason_Technical'].apply(get_readable_reason)
analyst_df['Suggested_Action'] = analyst_df['Main_Reason_Technical'].apply(get_action)

# Xử lý nhóm Safe
analyst_df.loc[analyst_df['Risk_Level'] == 'Safe', 'Main_Reason'] = 'Đạt chuẩn'
analyst_df.loc[analyst_df['Risk_Level'] == 'Safe', 'Suggested_Action'] = 'Duy trì phong độ'

print(f"\nĐã hoàn thành phân tích rủi ro cho {len(analyst_df)} sinh viên.")
print("\nDanh sách sinh viên High Risk (5 dòng đầu):")
print(analyst_df[analyst_df['Risk_Level'] == 'High Risk'].head())

# --- 6. FP-GROWTH (LUẬT KẾT HỢP) ---
cols_fp = feature + ['final_exam_score']
data_fp = data[data['passed_exam'] == 'Passed'][cols_fp].copy()
labels = ['Low', 'High']

# Binning
for col in cols_fp:
    # Thêm drop_duplicates=True để tránh lỗi nếu dữ liệu phân bố lệch
    data_fp[f'{col}_Bin'] = pd.qcut(data_fp[col], q=[0, 0.5, 1], labels=labels, duplicates='drop')

cols_bin = [f'{col}_Bin' for col in cols_fp]
basket = pd.get_dummies(data_fp[cols_bin])

frequen_items = fpgrowth(basket.astype(bool), min_support=0.1, use_colnames=True)
rules = association_rules(frequen_items, metric='lift', min_threshold=1)

# Lọc luật liên quan đến điểm số
# Lưu ý: Tên cột sau khi get_dummies sẽ có dạng 'final_exam_score_Bin_High'
score_rules = rules[
    rules['consequents'].astype(str).str.contains('final_exam_score')
].sort_values(by='lift', ascending=False)

print('-------------TOP 10 RULES ---------------------')
print(score_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

# --- 7. EXPORT TO EXCEL ---
output_name = 'datamining_Student.xlsx'
try:
    with pd.ExcelWriter(output_name, engine='openpyxl') as writer:
        score_rules.to_excel(writer, sheet_name='FP_Growth_Rules', index=False)
        comparison.to_excel(writer, sheet_name='Logistic_Prediction', index=False)
        coef_df.to_excel(writer, sheet_name='Logistic_Coefficients', index=False)
        data.to_excel(writer, sheet_name='Full_Data_With_Risk', index=False)
        analyst_df.to_excel(writer, sheet_name='RF_Risk_Analysis', index=False)
        print(f"✅ Thành công! File đã được lưu tại: {output_name}")
except Exception as e:
    print(f'Lỗi xuất file: {e}')