import pymysql

conn = pymysql.connect(host="117.50.187.219", user="root", password="123456")

with conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS device_management")
        cursor.execute("USE device_management")

        sql = """CREATE TABLE IF NOT EXISTS device
        (
            device_id VARCHAR(20) NOT NULL,
            device_name VARCHAR(20),
            type VARCHAR(20)
        )
        """

        cursor.execute(sql)