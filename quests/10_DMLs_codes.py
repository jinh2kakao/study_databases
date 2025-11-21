# -*- coding: utf-8 -*-
import psycopg2
import os

def get_postgres_connection():
    """PostgreSQL 연결 객체를 반환합니다."""
    # 중요: 실제 운영 환경에서는 환경 변수나 보안 설정 파일을 사용하는 것이 좋습니다.
    # 이 스크립트는 교육용으로 하드코딩된 값을 사용합니다.
    return psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
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

    # 문제 2: 데이터 3건 INSERT
    print("\n--- [문제 2] 데이터 3건 삽입 ---")
    insert_query = "INSERT INTO students (name, age) VALUES (%s, %s);"
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
    
    print("\n[3-1] 전체 학생 조회:")
    cur.execute("SELECT * FROM students;")
    all_students = cur.fetchall()
    for row in all_students:
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

    # 문제 4: '이영희' 학생의 나이를 25로 수정 (Option 적용)
    print("\n--- [문제 4] 학생 정보 수정 (UUID 활용) ---")
    # 1. 이름으로 UUID 조회
    cur.execute("SELECT id FROM students WHERE name = '이영희';")
    target_id_tuple = cur.fetchone()
    if target_id_tuple:
        target_id = target_id_tuple[0]
        print(f"'이영희' 학생의 UUID: {target_id}")

        # 2. 조회된 UUID를 사용하여 나이 수정
        update_query = "UPDATE students SET age = 25 WHERE id = %s;"
        cur.execute(update_query, (target_id,))
        print(f"'이영희' 학생의 나이를 25로 성공적으로 수정했습니다.")
    else:
        print("'이영희' 학생을 찾을 수 없습니다.")

    # 문제 5: '박철수' 학생을 삭제 (Option 적용)
    print("\n--- [문제 5] 학생 정보 삭제 (UUID 활용) ---")
    # 1. 이름으로 UUID 조회
    cur.execute("SELECT id FROM students WHERE name = '박철수';")
    target_id_tuple = cur.fetchone()
    if target_id_tuple:
        target_id = target_id_tuple[0]
        print(f"'박철수' 학생의 UUID: {target_id}")

        # 2. 조회된 UUID를 사용하여 데이터 삭제
        delete_query = "DELETE FROM students WHERE id = %s;"
        cur.execute(delete_query, (target_id,))
        print(f"'박철수' 학생의 정보를 성공적으로 삭제했습니다.")
    else:
        print("'박철수' 학생을 찾을 수 없습니다.")

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
