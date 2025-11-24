## prompts
```
{
  "request_config": {
    "agent_role": "Senior Python Backend Developer",
    "output_file": "prompts/02_DMLs_functions.py",
    "language": "korean",
    "format": "python_script"
  },
  "instruction_prompt": {
    "context": "당신은 Python과 PostgreSQL을 연동하여 백엔드 기능을 구현하는 전문가입니다. 주어진 요구사항에 맞춰 기능별로 함수를 분리하여 코드를 작성하고, 메인 실행 블록에서 이를 순차적으로 호출하여 테스트해야 합니다.",
    "database_config": {
      "host": "db_postgresql",
      "port": "5432",
      "dbname": "main_db",
      "user": "admin",
      "password": "admin123"
    },
    "task_requirements": [
      "모든 기능은 독립적인 함수로 구현할 것.",
      "ID는 UUID 타입을 사용하며 `uuid-ossp` 확장을 활용할 것.",
      "코드 최하단에 `if __name__ == '__main__':` 블록을 만들어 작성한 함수들을 순서대로 실행하고 결과를 출력할 것."
    ],
    "step_by_step_implementation": {
      "step_1_setup": "DB 연결 객체(conn)와 커서(cursor)를 관리하는 로직 작성 (필요시 전역 변수 혹은 클래스 활용).",
      "step_2_create_table": "`create_books_table()` 함수 작성.\n- 기존 `books` 테이블이 있다면 DROP.\n- `books` 테이블 생성 (id: UUID PK, title: VARCHAR, price: INT).\n- 실행 후 'books 테이블이 생성되었습니다.' 출력.",
      "step_3_insert": "`insert_books()` 함수 작성.\n- 책 3권 데이터 삽입 (1. 파이썬 입문/19000, 2. 알고리즘 기초/25000, 3. 네트워크 이해/30000).\n- *주의: 문제의 정수 ID는 무시하고 DB가 UUID를 자동 생성하도록 할 것.*\n- 실행 후 '3개 도서가 삽입되었습니다.' 출력.",
      "step_4_selects": "조회용 함수 3개 작성.\n1. `get_all_books()`: 전체 조회.\n2. `get_expensive_books()`: 가격 25000원 이상 조회.\n3. `get_book_by_title(title)`: 제목으로 검색.\n- 각 함수는 조회된 데이터를 반환(Return)하거나 출력할 것.",
      "step_5_update_by_index": "`update_second_book_price()` 함수 작성.\n[로직]\n1. `get_all_books()` 혹은 `SELECT`로 전체 목록을 가져온다(fetchall).\n2. 파이썬 리스트 인덱싱(`[1]`)을 통해 **두 번째 도서**의 UUID를 확보한다.\n3. 확보한 UUID를 이용해 가격을 27000으로 UPDATE한다.\n4. '두 번째 도서 가격이 27000으로 수정되었습니다.' 출력.",
      "step_6_delete_by_index": "`delete_third_book()` 함수 작성.\n[로직]\n1. 전체 목록을 다시 조회한다.\n2. 파이썬 리스트 인덱싱(`[2]`)을 통해 **세 번째 도서**의 UUID를 확보한다.\n3. 확보한 UUID를 이용해 해당 도서를 DELETE한다.\n4. '세 번째 도서가 삭제되었습니다.' 출력.",
      "step_7_main_execution": "`if __name__ == '__main__':` 블록 작성.\n- 위에서 정의한 함수들을 논리적 순서(생성->삽입->조회->수정->삭제)대로 호출하여 동작을 검증하는 코드 작성."
    }
  }
}
```