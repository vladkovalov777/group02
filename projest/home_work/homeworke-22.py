import config
import psycopg2

from redis_service.base import result

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                content TEXT,
                user_id INTEGER REFERENCES users(id),
                topic_id INTEGER REFERENCES topics(id)
            );
        """)

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        topics_to_add = [
            ("Python programming",),
            ("Databases",),
            ("AI and Machine Learning",)
        ]
        cursor.executemany("INSERT INTO topics (title) VALUES (%s)", topics_to_add)
        connection.commit()