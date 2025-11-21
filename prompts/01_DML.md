최고의 DBA이자 강사로서 다음문제 해결.

📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
✔ 요구사항
테이블명: students


컬럼:


id (INT, PRIMARY KEY)


name (VARCHAR(50))


age (INT)



📌 문제 2 — CREATE (INSERT) 기초
✔ 요구사항
위 students 테이블에 다음 데이터를 INSERT 하시오.
id
name
age
1
홍길동
23
2
이영희
21
3
박철수
26


📌 문제 3 — READ (SELECT) 기본 조회
다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
students 테이블의 전체 데이터를 조회


나이가 22세 이상인 학생만 조회


name 이 “홍길동”인 학생만 조회



📌 문제 4 — UPDATE 연습
✔ 요구사항
id = 2 인 학생의 나이를 25로 수정하시오.


📌 문제 5 — DELETE 연습
✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.

📌 문제 6 — PRIMARY KEY 이해 문제
다음과 같은 테이블을 가정하시오:
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

아래 데이터 INSERT 시 발생할 문제를 설명하시오.
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

📌 질문:
어떤 에러가 발생하는가?


왜 발생하는가?


PRIMARY KEY 의 규칙을 쓰시오.

