import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



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
print(fail_group)
print('Passed Student:\n')
print(mark_feature)

# Log Transform => tránh dữ liệu lệch phải
data_loga = pd.DataFrame()
data_loga['hours_spent_learning_per_week'] = np.log1p(fail_group['hours_spent_learning_per_week'])
data_loga['practice_problems_solved'] = np.log1p(fail_group.practice_problems_solved)
data_loga['projects_completed']= np.log1p(fail_group.projects_completed)
data_loga['tutorial_videos_watched'] = np.log1p(fail_group.tutorial_videos_watched)
data_loga['debugging_sessions_per_week'] = np.log1p(fail_group.debugging_sessions_per_week)


scaler = StandardScaler()
data_scaler = scaler.fit_transform(data_loga)
data_scaled = pd.DataFrame(data_scaler,columns=feature)
data_scaled['student_id'] = data['student_id']

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
print(f'Số cụm tối ưu:{optimal_k}')

plt.plot(K_range,wcss,marker = "o",linestyle="--")
plt.xlabel(K_range)
plt.ylabel("WCSS")
plt.title("Biểu đồ Elbow chọn K tối ưu")
for i,txt in enumerate(wcss):
    plt.text(K_range[i],wcss[i],f"{round(wcss[i],2)}",fontsize = 9,ha="left",va="bottom")
plt.grid(True)
plt.show()

kmeansFinal = KMeans(optimal_k,init='k-means++',random_state=42,n_init = 10)
kmeansFinal.fit(X)
cluster_label = kmeansFinal.labels_
fail_group['Cluster'] = cluster_label
print(fail_group)

cluster_analysis = fail_group.groupby('Cluster')[feature].mean()
cluster_analysis['Size_Cluster'] = fail_group.groupby('Cluster').size()
print(cluster_analysis)









