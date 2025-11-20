-- 문제 3
CREATE TABLE scraping_html_results (
    page_title VARCHAR(255),
    page_url VARCHAR(2048),
    html_length INT,
    status_code INT
);
INSERT INTO scraping_html_results (page_title, page_url, html_length, status_code)
VALUES 
    ('홈페이지', 'https://site.com', 15700, 200),
    ('블로그', 'https://blog.com', 9800, 200),
    ('404 페이지', 'https://site.com/notfound', 0, 404);


SELECT * FROM scraping_html_results 
--WHERE status_code = 200;


UPDATE scraping_html_results 
SET html_length = 12000 
WHERE page_title = '블로그';


DELETE FROM scraping_html_results 
WHERE status_code = 404;