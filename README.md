# DA_PythonExamInKaggle
🎓 **Student Performance Enhancement System**
Hệ Thống Tối Ưu & Dự Báo Hiệu Suất Sinh Viên Python

**📖 Tổng quan dự án (Project Overview)**
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
 - Mục tiêu:
      + Định danh chân dung người học(Student Segmentation): Thay vì nhìn sinh viên như những cá thể riêng lẻ, gom nhóm các sinh viên dựa theo đặc điểm chung trong việc học tập để hiểu thêm những phong cách học hiện tại.
      + Thiết lập chuẩn: Sử dụng hành vi của nhóm đã đỗ làm 'thước đo'.Từ đó đặt mục tiêu phù hợp cho những sinh viên chưa đạt.
 - Vấn đề giải quyết:
      + Trong học tập, việc một lộ trình học cho tất cả học sinh trong một lớp, giữa nhiều cá thể khác nhau không thể phù hợp cho tất cả. Gây nên sự kém hiệu quả trong việc học tập của 1 số sinh viên.
      + Sử dụng thuật toán học máy không giám sát (Unsupervised Learning) K-Means Clustering để tự động phân tách sinh viên thành các nhóm đặc thù. Điều này giúp nhà trường/hệ thống đưa ra các can thiệp cá nhân hóa (Personalized Intervention) chính xác cho từng nhóm.
 - Các bước thực hiện:
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
  - Mục tiêu:
      + Chuyển từ phân tích mô tả (đã xảy ra) sang phân tích dự báo (Predictive Analytics). Mục tiêu là xây dựng một "Hệ thống cảnh báo sớm", giúp xác định xác suất đỗ/trượt của từng sinh viên ngay từ giai đoạn giữa khóa học để can thiệp kịp thời.
  - Giải quyết vấn đề:
      + Giảng viên không thể theo dõi sát sao hàng nghìn sinh viên. Việc đợi đến khi có điểm thi mới biết ai trượt là quá muộn. Sử dụng Logistic Regression để dự đoán xem sinh viên có thể vượt qua bài kiểm tra hay không?
  - Các bước thực hiện:
    - Bước 1. Chuẩn bị dữ liệu
        + Tương tự với thuật toán KMeans, cần phải chuẩn hóa dữ liệu bằng phương pháp Z-Score để đưa các dữ liệu về cùng 1 thang đo để tránh việc model ưu tiên những dữ liệu lớn.
        + Đối với một số cột có dạng Text(Country,prior_programming_experience) cần phải One-Hot Encoding để giữ lại toàn bộ ngữ cảnh của dữ liệu.
    - Bước 2. Phân tích kết quả của mô hình
        + Áp dụng Logistic Regression, ta nhận được Logistic Regression Accuracy: 91.33%(Cứ 100 sinh viên thì đoán chính xác 91 người). Mô hình này hoàn toàn có thể áp dụng cho bộ dữ liệu này.
    - Bước 3. Phân tích những yếu tố ảnh hưởng
       + Từ những yếu tố ảnh hưởng trên, Thời gian học(hours_spent_learning_per_week) và (projects_completed) là 2 yếu tố ảnh hưởng mạnh mẽ nhất đến sự thành công của sinh viên trong khóa học => Học phải đi đôi với hành, không chỉ cần học lý thuyết mà cần phải thực hành những dự án thì mới có thể thành công được.
       + Thực hành dự án hiệu quả hơn gấp 10 lần việc chỉ xem tutorial video.
       + Các yếu tố như quốc gia hay độ tuổi không gây ảnh hưởng lớn đến việc học.
       + Trình độ Beginner đang ở mốc -1.87 cho thấy rằng nhóm người này cần được hỗ trợ, quan tâm nhiều hơn.
    - Bước 4. Phân tầng rủi ro(Risk Segmentation): Phân chia thành 3 nhóm chính(High Risk < 50%, 50%< Medium Risk < 80%, Safe > 80%)
  - Khuyến nghị:
       + Chương trình "Onboarding" cho Beginner (Giải quyết hệ số -1.87): Vì nhóm Beginner chịu bất lợi lớn (-1.87), hệ thống không thể để họ học chung lộ trình với nhóm Advanced ngay từ đầu.
         Đề xuất: Cần một khóa "Pre-course" hoặc 2 tuần đầu tiên tập trung lấp lỗ hổng kiến thức nền tảng để đưa hệ số này về gần 0 trước khi vào bài khó.
💡**Thực hiện thuật toán FP-Growth để tìm ra phương pháp học tập hiệu quả**
   - Mục tiêu: Thay vì phân tích lý do sinh viên thất bại, dự án tập trung đào sâu vào nhóm sinh viên đã vượt qua khóa học (Passed) để trả lời câu hỏi cốt lõi: **"Đâu là công thức hành vi chung của những người chiến thắng?"**
   - Vấn đề giải quyết: Dữ liệu thô chỉ cho biết ai đậu, ai rớt, nhưng không giải thích được mối quan hệ nhân quả giữa các thói quen học tập. Phân tích thống kê thông thường dễ bỏ qua các tương tác phức tạp (ví dụ: Xem video nhiều nhưng không làm bài tập thì sao?).Dự án sử dụng **Association Rule Mining (Khai phá luật kết hợp)** để tìm ra các mẫu hành vi ẩn (hidden patterns) quyết định hiệu suất học tập.
   - Các bước thực hiện:
       + Bước 1. Filtering Data
           + Lọc bộ dữ liệu chỉ lấy những trường hợp passed_exam == 'Passed' để lấy ra tập hợp những sinh viên đã vượt qua bài kiểm tra.
       + Bước 2. Data discretization(Rời rạc hóa số liệu)
           + Vì thuật toán FP-Growth yêu cầu dữ liệu đầu vào dạng định danh(categorical).Vì vậy,sử dụng kĩ thuật binning theo phân vị. Nhóm dữ liệu dưới ngưỡng phân vị(< 50%) sẽ được đánh nhãn là 'Low' và ngược lại sẽ được gánh nhãn là 'High'
           + Điều này giúp chuẩn hóa các thang đo khác nhau trong dữ liệu về cùng 1 hệ quy chiếu.
       + Bước 3. Áp dụng thuật toán FP-Growth.
           + Áp dụng One-Hot Encoding để chuyển dữ liệu sang dạng Boolean.
           + Sử dụng min_support = 0.1 và min_confidence để loại đi những luật không phổ biến.
           + Support: Độ phổ biến của luật trên toàn bộ bản ghi. Support(A->B) = Số lần xuất hiện của A và B / Tổng số bản ghi.
           + Confident: Xác suất xảy ra B khi A đã xảy ra được sử dụng để đánh giá độ tin cậy của luật này. Confident(A->B) = Số lần xuất hiện của A và B / Số lần xuất hiện của A. Ví dụ: Confidence(A->B) = 75%: Trong 100 sinh viên có A thì 75% đó sẽ có thêm cả B. 
           + Lift: Đánh giá mức độ phụ thuộc giữa A và B.
                +   Lift(A->B) = Confidence(A->B) / Support(B).
                +   Lift > 1: Luật này là hữu ích khi nếu đã xuất hiện A sẽ làm tăng sự xuất hiện của B.
                +   Lift = 1: A và B là 2 thành phần độc lập và không liên quan tới nhau.
                +   Lift < 1: nếu đã xuất hiện A thì làm giảm sự xuất hiện của B.
        + Bước 4. Đánh giá kết quả.
           + Công thức thành công:
                + Hour_high + Project_high => final_exam_high.
                + Luật này chiếm 10% trong bộ dữ liệu và có độ tin cậy 75%.
                + Như vậy việc học tập theo phương pháp(Project-Based Learning) kết hợp với sự đảm bảo về thời gian học là yếu tố quan trọng nhất dẫn đến sự thành công vượt qua khóa học.
           + Vai trò của thực hành:
                + Tiếp theo việc học từ Project thì việc thực hành debug cũng như làm bài tập là những phương pháp mạnh mẽ tiếp theo
           + Cảnh báo về việc học thụ động:
                + Từ bộ dữ liệu, ta nhận thấy rằng việc xem video tutorials không thể đảm bảo việc dành được kết quả cao.
   - Khuyến nghị: 
      - Dành cho giáo viên:
           + Tái cấu trúc trọng số điểm: Nâng trọng số điểm của Project ép buộc sinh viên phải đầu tư thời gian vào việc làm Project nếu muốn đạt điểm cao.
           + Thiết kế bài giảng: Giảm số lượng video tutorial thay vào đó là những buổi thực hành cũng như debug.

**📊 I.Python Course Overview**
<img width="1279" height="716" alt="image" src="https://github.com/user-attachments/assets/59734a7e-7e89-4c25-a998-ca9f19b647c7" />

- Tổng quan:
  + Tổng số người đã tham gia khóa học là **3000 người**.
  + Tuy nhiên,tỉ lệ vượt qua khóa học chỉ ở mức **17.73%** và điểm trung bình của toàn khóa học chỉ ở mức **43.32** còn kém xa so với con số để vượt qua khóa học là **60 điểm**.
  + Biểu đồ Histogram cho chúng ta thấy rằng đa phần sinh viên đang ở mức trung bình, chưa thể vượt qua ngưỡng **60 điểm**. 
  + Khi nhìn vào biểu đồ Treemap, 1/3 sinh viên đang gặp bế tắc trong khóa học, nhóm này cần thực sự được quan tâm nhiều hơn.
  + Và khi nhìn vào biểu đồ phễu, có tới 2000 sinh viên đang ở mức dự báo không thể vượt qua được khóa học.
  => Từ 3 điều trên, chúng ta thấy rằng khóa học đang gặp vấn đề thực sự trong quá trình giảng dạy và không đạt được kết quả cao cũng như đầu ra cũng đang hạn chế. Câu hỏi được đặt ra là:Tại sao họ rớt? Tìm ra chân dung sinh viên để khắc phục vấn đề đang xảy ra.
- 1 Số thông tin khác:
  + Khóa học đang được phổ biến rộng rãi trên toàn thế giới khi châu lục nào cũng có người hiện tại đang theo học khóa học.
  + Những người đã có kinh nghiệm lập trình từ trước khi tham gia khóa học là lợi thế lớn khi điểm trung bình của những người này đang ở ngưỡng vượt qua khóa học.
  + Những sinh viên, người có khả năng tiếp thu kiến thức và học tập nhanh đang đạt hiệu quả cao nhất của khóa học, tuy nhiên vẫn chưa bứt phá được so với những nhóm tuổi còn lại.
 
**📊 II.Student Portrait**
<img width="1262" height="715" alt="image" src="https://github.com/user-attachments/assets/5765541e-a436-4cc4-a9ae-ea6843fa8fc2" />

Sau khi thực thi thuật toán K-Means, Chúng ta đã tìm ra được 3 chân dung khác nhau của sinh viên: Deadlock(Những người đang gặp bế tắc), Passed(Những người đã vượt qua khóa học, lấy mốc làm chuẩn để so sánh, đặt mục tiêu cho những nhóm còn lại), Potential Passed(Những người có khả năng vượt qua khóa học khi sắp tiệm cận với những người passed),Suspect(Những người thuộc diện nhóm nghi ngờ khi không dành nhiều thời gian học tập nhưng lại đạt kết quả cao).
1. Programming Background Distribution:
   + Những người ở nhóm Deadlock và Suspect là những sinh viên chưa có kinh nghiệm lập trình trước đó.
   + Ngược lại thì ở nhóm passed đều là những người đã có kinh nghiệp lập trình từ trước.
2. Learning Behavior Profile:
   +  Deadlock:
       + ⚠️ ĐẶC ĐIỂM NHẬN DẠNG: 'HỌC NHIỀU - HIỂU ÍT'
       + Hành vi: Đây là nhóm 'mọt sách' điển hình nhưng sai phương pháp. Dữ liệu cho thấy họ xem tới **42.51 video (cao nhất lớp)** nhưng chỉ hoàn thành **1.28** dự án.
       + Kết quả: Mặc dù tốn nhiều thời gian, điểm trung bình chỉ đạt **38.23 điểm**.
       +  Hành động: Cần 'cai nghiện' Video. Yêu cầu giảng viên giao bài tập bắt buộc để ép họ thực hành.
   + Suspect:
       + ❓ ĐẶC ĐIỂM NHẬN DẠNG: 'ẨN SỐ'
       +  Hành vi: Số liệu cực kỳ bất thường. Thời gian học trên hệ thống gần như bằng 0, nhưng vẫn nộp đủ bài tập và dự án.
       +  Kết quả: Số lượng bài hoàn thành cũng như số lượng Project đạt ở mức cao. Đây có thể là người đã có kinh nghiệm (Expert) hoặc gian lận.
       +  Hành động: Cần phỏng vấn trực tiếp để xác thực năng lực.
   + Potential Passed:
       +  📈 ĐẶC ĐIỂM NHẬN DẠNG: 'NGƯỜI CẬN ĐÍCH'
       +  Hành vi: Rất chăm chỉ làm bài tập nhỏ (Practice Problems) nhưng còn rụt rè với các Dự án lớn.
       +  Kết quả: Các kết quả học tập có hình dạng RadarChart tương đối giống với nhóm Passed. Chỉ cần chăm chỉ hơn một chút nữa thì sẽ có khả năng chuyển sang nhóm Passed.
       +  Hành động: Hỗ trợ làm thêm những dự án cho nhóm này.
   + Passed:
       + 🏆 ĐẶC ĐIỂM NHẬN DẠNG: 'CHIẾN BINH THỰC TẾ'
       + Hành vi: Nhóm này là hình mẫu lý tưởng. Họ cân bằng hoàn hảo giữa lý thuyết và thực hành. Thực hành tốt sẽ đem lại điểm số cao.
       + Kết quả: Điểm số ấn tượng. Kết quả cao trong final exam.
       + Hành động: Khuyến khích họ làm Mentor (người hướng dẫn) cho nhóm Deadlock.

 **📊 III.Success Driver**
 <img width="1278" height="720" alt="image" src="https://github.com/user-attachments/assets/06b24f65-4bda-4a7e-b1a7-d2efe64028f8" />

 Thực hiện thuật toán FP-Growth, Chúng ta đã tìm được những phương pháp học tốt nhất dẫn đến đạt kết quả cao trong kì thi. 
1. Sankey Graph: Some learning methods have the most powerful impact on grades.
    + Việc học thụ động như việc xem Videos và làm những bài tập nhỏ không hề dẫn đến điểm cao trong kì thi, khi không xuất hiện bất cứ luồng nào có input từ việc xem video tutorials nhiều.
    + Việc dành nhiều thời gian học tập mang lại kết quả cao và cũng phủ sóng lớn trong cộng đồng người đã vượt qua khóa học. Cũng như độ tương quan(lift) dương đang cho thấy sự tích cực và độ confidence cao ở mức 60% cho thấy luật này hoàn toàn có thể tin tưởng được.
    + Tương tự với dành nhiều thời gian cho việc học, làm nhiều Project cũng phổ biến lên tới 17% và độ tin cậy cao.
    + Có 1 luồng đáng chú ý, khi việc kết hợp việc xem ít Video Tutorials và chăm làm Project vẫn sẽ đạt kết quả cao. Càng chứng minh rằng việc học thụ động không hề đem lại nhiều kết quả cho điểm thi.
    + Kết hợp từ 2 yếu tố trên, ta có thể đặt ra kết luận như sau: Chất lượng thực hành (Active Learning) quan trọng hơn số lượng lý thuyết tiêu thụ (Passive Learning).
    + Gợi ý hành động: Thay đổi trọng số của việc học chủ động(Debug,Project) và giảm đi trọng số của việc học thụ động(Tutorials Video). Thay vì giao bài tập lớn làm từ đầu khóa học tới cuối khóa học. Hãy chia nhỏ Project thành nhiều Milestones giúp theo dõi quá trình làm việc của sinh viên, giúp những sinh viên đang gặp bế tắc một cách hiệu quả hơn.

2. Key Influencer: Một số cách để đạt được trạng thái Passed.
    + Dành ra việc học từ 7 đến 12h một tuần có thể tăng tỉ lệ passed lên tới 2 lần.
    + Dành thời gian cho việc làm Project, đặc biệt từ 3 project trở lên sẽ tăng tỉ lệ lên tới 2.55 lần.
    + Ngoài ra, còn nên tham gia những hoạt động debate trên những Forum hay sử dụng các công cụ như Kaggle cũng khiến tỉ lệ Pass tăng lên đáng kể.
  
=> Như vậy sau khi qua Dashboard này, chúng ta có thể kết luận rằng việc học thụ động không thể nào đạt hiệu quả như việc học chủ động.

**📊 IV.Risk Prediction**
<img width="1279" height="702" alt="image" src="https://github.com/user-attachments/assets/1fcd4bec-3a55-4ea3-b94a-3fc5a05bdfb5" />

 Thực hiện thuật toán RandomForestRegression để có thể dự đoán khả năng đỗ của học sinh từ đó có thể đưa ra hành động trước khi kết quả xảy ra.
 Tập trung vào các yếu tố chính gây ảnh hưởng đến điểm thi và phân loại học sinh theo tỉ lệ vượt qua khóa học: 
 + Những học sinh có nguyên nhân chính thiếu Project: Hãy gợi ý học sinh làm thêm Project.
 + Những học sinh có thể thiếu giờ học: Hãy gợi ý học sinh tăng chất lượng buổi học và dành nhiều thời gian học hơn.
 + Những học sinh chưa có người hướng dẫn: Hãy gợi ý học sinh có thể chủ động tìm kiếm thông qua Kaggle hoặc những diễn đàn về lập trình.
 + Những học sinh có nguyên nhân khác: Hãy trao đổi trực tiếp với sinh viên để tìm ra nguyên nhân.

   

