--PostgreSQL 데이터베이스에서 **UUID(범용 고유 식별자)**를 생성하는 기능을 활성화
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users_uuid_name (
    id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4 (),
    name VARCHAR(100)
);

SELECT * FROM users_uuid_name;

INSERT INTO
    users_uuid_name (name)
VALUES ('John Doe'),
    ('Jane Doe'),
    ('Alice'),
    ('Tom');