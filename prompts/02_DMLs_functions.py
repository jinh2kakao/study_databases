import psycopg2
import uuid

# 데이터베이스 연결 설정
DB_CONFIG = {
    "host": "db_postgresql",
    "port": "5432",
    "dbname": "main_db",
    "user": "admin",
    "password": "admin123"
}

def get_db_connection():
    """데이터베이스 연결 객체를 생성하여 반환합니다."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"DB 연결 오류: {e}")
        return None

def create_books_table(conn):
    """books 테이블을 생성합니다. (uuid-ossp 확장 사용)"""
    try:
        with conn.cursor() as cur:
            # UUID 생성을 위한 확장 설치 (권한 필요, 없을 시 오류 발생 가능하나 일반적으로 허용됨)
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
            
            cur.execute("DROP TABLE IF EXISTS books;")
            
            cur.execute("""
                CREATE TABLE books (
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    title VARCHAR(255) NOT NULL,
                    price INT NOT NULL
                );
            """)
        conn.commit()
        print("books 테이블이 생성되었습니다.")
    except Exception as e:
        conn.rollback()
        print(f"테이블 생성 중 오류 발생: {e}")

def insert_books(conn):
    """초기 도서 데이터를 삽입합니다."""
    books_data = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]
    try:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO books (title, price) VALUES (%s, %s)", books_data)
        conn.commit()
        print("3개 도서가 삽입되었습니다.")
    except Exception as e:
        conn.rollback()
        print(f"데이터 삽입 중 오류 발생: {e}")

def get_all_books(conn):
    """전체 도서 목록을 조회합니다."""
    with conn.cursor() as cur:
        # 순서 보장을 위해 제목으로 정렬하거나, 단순히 입력 순서(heap scan)를 따를 수 있습니다.
        # 여기서는 리스트 인덱싱 요구사항을 위해 별도 정렬 없이 가져오되,
        # 실무에서는 ORDER BY를 권장합니다.
        cur.execute("SELECT * FROM books;")
        return cur.fetchall()

def get_expensive_books(conn):
    """가격이 25000원 이상인 도서를 조회합니다."""
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM books WHERE price >= 25000;")
        return cur.fetchall()

def get_book_by_title(conn, title):
    """제목으로 도서를 검색합니다."""
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM books WHERE title = %s;", (title,))
        return cur.fetchall()

def update_second_book_price(conn):
    """목록의 두 번째 도서 가격을 27000원으로 수정합니다."""
    books = get_all_books(conn)
    
    if len(books) < 2:
        print("수정할 데이터가 충분하지 않습니다 (2개 미만).")
        return

    # 파이썬 리스트 인덱싱[1] -> 두 번째 도서
    target_book = books[1] 
    target_id = target_book[0] # UUID
    
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE books SET price = 27000 WHERE id = %s;", (target_id,))
        conn.commit()
        print("두 번째 도서 가격이 27000으로 수정되었습니다.")
    except Exception as e:
        conn.rollback()
        print(f"수정 중 오류 발생: {e}")

def delete_third_book(conn):
    """목록의 세 번째 도서를 삭제합니다."""
    # 전체 목록 다시 조회
    books = get_all_books(conn)
    
    if len(books) < 3:
        print("삭제할 데이터가 충분하지 않습니다 (3개 미만).")
        return

    # 파이썬 리스트 인덱싱[2] -> 세 번째 도서
    target_book = books[2]
    target_id = target_book[0] # UUID
    
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM books WHERE id = %s;", (target_id,))
        conn.commit()
        print("세 번째 도서가 삭제되었습니다.")
    except Exception as e:
        conn.rollback()
        print(f"삭제 중 오류 발생: {e}")

if __name__ == '__main__':
    conn = get_db_connection()
    
    if conn:
        try:
            # 1. 테이블 생성
            create_books_table(conn)
            
            # 2. 데이터 삽입
            insert_books(conn)
            
            # 3. 데이터 조회 (검증)
            print("\n[전체 도서 목록]")
            for book in get_all_books(conn):
                print(book)
                
            print("\n[가격 25000원 이상]")
            for book in get_expensive_books(conn):
                print(book)
                
            print("\n['네트워크 이해' 검색]")
            for book in get_book_by_title(conn, '네트워크 이해'):
                print(book)
            
            # 4. 데이터 수정 (두 번째 도서)
            print("\n[수정 실행]")
            update_second_book_price(conn)
            
            # 5. 데이터 삭제 (세 번째 도서)
            print("\n[삭제 실행]")
            delete_third_book(conn)
            
            # 최종 확인
            print("\n[최종 도서 목록]")
            for book in get_all_books(conn):
                print(book)
                
        finally:
            conn.close()
            print("\nDB 연결이 종료되었습니다.")
