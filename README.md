# DA_PythonExamInKaggle
🎓 **Student Performance Enhancement System**
Hệ Thống Tối Ưu & Dự Báo Hiệu Suất Sinh Viên Python
📖 Tổng quan dự án (Project Overview)
Trong bối cảnh giáo dục trực tuyến, việc theo dõi sát sao 3,000 sinh viên là bất khả thi đối với giảng viên. Tỷ lệ trượt môn (Exam Failure) cao không chỉ ảnh hưởng đến uy tín khóa học mà còn lãng phí tài nguyên đào tạo.

Dự án **Student Performance Enhancement System** được xây dựng nhằm cung cấp cho Ban Quản lý Đào tạo (Course Managers) những thông tin chi tiết dựa trên dữ liệu (data-driven insights). Hệ thống không chỉ dừng lại ở báo cáo mô tả mà còn tích hợp các mô hình Machine Learning để dự báo rủi ro và gợi ý lộ trình học tập cá nhân hóa.

🎯 **Mục tiêu chính (Objectives)**
 - Hiểu rõ hiệu suất: Phân tích tình hình học tập hiện tại của sinh viên.

 - Tìm nguyên nhân gốc rễ (Root Cause): Tại sao sinh viên trượt? Yếu tố nào ảnh hưởng nhất?

 - Phân tích hành vi (Behavior Pattern): Sự khác biệt giữa nhóm sinh viên Xuất sắc và Yếu kém.

 - Hỗ trợ ra quyết định: Dự báo sớm kết quả Pass/Fail và cá nhân hóa lộ trình để tăng tỷ lệ đậu.

💡**Design Thinking Process**
  
  Dự án được thực hiện dựa trên quy trình tư duy thiết kế để đảm bảo giải quyết đúng "nỗi đau" của người dùng cuối (Giảng viên & Sinh viên).
  
  **1. Empathize (Thấu cảm)**
    - Vấn đề của Giảng viên: Quá tải khi phải quản lý 3,000 sinh viên. Không thể giám sát quá trình học của từng cá nhân. Chỉ biết kết quả khi sự đã rồi (sau kỳ thi).
    - Vấn đề của Sinh viên: Mỗi người có cách học khác nhau nhưng lộ trình lại được lên kế hoạch cho tất cả sinh viên. Cần được cảnh báo sớm và nhận bài tập phù hợp với trình độ cũng như phù hợp với phương pháp học của bản thân.
 
  **2. Define (Xác định vấn đề)**
    Tỷ lệ trượt môn đang ở mức báo động, đe dọa uy tín khóa học.
    Problem Statement: Cần một hệ thống có khả năng dự báo sớm khả năng trượt (trước khi thi Final) để giáo viên kịp thời can thiệp, đồng thời gợi ý phương pháp học tối ưu cho từng nhóm đối tượng.
  
  **3. Ideate (Giải pháp)**
    
    - Dự báo (Decision Tree/Classification): Xây dựng mô hình dự đoán kết quả Final Exam dựa trên dữ liệu hoạt động các tuần đầu.
    
    - Khai phá luật kết hợp (FP-Growth): Tìm ra các combo hành động hiệu quả nhất (Ví dụ: Dùng Kaggle + Debug nhiều = Điểm cao).
    
    - Recommendation: Gợi ý hành động tiếp theo (Next Best Action) cho sinh viên hỗ trợ đạt kết quả cao nhất.

    - Phân cụm (K-Means): Phân nhóm sinh viên dựa trên hành vi (Giờ học, Debug, Video) để tìm ra các "Personas" khác nhau.
    
📊 **Business Analysis (5W1H)**

  WHO:   Giảng viên & Cố vấn học tập: Cần công cụ giám sát rủi ro. Sinh viên: Cần tự đánh giá năng lực.
  
  WHAT:  Mối quan hệ giữa Thói quen học tập (Input) và Kết quả thi (Output).
  
  WHERE:	Dữ liệu từ nền tảng học trực tuyến, diễn đàn, Kaggle và IDE lập trình.
  
  WHEN:	Phân tích xuyên suốt 15 tuần học. Mục tiêu là dự báo sớm (Real-time tracking).
  
  WHY:	Giảm tỷ lệ trượt, nâng cao chất lượng đào tạo và trải nghiệm người học.
  
  HOW:	Kết hợp: Phân tích mô tả (SQL/Power BI) + Phân tích dự báo (Python/ML)


**❓ Key Business Questions & Insights**
Dự án tập trung trả lời 4 câu hỏi cốt lõi để đưa ra hành động cụ thể như sau:

1. Hiệu suất hiện tại của sinh viên như thế nào?

  - Theo dõi Average Score và Pass Rate %.

  - Xem xét biểu đồ phân phối điểm số (Histogram).

2. Phân khúc nào đóng góp nhiều nhất vào tỷ lệ trượt?

  - So sánh tỷ lệ trượt giữa các nhóm Kinh nghiệm (Beginner vs Advanced).

  - Phân tích theo Quốc gia (Country) để tìm rào cản địa lý/ngôn ngữ.

3. Khoảng cách (Gap) giữa sinh viên Đậu và Trượt là gì?

  - Sinh viên Đậu debug trung bình bao nhiêu lần/tuần?

  - Điểm bão hòa của thời gian học (hours_spent_learning) là bao nhiêu?

4. Hành vi nào cần được ưu tiên cải thiện?

  - Sử dụng Correlation Matrix để xác định yếu tố tác động mạnh nhất (Ví dụ: projects_completed quan trọng hơn tutorial_videos_watched).

**💾 Dataset Description**
  Bộ dữ liệu bao gồm 3,000 dòng, mô phỏng hoạt động học tập của sinh viên Python.
  **https://www.kaggle.com/datasets/emonsharkar/python-learning-and-exam-performance-dataset**

**🛠 Tech Stack & Workflow**
Công nghệ sử dụng
  - Python: Xử lý dữ liệu (Pandas, NumPy) & Machine Learning (Scikit-learn, Mlxtend).

  - SQL: Truy vấn, làm sạch và tổng hợp dữ liệu.

  - Power BI: Trực quan hóa dữ liệu và xây dựng Dashboard tương tác.

**Quy trình thực hiện**
  1. Data Processing: Làm sạch dữ liệu, xử lý missing values, feature engineering (tạo biến Efficiency, Total_Engagement).

  2. Exploratory Data Analysis (EDA): Sử dụng SQL và Python để trả lời các Business Questions.

  3. Machine Learning Modeling:

      - Clustering: K-Means để phân nhóm sinh viên.
      
      - Classification: Decision Tree để dự báo passed_exam.
      
      - Mining: FP-Growth để tìm luật kết hợp.

  4. Dashboarding: Thiết kế báo cáo trên Power BI phục vụ giảng viên

💡**Thực hiện thuật toán KMeans phân cụm dữ liệu**
 - Bước 1. Data Segmentation & Benchmarking (Phân tách & Tạo chuẩn)
      + Tách dữ liệu thành 2 nhóm riêng biệt. Nhóm 1 bao gồm các sinh viên đã đạt(Passed Group) và nhóm 2 bao gồm các sinh viên chưa đạt(Failed Group)
      + Thiết lập chuẩn: Tính toán các chỉ số trung vị của nhóm Passed Group để làm 'Kim chỉ nam' cho nhóm còn lại. Nhóm 2 sẽ được so sánh với chuẩn này để có thể cải thiện khả năng.
 - Bước 2. Data Transforming
      + Log Transform: Vì bộ dữ liệu đưa vào có số lượng bài tập sẽ là số có thể là đơn vị hàng trăm và số lượng dự án đã làm có số lượng nhỏ như vậy dữ liệu sẽ bị lệch phải(right skewed) và làm giảm thiểu tác động của các giá trị outlier.
      + StandardScaler: Đưa bộ dữ liệu về chung 1 thang đo(Z-Score Standardlization) để đảm bảo các giá trị lớn không ảnh hưởng nhiều hơn những giá trị nhỏ như đã đề cập bên trên.
 - Bước 3.  Tìm số cụm tối ưu bằng thuật toán Elbow
      + Sử dụng thuật toán Elbow để xác định điểm gập(nơi mà độ giảm diện tích của từng cụm là nhỏ nhất) => Kết quả đạt được Optimize_K = 6 => Tiếp tục thực hiện KMeans
 - Bước 4. Thực hiện thuật toán KMeans với Optimize_K đã tìm được bên trên
      + Chạy thuật toán K_Means với K = 6 và khởi tạo tâm cụm là ngẫu nhiên. Tuy nhiên sau khi đánh giá kết quả thì k = 6 đưa ra những nhóm có các đặc điểm gần như là tương đương nhau và rất khó có thể phân biệt từng nhóm. Đánh giá K = 6 là chưa hiệu quả với bộ dữ liệu này. Sau khi thử nghiệm k = 3, Kết quả có vẻ đã rõ ràng hơn.
        <img width="641" height="226" alt="image" src="https://github.com/user-attachments/assets/75c622bd-46f7-434e-84ca-7cfdc240a0a8" />
 - Bước 5. Đánh giá kết quả
      + Cluster 0(Nhóm bất thường - Cần phải kiểm tra và đánh giá): Thời gian học ít, số lượng bài tập làm là lớn và số lượng Project đang ở mức khá.Số liệu này là phi logic đối với những người học bình thường có thể đặt ra giả thuyết với nhóm này như sau:
          *  Nhóm Chuyên Gia: là những người từng có prior_programming_experience, học chỉ để lấy chứng chỉ. Đối với những prior_programming_experience = 'Advanced' thì không cần kiểm tra
          *  Nhóm Cheater: Những người không thực sự học mà chỉ copy code để có thể hoàn thiện bài tập để có thể qua môn. Đối với những prior_programming_experience còn lại thì cần một bài kiểm tra để đánh giá thực lực của nhóm này.
      + Cluster 1(Nhóm thực chiến - Khả năng cao sẽ đỗ): Nhóm này dành nhiều thời gian học, làm nhiều dự án nhất. Đây là nhóm học hiệu quả nhất khi chỉ cần dành ít thời gian học thụ động(Xem video Tutorial) nhưng lại thực hành nhiều, chỉ số debug thấp cho thấy rằng logic code tốt ít khi phải debug => Khuyến khích thực hiện thêm các Project.
      + Cluster 2(Nhóm bế tắc - cần phải hỗ trợ): Nhóm này dành nhiều thời gian học nhất, xem Tutorial nhiều nhất, làm bài tập nhiều nhất. Tuy nhiên số lượng Project ít cho thấy rằng nhóm này mới chỉ dừng lại ở lý thuyết mà chưa thực sự tiến tới việc thực hành làm những dự án. Số lần debug cũng nhiều => Điển hình của bẫy hướng dẫn. Họ dành nhiều thời gian cho việc xem Video và sửa lỗi vụn vặt mà không có thời gian để mà tổng hợp kiến thức hoặc thực hành dự án. Cần phải hướng dẫn, đưa ra phương pháp học hiệu quả. Tổng hợp kiến thức cho nhóm này và khuyến khích, hướng dẫn thực hiện Project.

💡 **Xây dựng mô hình dự báo và rủi ro bằng thuật toán Logistic Regression**
  - Bước 1. Chuẩn bị dữ liệu
      + Tương tự với thuật toán KMeans, cần phải chuẩn hóa dữ liệu bằng phương pháp Z-Score trước khi đưa vào mô hình.
      + Đối với một số cột có dạng Text(Country,prior_programming_experience) cần phải One-Hot Encoding để giữ lại toàn bộ ngữ cảnh của dữ liệu.
  - Bước 2. Phân tích kết quả của mô hình
      + Áp dụng Logistic Regression, ta nhận được Logistic Regression Accuracy: 91.33%(Cứ 100 sinh viên thì đoán chính xác 91 người). Mô hình này hoàn toàn có thể áp dụng cho bộ dữ liệu này.
  - Bước 3. Phân tích những yếu tố ảnh hưởng
                         Feature               Coefficient
             hours_spent_learning_per_week     1.669932
                          projects_completed     1.372536
             self_reported_confidence_python     1.022274
                                 uses_kaggle     0.475370
                 debugging_sessions_per_week     0.457181
                    practice_problems_solved     0.448979
           participates_in_discussion_forums     0.203724
                             country_Brazil     0.199423
                           country_Pakistan     0.143672
                     tutorial_videos_watched     0.138292
                                 country_UK     0.119108
                              country_India     0.109469
                            country_Germany     0.097546
                                         age     0.078999
                             weeks_in_course     0.063117
                                country_USA     0.009828
                            country_Nigeria    -0.017627
                          country_Indonesia    -0.024163
                              country_Other    -0.093889
  prior_programming_experience_Intermediate    -0.740901
      prior_programming_experience_Beginner    -1.878632
       prior_programming_experience_unknown    -3.431808
    
     + Từ những yếu tố ảnh hưởng trên, Thời gian học(hours_spent_learning_per_week) và (projects_completed) là 2 yếu tố ảnh hưởng mạnh mẽ nhất đến sự thành công của sinh viên trong khóa học => Học phải đi đôi với hành, không chỉ cần học lý thuyết mà cần phải thực hành những dự án thì mới có thể thành công được.
     + Thực hành dự án hiệu quả hơn gấp 10 lần việc chỉ xem tutorial video.
     + Các yếu tố như quốc gia hay độ tuổi không gây ảnh hưởng lớn đến việc học.
     + Trình độ Beginner đang ở mốc -1.87 cho thấy rằng nhóm người này cần được hỗ trợ, quan tâm nhiều hơn.
   
 - Bước 4. Phân tầng rủi ro(Risk Segmentation): Phân chia thành 3 nhóm chính(High Risk < 50%, 50%< Medium Risk < 80%, Safe > 80%)
  


