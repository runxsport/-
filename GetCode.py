import pymysql

host = 'rm-uf6bst1i3h32z267uto.mysql.rds.aliyuncs.com'
port = 3306
user = 'sports'
passwd = 'RUNX123#'
database = 'live_catalina'
charset = "utf8"
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, database=database,charset=charset)
cursor = conn.cursor()
while True:
    phone = input("请输入手机号：")
    cursor.execute('select code from sms_history where phone = "%s" and result = "OK" order by create_time asc limit 1' % phone)
    print(str(cursor.fetchall())[3:9])