-- 문제 1

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

SELECT * FROM students;

-- 문제 2
INSERT INTO
    students (id, name, age)
VALUES (1, '홍길동', 23),
    (2, '이영희', 21),
    (3, '박철수', 26);

-- 문제 3
-- 1. 전체 데이터 조회
SELECT * FROM students;

-- 2. 나이가 22세 이상인 학생만 조회
SELECT * FROM students WHERE age >= 22;

-- 3. 이름이 홍길동
SELECT * FROM students WHERE name = '홍길동';

-- 문제 4
UPDATE students SET age = 25 WHERE id = 2;

-- 문제 5
DELETE FROM students WHERE id = 3;

-- 문제 6
-- 1. 어떤 에러가 발생하는가?
-- ERROR 1062 (23000): Duplicate entry '1' for key 'books.PRIMARY'

-- 2. 왜 발생하는가?
-- PRIMARY KEY 중복

-- 3. PRIMARY KEY 의 규칙을 쓰시오
-- 고유성(유일성), NOT NULL