## Prompts
```
{
  "request_config": {
    "agent_role": "Senior Python Developer & SQL Educator",
    "output_file": "quests/10_DMLs_codes.py",
    "language": "korean"
  },
  "instruction_prompt": {
    "context": "당신은 최고의 파이썬 개발자이자 데이터베이스 교육자입니다. 주어진 `psycopg2` 참조 코드를 바탕으로 PostgreSQL 데이터베이스에 DML(Data Manipulation Language)을 수행하는 파이썬 스크립트를 작성해야 합니다.",
    "task_requirements": [
      "작성할 파일 경로: quests/10_DMLs_codes.py",
      "기존 `students` 테이블이 있다면 DROP 하고 새로 CREATE 할 것.",
      "모든 `id` 컬럼은 `UUID` 타입을 사용하며 `uuid_generate_v4()`를 기본값으로 설정할 것.",
      "문제에 제시된 논리적 ID(1, 2, 3)는 UUID 환경에 맞춰 적절히 변환하여 처리할 것(아래 상세 지침 참조)."
    ],
    "step_by_step_guide": {
      "step_0_setup": "제공된 [참조 코드]의 DB 연결 설정을 그대로 사용할 것. 필요 시 `CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";` 쿼리를 먼저 실행하여 UUID 함수를 활성화할 것.",
      "step_1_create_table": "요구사항에 맞춰 `students` 테이블 생성 (id: UUID PK, name: VARCHAR, age: INT).",
      "step_2_insert": "문제의 데이터(홍길동, 이영희, 박철수)를 INSERT 하시오. **주의**: 문제에는 ID가 1, 2, 3으로 되어 있으나 DB는 UUID이므로, ID 값은 DB가 자동 생성하도록 하고 name과 age만 INSERT 하시오.",
      "step_3_select": "전체 조회, 22세 이상 조회, 이름이 '홍길동'인 학생 조회를 수행하는 쿼리를 작성하고 결과를 출력하시오.",
      "step_4_update": "문제: 'ID=2인 학생 수정'. **해결**: UUID 환경이므로, 먼저 `name='이영희'`(논리적 ID 2)인 학생의 UUID를 조회(SELECT)한 뒤, 그 UUID를 사용하여 나이를 25로 UPDATE 하시오.",
      "step_5_delete": "문제: 'ID=3인 학생 삭제'. **해결**: `name='박철수'`(논리적 ID 3)인 학생의 UUID를 조회(SELECT)한 뒤, 그 UUID를 사용하여 DELETE 하시오.",
      "step_6_theory": "스크립트 하단에 주석(Docstring)으로 문제 6번에 대한 답을 작성하시오. (UUID 컬럼에 정수 '1'을 넣을 때 발생하는 'invalid input syntax for type uuid' 에러와 PK 유일성 규칙에 대해 설명).",
      "final_check": "모든 트랜잭션은 `conn.commit()`으로 확정하고 연결을 안전하게 닫을 것."
    },
    "reference_code": "import psycopg2\n\ndb_host = \"db_postgresql\"\ndb_port = \"5432\"\ndb_name = \"main_db\"\ndb_user = \"admin\"\ndb_password = \"admin123\"\n\nconn = psycopg2.connect(\n    host=db_host,\n    port=db_port,\n    dbname=db_name,\n    user=db_user,\n    password=db_password\n)\n# ... (connection logic)"
  }
}
```