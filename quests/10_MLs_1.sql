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
SET title = 'AI 시대의 급격한 변화'
WHERE title = 'AI 시대 도래';

DELETE FROM news_articles 
WHERE title = '경제 성장률 상승';
