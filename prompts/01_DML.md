{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "당신은 최고의 DBA이자 강사입니다. 아래 제공되는 6개의 문제(Part 1 ~ Part 6)를 순서대로 해결하여 하나의 SQL 스크립트를 작성해 주세요.\n\n**[출력 및 작성 가이드]**\n1. 최종 결과물은 '01_DML.sql' 파일에 저장될 내용이어야 합니다.\n2. 각 문제 사이에는 주석(`-- [문제 X]`)을 달아 구분해 주세요.\n3. 문제 6번(서술형)은 SQL 블록 주석(`/* ... */`) 내에 답안을 작성하세요.\n4. 별도의 서론이나 결론 없이, 오직 SQL 코드(주석 포함)만 출력하세요."
        },
        {
          "text": "📌 [문제 1] 테이블 생성 (PRIMARY KEY 기초)\n\n✔ 요구사항\n테이블명: students\n컬럼:\n- id (INT, PRIMARY KEY)\n- name (VARCHAR(50))\n- age (INT)"
        },
        {
          "text": "📌 [문제 2] CREATE (INSERT) 기초\n\n✔ 요구사항\n위 students 테이블에 다음 데이터를 INSERT 하시오.\n(id, name, age 순서)\n- 1, 홍길동, 23\n- 2, 이영희, 21\n- 3, 박철수, 26"
        },
        {
          "text": "📌 [문제 3] READ (SELECT) 기본 조회\n\n✔ 요구사항\n다음 조건들을 만족하는 SELECT 쿼리를 각각 작성하시오.\n1. students 테이블의 전체 데이터를 조회\n2. 나이가 22세 이상인 학생만 조회\n3. name 이 '홍길동'인 학생만 조회"
        },
        {
          "text": "📌 [문제 4] UPDATE 연습\n\n✔ 요구사항\nid = 2 인 학생의 나이를 25로 수정하시오."
        },
        {
          "text": "📌 [문제 5] DELETE 연습\n\n✔ 요구사항\nid = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오."
        },
        {
          "text": "📌 [문제 6] PRIMARY KEY 이해 문제\n\n다음과 같은 테이블을 가정하시오:\nCREATE TABLE books (\n    book_id INT PRIMARY KEY,\n    title VARCHAR(100),\n    price INT\n);\n\n아래 데이터 INSERT 시 발생할 문제를 설명하시오.\nINSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);\nINSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);\n\n✔ 질문:\n1. 어떤 에러가 발생하는가?\n2. 왜 발생하는가?\n3. PRIMARY KEY 의 규칙을 쓰시오."
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.1,
    "maxOutputTokens": 2000
  }
}