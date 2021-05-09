import pymysql

def create(datas):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password=None)
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)


    sql = 'insert into movie(title) values (%s)'
    # sql = 'insert into movie(jumsu) values (%s)'
    # sql = 'insert into movie(title, jumsu) values (%s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과', result, '개')

    con.commit()
    con.close()