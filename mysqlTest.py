import pymysql.cursors

mysqldb_user = "root"
mysqldb_password = "123456"
mysql_host = "localhost"
mysql_port = 3306
db_name = "mysql"

connection = pymysql.connect(host=mysql_host,
                             user=mysqldb_user,
                             password=mysqldb_password,
                             db=db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
