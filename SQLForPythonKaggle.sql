
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


select * from data

-- Tính tỷ lệ pass theo từng mốc thời gian học (tuần / tháng)?

select count(case when passed_exam = 1 then 1 end) 'numOfPassExam',count(*) 'Total',
		CONCAT(ROUND(count(case when passed_exam = 1 then 1 end) * 100 / count(*),2),'%') 'Pass Rate %',
		weeks_in_course
from data 
group by weeks_in_course

--Phát hiện giai đoạn nào tỷ lệ pass giảm mạnh nhất?
select top 1 count(case when passed_exam = 1 then 1 end) 'numOfPassExam',count(*) 'Total',
		CONCAT(ROUND(count(case when passed_exam = 1 then 1 end) * 100 / count(*),2),'%') 'Pass Rate %',
		weeks_in_course
from data 
group by weeks_in_course
order by [Pass Rate %] asc


-- So sánh thời gian học tập trung bình của nhóm passed và failed 
WITH starts AS (
    SELECT 
        passed_exam,
        CAST(AVG(hours_spent_learning_per_week) AS FLOAT) AS avgTime,
        CAST(AVG(projects_completed) AS FLOAT) AS avgProject,
        CAST(AVG(debugging_sessions_per_week) AS FLOAT) AS avgDebug,
        CAST(AVG(practice_problems_solved) AS FLOAT) AS avgPractice,
        CAST(AVG(tutorial_videos_watched) AS FLOAT) AS avgVideo
    FROM data
    GROUP BY passed_exam
),
unpivotedStats AS (
    SELECT 
        passed_exam,
        MetricName,
        MetricValue
    FROM starts
    UNPIVOT (
        MetricValue FOR MetricName IN (avgTime, avgProject, avgDebug, avgPractice, avgVideo)
    ) AS unpvt
)
SELECT 
    MetricName,
    [0] AS Failed_Avg,
    [1] AS Passed_Avg,
    ([1] - [0]) AS Difference
FROM unpivotedStats
PIVOT (
    MAX(MetricValue)
    FOR passed_exam IN ([0], [1])
) AS finalPvt;

-- Segmentation 
select * from data;

/* 
	311: Giờ học nhiều nhưng không thực hành nhiều
	111: Lười học 
	211: Giờ học tương xứng với thực hành
	121: : Học ít làm bài tập tương đối 
	131: Học ít làm bài tập nhiều
	112: Học ít làm Project
	113: Học ít nhưng làm nhiều project
*/
with study_behavior_score as(
	select student_id,NTILE(3) over (order by hours_spent_learning_per_week) 'hour_score',
					  NTILE(3) over (order by practice_problems_solved) 'practice_score',
					  NTILE(3) over (order by projects_completed) 'project_score'
	from data
),
study_behavior_score_final as(
	select student_id,CONCAT(hour_score,practice_score,project_score) 'behavior_study'
	from study_behavior_score
)
SELECT 
    student_id,
    behavior_study,
    CASE behavior_study
        WHEN '311' THEN N'Giờ học nhiều nhưng không thực hành nhiều'
        WHEN '111' THEN N'Lười học'
        WHEN '211' THEN N'Giờ học tương xứng với thực hành'
        WHEN '121' THEN N'Học ít làm bài tập tương đối'
        WHEN '131' THEN N'Học ít làm bài tập nhiều'
        WHEN '112' THEN N'Học ít làm Project'
        WHEN '113' THEN N'Học ít nhưng làm nhiều project'
        ELSE N'Nhóm khác' 
    END AS 'segmentation'
FROM study_behavior_score_final
ORDER BY behavior_study;

select *
from data


-- Segmentation theo Effort
with cte as(
	select avg(hours_spent_learning_per_week) avgHour
	from data
)

select student_id,[hours_spent_learning_per_week],[passed_exam],
		case 
			when  [hours_spent_learning_per_week] >= avgHour and passed_exam = 1 then 'High Effort - Passed'
			when  [hours_spent_learning_per_week] <= avgHour and passed_exam = 1 then 'Low Effort - Passed'
			when  [hours_spent_learning_per_week] >= avgHour and passed_exam = 0 then 'High Effort - Failed'
			when  [hours_spent_learning_per_week] <= avgHour and passed_exam = 0 then 'Low Effort - Passed'
		end as 'Status'
from data 
cross join cte


-- Phát hiện bất thường, học nhiều hơn mức trung bình nhưng vẫn trượt
SELECT
    student_id,
    [hours_spent_learning_per_week]
    passed_exam
FROM data
WHERE
    [hours_spent_learning_per_week] >
        (SELECT AVG([hours_spent_learning_per_week]) FROM data)
    AND passed_exam = '0';

-- Phát hiện outlier  theo IQR

with quartiles as(
	select percentile_cont(0.25) within group   (order by [hours_spent_learning_per_week]) over() Q1,
		   percentile_cont(0.75) within group   (order by [hours_spent_learning_per_week]) over() Q3
	from data
)
select distinct student_id,[hours_spent_learning_per_week]
from data
cross join quartiles 
where [hours_spent_learning_per_week] < Q1  - 1.5 * (Q3 - Q1)
	   or [hours_spent_learning_per_week] > Q3 + 1.5 * (Q3 - Q1)

