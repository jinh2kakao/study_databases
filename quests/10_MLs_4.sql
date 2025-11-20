-- 문제 4

CREATE TABLE keyword_search_logs (
    keyword VARCHAR(255),
    result_count INT,
    search_time TIMESTAMP
);


INSERT INTO keyword_search_logs (keyword, result_count, search_time)
VALUES 
    ('python', 120, '2025-11-19 10:00:00'),
    ('chatgpt', 300, '2025-11-19 10:05:00'),
    ('docker', 90, '2025-11-19 10:10:00');


SELECT * FROM keyword_search_logs 
-- WHERE result_count >= 100;


UPDATE keyword_search_logs 
SET result_count = 150 
WHERE keyword = 'docker';


DELETE FROM keyword_search_logs 
WHERE keyword = 'python';