import psycopg2
import psycopg2.extras # For dictionary cursor
import os

def main():
    """
    Main function to execute the database operations for the student management quest.
    """
    db_host = os.getenv("DB_HOST", "db_postgresql")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "main_db")
    db_user = os.getenv("DB_USER", "admin")
    db_password = os.getenv("DB_PASSWORD", "admin123")

    conn = None
    cursor = None

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        # Use a dictionary cursor for easier column access by name
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        print("--- 데이터베이스 연결 성공 ---")

        # Step 0: Enable UUID extension
        print("\n--- [단계 0] UUID 확장 활성화 ---")
        cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
        print("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"; 실행 완료")

        # Step 1: Create the students table
        print("\n--- [단계 1] 테이블 생성 ---")
        cursor.execute("""
            DROP TABLE IF EXISTS students;
        """)
        print("DROP TABLE IF EXISTS students; 실행 완료")
        
        create_table_query = """
        CREATE TABLE students (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,
            age INT
        );
        """
        cursor.execute(create_table_query)
        print("CREATE TABLE students; 실행 완료")

        # Step 2: Insert student data
        print("\n--- [단계 2] 데이터 삽입 ---")
        students_to_insert = [
            ('홍길동', 20),
            ('이영희', 22),
            ('박철수', 23)
        ]
        insert_query = "INSERT INTO students (name, age) VALUES (%s, %s);"
        cursor.executemany(insert_query, students_to_insert)
        print(f"{cursor.rowcount}명의 학생 데이터 삽입 완료.")

        # Step 3: Select student data
        print("\n--- [단계 3] 데이터 조회 ---")
        
        # 3-1: Select all students
        print("\n[3-1] 전체 학생 조회:")
        cursor.execute("SELECT * FROM students ORDER BY age;")
        all_students = cursor.fetchall()
        for student in all_students:
            print(f"  ID: {student['id']}, 이름: {student['name']}, 나이: {student['age']}")

        # 3-2: Select students with age >= 22
        print("\n[3-2] 나이가 22세 이상인 학생 조회:")
        cursor.execute("SELECT * FROM students WHERE age >= 22 ORDER BY age;")
        students_over_22 = cursor.fetchall()
        for student in students_over_22:
            print(f"  ID: {student['id']}, 이름: {student['name']}, 나이: {student['age']}")

        # 3-3: Select student with name '홍길동'
        print("\n[3-3] 이름이 '홍길동'인 학생 조회:")
        cursor.execute("SELECT * FROM students WHERE name = '홍길동';")
        gildong = cursor.fetchone()
        if gildong:
            print(f"  ID: {gildong['id']}, 이름: {gildong['name']}, 나이: {gildong['age']}")

        # Step 4: Update student data
        print("\n--- [단계 4] 데이터 수정 ---")
        # Problem: Update student with logical ID=2
        # Solution: Find the UUID for '이영희' (logical ID 2) first
        print("'이영희' 학생의 UUID를 조회합니다.")
        cursor.execute("SELECT id FROM students WHERE name = '이영희';")
        younghee_record = cursor.fetchone()
        if younghee_record:
            younghee_uuid = younghee_record['id']
            print(f"'이영희'의 UUID는 {younghee_uuid} 입니다.")
            print("해당 UUID를 사용하여 나이를 25로 수정합니다.")
            cursor.execute("UPDATE students SET age = 25 WHERE id = %s;", (younghee_uuid,))
            print(f"{cursor.rowcount}명의 학생 정보 수정 완료.")
            
            # Verify the update
            cursor.execute("SELECT * FROM students WHERE id = %s;", (younghee_uuid,))
            updated_student = cursor.fetchone()
            print("수정 확인:", f"ID: {updated_student['id']}, 이름: {updated_student['name']}, 나이: {updated_student['age']}")
        else:
            print("'이영희' 학생을 찾을 수 없습니다.")

        # Step 5: Delete student data
        print("\n--- [단계 5] 데이터 삭제 ---")
        # Problem: Delete student with logical ID=3
        # Solution: Find the UUID for '박철수' (logical ID 3) first
        print("'박철수' 학생의 UUID를 조회합니다.")
        cursor.execute("SELECT id FROM students WHERE name = '박철수';")
        chulsoo_record = cursor.fetchone()
        if chulsoo_record:
            chulsoo_uuid = chulsoo_record['id']
            print(f"'박철수'의 UUID는 {chulsoo_uuid} 입니다.")
            print("해당 UUID를 사용하여 학생 정보를 삭제합니다.")
            cursor.execute("DELETE FROM students WHERE id = %s;", (chulsoo_uuid,))
            print(f"{cursor.rowcount}명의 학생 정보 삭제 완료.")
            
            # Verify the deletion
            cursor.execute("SELECT * FROM students WHERE id = %s;", (chulsoo_uuid,))
            deleted_student = cursor.fetchone()
            if not deleted_student:
                print(f"UUID {chulsoo_uuid}에 해당하는 학생이 성공적으로 삭제되었음을 확인했습니다.")
        else:
            print("'박철수' 학생을 찾을 수 없습니다.")
        
        # Final check of the table state
        print("\n--- 최종 데이터 확인 ---")
        cursor.execute("SELECT * FROM students ORDER BY age;")
        final_students = cursor.fetchall()
        for student in final_students:
            print(f"  ID: {student['id']}, 이름: {student['name']}, 나이: {student['age']}")

        # Commit the transaction
        conn.commit()
        print("\n--- 모든 변경사항이 데이터베이스에 커밋되었습니다. ---")

    except psycopg2.Error as e:
        print(f"데이터베이스 오류: {e}")
        if conn:
            conn.rollback() # Rollback on error
    finally:
        # Close the connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("\n--- 데이터베이스 연결이 종료되었습니다. ---")


if __name__ == "__main__":
    main()

