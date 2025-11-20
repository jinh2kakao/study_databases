-- 문제 1
CREATE TABLE news_articles (
    title VARCHAR(255),
    url VARCHAR(255),
    author VARCHAR(100),
    published_at DATE
);

INSERT INTO news_articles (title, url, author, published_at)
VALUES 
    ('AI 시대 도래', 'https://news.com/ai', '홍길동', '2025-01-01'),
    ('경제 성장률 상승', 'https://news.com/economy', '이영희', '2025-01-05');

SELECT * FROM news_articles 
--WHERE author = '홍길동';

UPDATE news_articles
SET title = 'AI 시대의 급격한 변화'  -- 변경하고 싶은 새로운 제목
WHERE title = 'AI 시대 도래';

DELETE FROM news_articles 
WHERE title = '경제 성장률 상승';


-- 문제 2
CREATE TABLE web_links (
    link_text VARCHAR(100),  -- 링크 텍스트 (예: 네이버)
    link_url VARCHAR(255),   -- 실제 주소
    category VARCHAR(50)     -- 카테고리
);


INSERT INTO web_links (link_text, link_url, category)
VALUES 
    ('네이버', 'https://naver.com', 'portal'),
    ('구글', 'https://google.com', 'portal'),
    ('깃허브', 'https://github.com', 'dev');


SELECT * FROM web_links 
WHERE category = 'portal';


UPDATE web_links
SET category = 'code'
WHERE link_text = '깃허브';


DELETE FROM web_links 
WHERE link_text = '네이버';


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


-- 문제 5

CREATE TABLE shop_products (
    name VARCHAR(255),
    price INT,
    stock INT,
    category VARCHAR(255)
);


INSERT INTO shop_products (name, price, stock, category)
VALUES 
    ('USB 메모리', 12000, 50, '전자제품'),
    ('블루투스 스피커', 45000, 20, '전자제품'),
    ('물병', 5000, 100, '생활용품');


SELECT * FROM shop_products 
WHERE price >= 10000;


UPDATE shop_products 
SET stock = 80 
WHERE name = '물병';


DELETE FROM shop_products 
WHERE name = '블루투스 스피커';