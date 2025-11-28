import psycopg2
from config import load_config

params = load_config()

def user(username):
    
    user_id = None
    last_score = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL
                    );
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_score (
                        score_id SERIAL PRIMARY KEY,
                        user_id INT REFERENCES users(user_id),
                        score INT NOT NULL,
                        level INT NOT NULL
                    );
                """)
                cur.execute("SELECT user_id FROM users WHERE username=%s", (username,))
                res = cur.fetchone()
                if res:
                    user_id = res[0]
                    cur.execute("SELECT score, level FROM user_score WHERE user_id=%s ORDER BY score_id DESC LIMIT 1", (user_id,))
                    last_score = cur.fetchone()
                else:
                    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
                    user_id = cur.fetchone()[0]
        return user_id, last_score
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
        return None, None

def save_score(user_id, score, level):
    
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                conn.commit()
                print("Game saved successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        