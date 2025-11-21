import psycopg2
import os

"""PostgreSQL 데이터베이스에 연결합니다."""

# 환경 변수 또는 기본값으로 데이터베이스 연결 정보 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"
# db_host = os.getenv("DB_HOST", "db_postgresql")
# db_port = os.getenv("DB_PORT", "5432")
# db_name = os.getenv("POSTGRES_DB", "main_db")
# db_user = os.getenv("POSTGRES_USER", "admin")
# db_password = os.getenv("POSTGRES_PASSWORD", "admin123")
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
# return conn
# except psycopg2.OperationalError as e:
#     print(f"데이터베이스 연결에 실패했습니다: {e}")
#     print("연결 정보를 확인하거나 Docker 컨테이너가 실행 중인지 확인하세요.")

# with conn.cursor() as cursor :
#     cursor.execute("INSERT INTO users_uuid_name (name) VALUES ('John Doe'), ('Jane Doe'), ('Alice'), ('Tom');")

# with conn.cursor() as cursor :
#     cursor.execute("""UPDATE users_uuid_name
#     SET name = 'postgres_updated_name'
#     WHERE id_name = '2bb076c5-cfc4-412a-9094-37247cff0950';""")

with conn.cursor() as cursor :
    # cursor.execute("""DELETE FROM users_uuid_name
    #     WHERE id_name = 'f7ce7ffc-f182-4ae2-882c-2e4f631cc530';""")
    cursor.execute("""SELECT name, id_name FROM users_uuid_name;""")
    records = cursor.fetchall()
    for record in records :
        print(record)
        print(f'{record[0]} : {record[1]}')


conn.commit()
