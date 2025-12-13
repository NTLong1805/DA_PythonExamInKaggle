from statistics import LinearRegression

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kneed import KneeLocator
from mlxtend.classifier import LogisticRegression
from mlxtend.frequent_patterns import fpgrowth, association_rules
from pandas.core.common import random_state
from scipy.signal import square
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals.array_api_compat.numpy.linalg import solve
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor



def check_data_quality(df):
    quality_report = {
        'null_value' : df.isnull().sum().to_dict(),
        'na_value' : df.isna().sum().to_dict(),
        'duplicate_values' : df.duplicated().sum(),
        'describe' : df.describe(),
        'columns' : df.columns,
        'columns_Type' : df.dtypes,
        'info': df.info(),
    }
    return quality_report

pd.set_option('display.max_columns', 20)
pd.set_option('display.width',2000)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('python_learning_exam_performance.csv')

# Info Data
# check_quality_report = check_data_quality(data)
# print(check_quality_report)

# Percentage Of Null Value => giá trị null chủ yếu nằm ở
percentage_null_value = (data.isnull().sum() / len(data) * 100).sort_values(ascending=True)
percentage_null_value = percentage_null_value.loc[percentage_null_value > 0]
# print(percentage_null_value)

# Xử lý NA bằng giá trị Unknown
data.fillna('unknown', inplace=True)

#Giá trị duplicated Không có giá trị nào duplicated nên không cần xử lí
# print(data.duplicated().sum())

# Thay giá trị 1 0 ở cột passed_exam thành passed/failed
data['passed_exam'] = data['passed_exam'].apply(lambda x: 'Passed' if x == 1 else 'Failed')
# Thay giá trị 1/0 ở cột participates_in_discussion_forums thành Yes/No
data['participates_in_discussion_forums'].apply(lambda x: 'Yes' if x == 0 else 'No')
# Thay giá trị 1/0 ở uses_kaggle thành Yes/No
data['uses_kaggle'].apply(lambda x: 'Yes' if x == 0 else 'No')

pass_group = data[data['passed_exam'] == 'Passed']

fail_group = data[data['passed_exam'] == 'Failed'].copy()

mark_feature = pass_group[[
            'hours_spent_learning_per_week',
           'practice_problems_solved',
           'projects_completed',
           'tutorial_videos_watched',
           'debugging_sessions_per_week',
            ]].median()
feature = [ 'hours_spent_learning_per_week',
           'practice_problems_solved',
           'projects_completed',
           'tutorial_videos_watched',
           'debugging_sessions_per_week']
# print(fail_group)
# print('Passed Student:\n')
# print(mark_feature)

# Log Transform => tránh dữ liệu lệch phải
data_loga = pd.DataFrame()
data_loga['hours_spent_learning_per_week'] = np.log1p(fail_group['hours_spent_learning_per_week'])
data_loga['practice_problems_solved'] = np.log1p(fail_group.practice_problems_solved)
data_loga['projects_completed']= np.log1p(fail_group.projects_completed)
data_loga['tutorial_videos_watched'] = np.log1p(fail_group.tutorial_videos_watched)
data_loga['debugging_sessions_per_week'] = np.log1p(fail_group.debugging_sessions_per_week)

# Chuẩn hóa dữ liệu với Z-Score
scaler = StandardScaler()
data_scaler = scaler.fit_transform(data_loga)
data_scaled = pd.DataFrame(data_scaler,columns=feature)
data_scaled['student_id'] = data['student_id']
data_scaled['final_exam_score'] = data['final_exam_score']

X = data_scaled[['hours_spent_learning_per_week',
           'practice_problems_solved',
           'projects_completed',
           'tutorial_videos_watched',
           'debugging_sessions_per_week']]
K_range = range(1,11)
wcss = []
for k in K_range:
    kmeans = KMeans(n_clusters=k,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
kl = KneeLocator(K_range,wcss,curve='convex', direction='decreasing')
optimal_k = kl.elbow
# print(f'Số cụm tối ưu:{optimal_k}')
#
# # Vẽ biểu đồ trực quan cho thuật toán Elbow
# plt.plot(K_range,wcss,marker = "o",linestyle="--")
# plt.xlabel(K_range)
# plt.ylabel("WCSS")
# plt.title("Biểu đồ Elbow chọn K tối ưu")
# for i,txt in enumerate(wcss):
#     plt.text(K_range[i],wcss[i],f"{round(wcss[i],2)}",fontsize = 9,ha="left",va="bottom")
# plt.grid(True)
# plt.show()

# THực hiện KMeans
kmeansFinal = KMeans(3,init='k-means++',random_state=42,n_init = 10)
kmeansFinal.fit(X)
cluster_label = kmeansFinal.labels_
fail_group['Cluster'] = cluster_label
# print(fail_group)

# Đánh giá kết quả KMeans
cluster_analysis = fail_group.groupby('Cluster')[feature].mean()
cluster_analysis['Size_Cluster'] = fail_group.groupby('Cluster').size()
# print(cluster_analysis)



# Linear Regression(Dự báo điểm của sinh viên chưa đỗ)-------------- Không sử dụng được do học tập là dữ liệu phi tuyến tính => Bộ dữ liệu cho ra kết quả không đáng tin
feature_prediction = [ 'hours_spent_learning_per_week',
           'practice_problems_solved',
           'projects_completed',
           'tutorial_videos_watched',
           'debugging_sessions_per_week'
           ]

experience_map = {
    'Unknown':0,
    'Beginner':1,
    'Intermediate':2,
    'Advanced':3
}

X = data_scaled[feature_prediction].copy()
X['Experience_Programming'] = fail_group['prior_programming_experience'].map(experience_map)
X['Cluster'] = fail_group['Cluster'].values
y = fail_group['final_exam_score'].reset_index(drop=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(f'Kích thước tập train:{X_train.shape}')
print(f'Kích thước tập Test:{X_test.shape}')

print(X.head())

#Khởi tạo mô hình
assess_model = RandomForestRegressor(n_estimators=200,max_depth=10,random_state=42)
assess_model = XGBRegressor(
    n_estimators=10000,
    learning_rate=0.01,
    max_depth=5,
    early_stopping_rounds=50,
    random_state=42,
    n_jobs=-1
)
assess_model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=False
)
# assess_model.fit(X_train,y_train)

y_predict = assess_model.predict(X_test)

# Đánh giá hiệu suất
mae = mean_absolute_error(y_test,y_predict)
rmse = root_mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test,y_predict)

print("=== KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH ===")
print(f"MAE (Sai số tuyệt đối trung bình): {mae:.2f} điểm")
print(f"RMSE (Sai số toàn phương trung bình): {rmse:.2f} điểm")
print(f"R-squared (Độ phù hợp): {r2:.2f}")

feature_importance = pd.DataFrame({
    'Feature' : X.columns,
    'Importance' :assess_model.feature_importances_
}).sort_values(by='Importance',ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance, palette='viridis',hue='Feature', legend=False)
plt.title('Yếu tố nào ảnh hưởng nhất đến điểm thi?')
plt.xlabel('Mức độ quan trọng (Importance Score)')
plt.ylabel('Các yếu tố hành vi')
plt.show()

print(feature_importance)




#Logistic Regression Classification
x_logis = data.drop(['student_id','final_exam_score','passed_exam'],axis = 1)
target = data['passed_exam'].apply(lambda x: 1 if x == 'Passed' else 0)
x_logis = pd.get_dummies(x_logis,columns = ['country','prior_programming_experience'],drop_first=True)

numeric_cols = [
    'hours_spent_learning_per_week',
    'practice_problems_solved',
    'projects_completed',
    'tutorial_videos_watched',
    'debugging_sessions_per_week',
    'final_exam_score'
]

for col in numeric_cols:
    x_logis[col] = np.log1p(x_logis[col])

x_scaler = scaler.fit_transform(x_logis)
x_scaled = pd.DataFrame(x_scaler,columns= x_logis.columns)

X_train,X_test,y_train,y_test = train_test_split(x_scaled,target,test_size=0.2,random_state=42)
model = LogisticRegression(solver='liblinear', random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, y_pred):.2%}")
coef_df = pd.DataFrame({
    'Feature': x_logis.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("\nCác yếu tố ảnh hưởng nhất đến việc Đậu/Trượt:")
print(coef_df)

data['Predicted_Status'] = model.predict(x_scaled)
data['Pass_Probability'] = model.predict_proba(x_scaled)[:,1]

conditions = [
    (data['Pass_Probability'] <0.5),
    (data['Pass_Probability'] > 0.5) & (data['Pass_Probability'] <0.8),
    (data['Pass_Probability']> 0.8)
]
choices = ['High Risk','Medium Risk','Safe']
data['Risk_Level'] = np.select(conditions, choices, default='Unknown')

comparison = data[['student_id', 'passed_exam', 'Predicted_Status', 'Pass_Probability', 'Risk_Level']]

print("=== BẢNG KẾT QUẢ DỰ BÁO (TOP 10 SINH VIÊN) ===")
print(comparison.head(10))

# Thống kê số lượng từng nhóm rủi ro
print("\n=== THỐNG KÊ NHÓM RỦI RO ===")
print(data['Risk_Level'].value_counts())


# Thực hiện FP-Growth => Tìm kiếm các tập phổ biến trong hành vi học tập

data_fp = data[data.passed_exam == 'Passed'].copy()
labels = ['Low','High']
# Chia dữ liệu thành 4 tập theo Quantile(25%,50%,75%)
for col in numeric_cols:
    data_fp[f'{col}_Bin'] = pd.qcut(data_fp[col], q = [0,0.5,1],labels= labels,duplicates='drop')

cols_bin = [f'{col}_Bin' for col in numeric_cols]
basket = pd.get_dummies(data_fp[cols_bin], prefix=numeric_cols)
# print(basket)

frequen_items = fpgrowth(basket,0.1,use_colnames=True)
rules = association_rules(frequen_items,metric='lift',min_threshold=1)
top_rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by='lift', ascending=False)
score_rules = rules[rules.consequents.astype(str).str.contains('final_exam_score')]
score_rules = score_rules.sort_values(by = 'lift',ascending = False)
print('-------------TOP 10 ---------------------')
print(score_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(20))
print(rules.head(20))


