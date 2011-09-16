DATABASE_USER_MYSQL = "user"
DATABASE_PASS_MYSQL = "pass"
DATABASE_NAME_MYSQL = "tester"
DATABASE_ENGINE = "mysql"

def cursor():
    global cursor, conn
    import MySQLdb
    conn = MySQLdb.connect (host = "localhost", user = DATABASE_USER_MYSQL, passwd = DATABASE_PASS_MYSQL, db = DATABASE_NAME_MYSQL)
    cursor = conn.cursor()
    return cursor

def cursor_close():
    global cursor, conn
    cursor.close()
    conn.close()
