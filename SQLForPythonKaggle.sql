
-- Theo dõi Average Score 
select AVG(final_exam_score) 'Avg Score'
from Python

-- Theo dõi Pass Rate
select count(case when passed_exam = 1 then 1 end) 'numOfPassExam',count(*) 'Total',
		CONCAT(ROUND(count(case when passed_exam = 1 then 1 end) * 100 / count(*),2),'%') 'Pass Rate %'
from Python

 -- So sánh tỷ lệ trượt giữa các nhóm Kinh nghiệm (Beginner vs Advanced vs Intermediate vs None).

select count(case when passed_exam = 1 then 1 end) 'numOfPassExam',count(*) 'Total',
		CONCAT(ROUND(count(case when passed_exam = 1 then 1 end) * 100 / count(*),2),'%') 'Pass Rate %',
		prior_programming_experience 
from Python
group by prior_programming_experience 


-- Phân tích theo Quốc gia (Country) để tìm rào cản địa lý/ngôn ngữ.
select count(case when passed_exam = 1 then 1 end) 'numOfPassExam',count(*) 'Total',
		CONCAT(ROUND(count(case when passed_exam = 1 then 1 end) * 100 / count(*),2),'%') 'Pass Rate %',
		country
from Python
group by country


select *
from Python

select distinct prior_programming_experience 
from Python