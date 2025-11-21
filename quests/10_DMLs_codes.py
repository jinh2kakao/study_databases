# -*- coding: utf-8 -*-
import psycopg2
import os

def get_postgres_connection():
    """PostgreSQL 연결 객체를 반환합니다."""
    # codes/postgres_connection.py의 설정을 참고하여 수정함
    return psycopg2.connect(
        host="db_postgresql",   # localhost -> db_postgresql
        port="5432",
        dbname="main_db",       # mydatabase -> main_db
        user="admin",           # myuser -> admin
        password="admin123"     # mypassword -> admin123
    )

# -- 스크립트 시작 --

# 초기 설정: 데이터베이스 연결 및 커서 생성
try:
    conn = get_postgres_connection()
    cur = conn.cursor()
    print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

    # 문제 0: uuid-ossp 확장 기능 활성화
    print("\n--- [문제 0] uuid-ossp 확장 기능 활성화 ---")
    cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
    print("uuid-ossp 확장이 활성화되었습니다.")

    # 문제 1: 'students' 테이블 생성 (기존 테이블이 있다면 삭제)
    print("\n--- [문제 1] students 테이블 생성 ---")
    cur.execute("DROP TABLE IF EXISTS students;")
    create_table_query = """
    CREATE TABLE students (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        name VARCHAR(100),
        age INT
    );
    """
    cur.execute(create_table_query)
    print("students 테이블을 성공적으로 생성했습니다.")

    # 문제 2: 데이터 3건 INSERT (순서대로)
    print("\n--- [문제 2] 데이터 3건 순서대로 삽입 ---")
    insert_query = "INSERT INTO students (name, age) VALUES (%s, %s);"
    # 1.홍길동, 2.이영희, 3.박철수 순서를 지켜 삽입
    students_to_insert = [
        ('홍길동', 20),
        ('이영희', 22),
        ('박철수', 28)
    ]
    for student in students_to_insert:
        cur.execute(insert_query, student)
    print("데이터 3건을 성공적으로 삽입했습니다.")

    # 문제 3: 데이터 조회 (전체, 조건, 특정)
    print("\n--- [문제 3] 데이터 조회 ---")
    
    # NOTE: 문제의 '순서' 가정을 맞추기 위해 ORDER BY 없이 조회 (삽입 순서 유지 기대)
    print("\n[3-1] 전체 학생 조회:")
    cur.execute("SELECT * FROM students;") 
    all_students_initial = cur.fetchall()
    for row in all_students_initial:
        print(f"ID: {row[0]}, 이름: {row[1]}, 나이: {row[2]}")

    print("\n[3-2] 22세 이상 학생 조회:")
    cur.execute("SELECT * FROM students WHERE age >= 22;")
    students_over_22 = cur.fetchall()
    for row in students_over_22:
        print(f"ID: {row[0]}, 이름: {row[1]}, 나이: {row[2]}")

    print("\n[3-3] '홍길동' 학생 조회:")
    cur.execute("SELECT * FROM students WHERE name = '홍길동';")
    gildong = cur.fetchone()
    if gildong:
        print(f"ID: {gildong[0]}, 이름: {gildong[1]}, 나이: {gildong[2]}")

    # 문제 4: 두 번째 학생(이영희)의 나이를 25로 수정 (Index 기반)
    print("\n--- [문제 4] 학생 정보 수정 (Index 기반) ---")
    # 1, 2. 전체 목록 조회
    cur.execute("SELECT id, name, age FROM students;")
    students_list_for_update = cur.fetchall()
    
    if len(students_list_for_update) > 1:
        # 3. 두 번째(Index 1) 레코드의 UUID 추출
        # 예상: 홍길동(0), 이영희(1), 박철수(2) -> Index 1은 이영희
        target_student_record = students_list_for_update[1] 
        target_id = target_student_record[0]
        print(f"수정 대상 학생(Index 1): {target_student_record[1]}, UUID: {target_id}")

        # 4. 추출한 UUID로 UPDATE 실행
        update_query = "UPDATE students SET age = 25 WHERE id = %s;"
        cur.execute(update_query, (target_id,))
        print(f"'{target_student_record[1]}' 학생의 나이를 25로 성공적으로 수정했습니다.")
    else:
        print("수정할 데이터가 충분하지 않습니다 (2명 미만).")


    # 문제 5: 세 번째 학생(박철수)을 삭제 (Index 기반)
    print("\n--- [문제 5] 학생 정보 삭제 (Index 기반) ---")
    # 1, 2. 전체 목록 다시 조회
    cur.execute("SELECT id, name, age FROM students;")
    students_list_for_delete = cur.fetchall()

    if len(students_list_for_delete) > 2:
        # 3. 세 번째(Index 2) 레코드의 UUID 추출
        # 예상: 홍길동(0), 이영희(1), 박철수(2) -> Index 2는 박철수
        target_student_record = students_list_for_delete[2] 
        target_id = target_student_record[0]
        print(f"삭제 대상 학생(Index 2): {target_student_record[1]}, UUID: {target_id}")

        # 4. 추출한 UUID로 DELETE 실행
        delete_query = "DELETE FROM students WHERE id = %s;"
        cur.execute(delete_query, (target_id,))
        print(f"'{target_student_record[1]}' 학생의 정보를 성공적으로 삭제했습니다.")
    else:
        print("삭제할 데이터가 충분하지 않습니다 (3명 미만).")


    # 최종 결과 확인
    print("\n--- 최종 데이터 확인 ---")
    cur.execute("SELECT * FROM students;")
    final_students = cur.fetchall()
    if not final_students:
        print("테이블에 남은 데이터가 없습니다.")
    for row in final_students:
        print(f"ID: {row[0]}, 이름: {row[1]}, 나이: {row[2]}")

    # 변경사항 커밋
    conn.commit()
    print("\n모든 변경사항이 데이터베이스에 커밋되었습니다.")


except (Exception, psycopg2.DatabaseError) as error:
    print(f"데이터베이스 작업 중 에러 발생: {error}")
    # 에러 발생 시 롤백
    if 'conn' in locals() and conn is not None:
        conn.rollback()


finally:
    # 연결 종료
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
    print("\nPostgreSQL 연결이 종료되었습니다.")


# 문제 6: 이론 문제 정답
'''
--- [문제 6] SQL 에러 및 PK 규칙에 대한 설명 ---

1. [실제 에러: 데이터 타입 불일치 (Data Type Mismatch)]
   - 에러 발생 상황: `id` 컬럼은 UUID 타입으로 지정되어 있는데, `INSERT INTO students (id, name, age) VALUES (1, '김유신', 30);` 와 같이 정수 '1'을 `id` 값으로 직접 입력하려고 시도할 때 발생합니다.
   - 원인: PostgreSQL은 엄격한 데이터 타입을 적용하므로, UUID가 와야 할 자리에 다른 타입(정수)의 값이 오면 타입을 변환할 수 없어 에러를 발생시킵니다.
   - 정확한 에러 메시지 예시: `ERROR: column "id" is of type uuid but expression is of type integer`

2. [잠재적 에러: 기본 키 중복 (Primary Key Violation)]
   - 에러 발생 상황: 만약 `id` 컬럼이 정수형이고, `id`가 1인 데이터가 이미 존재하는 상태에서 `INSERT INTO students (id, name, age) VALUES (1, '강감찬', 40);` 처럼 동일한 `id` 값 '1'을 가진 데이터를 또 삽입하려고 시도할 때 발생합니다.
   - 원인: 기본 키(Primary Key)로 지정된 컬럼은 테이블 내에서 반드시 고유한(Unique) 값을 가져야 한다는 제약조건을 위반했기 때문입니다.
   - 정확한 에러 메시지 예시: `ERROR: duplicate key value violates unique constraint "students_pkey"`

3. [PK(기본 키)의 2가지 핵심 규칙]
   - 1. 고유성 (Uniqueness): 기본 키로 지정된 컬럼의 모든 값은 테이블 내에서 유일해야 합니다. 중복된 값을 허용하지 않습니다.
   - 2. NOT NULL: 기본 키 컬럼은 NULL 값을 가질 수 없습니다. 반드시 특정 값을 가져야 합니다.
'''