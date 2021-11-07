from getpass import getpass
import pymysql
# import pymysql.cursors
 

con = pymysql.connect(host='localhost',
    user='root',
    password=getpass("Пароль: "),
    db='parser_knig',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
try:
    with con as connection:
        print(connection)
        cur = con.cursor()
        
        cur.execute("SELECT * FROM knigi") 
        # row  = cur.fetchone()
        rows  = cur.fetchall()
        for row in rows:
            print(row['avtor'],row['cikl'])
except pymysql.Error as e:
    print(e)
else :
    cur.close()