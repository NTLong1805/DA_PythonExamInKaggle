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
