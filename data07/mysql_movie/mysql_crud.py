import pymysql

def create(insert):
    con = pymysql.connect(host='localhost', port=3306, user='root', password=None, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    # sql = 'insert into movie(title, jumsu) values (%s, %s)'
    sql = 'insert into movie(jumsu) values (%s)'
    result = cur.execute(sql, insert)
    print('처리 결과 >> ',result)

    con.commit()
    con.close()