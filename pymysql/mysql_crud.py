import pymysql


def connect():
    return pymysql.connect(host="117.50.187.219", user="root", password="123456")

def add(list):
    conn = connect()
    device_id = list[0]
    device_name = list[1]
    type = list[2]
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("USE device_management")
            sql = f"INSERT INTO device(device_id,device_name,type) VALUES('{device_id}','{device_name}','{type}')"
            cursor.execute(sql)
            conn.commit()

def delete(device_id):
    conn = connect()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("USE device_management")
            sql = f"DELETE FROM device WHERE device_id = '{device_id}'"
            cursor.execute(sql)
            conn.commit()

def get_one(device_id):
    conn = connect()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("USE device_management")
            sql = f"SELECT * FROM device WHERE device_id = '{device_id}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            print('id=%s, name=%s, type=%s' % (result[0], result[1], result[2]))

def get_all():
    conn = connect()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("USE device_management")
            sql = "SELECT * FROM device"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print('id=%s, name=%s, type=%s' % (row[0], row[1], row[2]))

args = input()
args_list = args.split(' ')
method = args_list[0]

if method == 'ADD':
    add(args_list[1:])
elif method == 'DEL':
    delete(args_list[1])
elif method == 'GET':
    if len(args_list) > 1:
        get_one(args_list[1])
    else:
        get_all()
