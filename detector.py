from database import create_connection

SENSITIVE_ENDPOINTS = [
    "/.env",
    "/.git",
    "/backup.zip",
    "/config.php",
    "/phpmyadmin",
    "/server-status",
    "/admin",
    "/administrator",
    "/test",
    "/old"
]

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

def top_endpoints(limit=5):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT endpoint, COUNT(*) AS total
        FROM logs
        GROUP BY endpoint
        ORDER BY total DESC
        LIMIT ?;
    """, (limit,))

    result = cursor.fetchall()

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

def directory_enumeration(min_404=10):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ip, COUNT(*) AS total
        FROM logs
        WHERE status = 404
        GROUP BY ip
        HAVING COUNT(*) >= ?;
    """, (min_404,))
    
    result = cursor.fetchall()

    connection.close()

    return result