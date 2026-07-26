from database import create_connection

def top_ip():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ip, COUNT(*) AS total
        FROM logs
        GROUP BY ip
        ORDER BY total DESC
        LIMIT 1;
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def brute_force():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ip, COUNT(*) AS tentativas
        FROM logs
        WHERE endpoint = '/login' AND status = 401
        GROUP BY ip
        HAVING COUNT(*) >= 5;
    """)

    result = cursor.fetchall()

    connection.close()

    return result