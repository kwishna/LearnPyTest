import psycopg2


def fetch_all_users():
    """Fetch all users from the database."""
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
