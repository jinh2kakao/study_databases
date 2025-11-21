## Prompts
```
{
  "request_config": {
    "agent_role": "Senior Python Developer & SQL Educator",
    "output_file": "quests/10_DMLs_codes.py",
    "language": "korean",
    "format": "python_script"
  },
  "instruction_prompt": {
    "context": "당신은 파이썬과 PostgreSQL 전문가입니다. 주어진 `psycopg2` 코드를 기반으로 DML 문제를 해결하는 스크립트를 작성해야 합니다. 특히 UUID 환경에서의 Update/Delete 처리를 위한 'Option' 요구사항을 명확한 단계별 로직으로 구현하는 것이 핵심입니다.",
    "task_requirements": [
      "작성 파일: quests/10_DMLs_codes.py",
      "기존 `students` 테이블이 존재하면 DROP 후 새로 CREATE 할 것.",
      "ID 컬럼은 UUID 타입을 사용하며 `uuid_generate_v4()`를 기본값으로 설정.",
      "각 문제(Problem)마다 주석을 달고 해당 코드를 작성할 것."
    ],
    "step_by_step_guide": {
      "step_0_init": "DB 연결 설정(참조 코드 활용). `uuid-ossp` extension 활성화 쿼리 실행.",
      "step_1_create": "문제 1: `students` 테이블 생성 (id: UUID, name: VARCHAR, age: INT).",
      "step_2_insert": "문제 2: 데이터 3건 INSERT (홍길동, 이영희, 박철수). *참고: 문제의 정수 ID(1,2,3)는 무시하고 UUID 자동 생성을 따름.*",
      "step_3_select": "문제 3: 전체 조회, 22세 이상 조회, '홍길동' 조회 쿼리 실행 및 결과 출력.",
      "step_4_update_with_option": "문제 4 (Option 적용): 'ID=2(이영희)'인 학생의 나이를 25로 수정.\n[구현 지침]\n1. `SELECT id FROM students WHERE name='이영희'`를 실행하여 UUID를 가져와 파이썬 변수(`target_id`)에 저장/출력.\n2. `UPDATE ... WHERE id = %s` 구문에 `target_id`를 사용하여 수정.",
      "step_5_delete_with_option": "문제 5 (Option 적용): 'ID=3(박철수)'인 학생을 삭제.\n[구현 지침]\n1. `SELECT id FROM students WHERE name='박철수'`를 실행하여 UUID를 가져와 파이썬 변수(`target_id`)에 저장/출력.\n2. `DELETE ... WHERE id = %s` 구문에 `target_id`를 사용하여 삭제.",
      "step_6_theory": "문제 6: 스크립트 하단에 멀티라인 주석(''' ... ''')으로 정답 작성. 다음 3가지를 반드시 포함할 것:\n1. [실제 에러]: UUID 컬럼에 정수 '1'을 입력하여 발생하는 'Data Type Mismatch' 에러 설명.\n2. [잠재적 에러]: 만약 타입이 맞다고 가정했을 때, 동일한 ID('1')를 두 번 입력하여 발생하는 'Primary Key Violation (Uniqueness)' 에러 설명.\n3. [PK 규칙]: Primary Key의 2가지 핵심 규칙(Unique, Not Null) 서술.",
      "final_step": "모든 변경 사항 `conn.commit()` 후 연결 종료."
    },
    "reference_code": "import psycopg2\n\n# ... (기존 DB 연결 설정 코드 사용)"
  }
}
```