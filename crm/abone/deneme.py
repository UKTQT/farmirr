import psycopg2
import time



def create():
    try:
        conn = psycopg2.connect("dbname='farmirr'user='postgres'host='127.0.0.1'password='ufuk123456'")
        print("Bağlanıldı")
    except:
        print("Bağlantı Hatası")

    subsCreateDay = time.strftime("%y" + "%m" + "%d")
    subscriberId = "SB" + subsCreateDay
    cur = conn.cursor()
    cur.execute("""SELECT subscriber_id FROM abone_subscribercreate""")
    rows = cur.fetchall()
    lastId = rows[-1]

    cur.close()
    lastId = lastId[0]
    lastIdNumber = lastId[8:]

    if not lastIdNumber:
        subscriberId = subscriberId + "001"
        cur = conn.cursor()
        sql = """INSERT INTO abone_subscribercreate(subscriber_id) VALUES(%s);"""
        cur.execute(sql, [subscriberId])
        conn.commit()

    lastIdDate = lastId[2:8]
    if lastIdDate != subsCreateDay:
        subscriberId = subscriberId + "001"
    else:
        newid = str()

        if (int(lastIdNumber) + 1) < 10:
            newid = str(subscriberId + ("00" + (str(int(lastIdNumber) + 1))))
            print(newid)
        elif (int(lastIdNumber) + 1) >= 10:
            newid = str(subscriberId + ("0" + (str(int(lastIdNumber) + 1))))
            print(newid)
        elif (int(lastIdNumber) + 1) > 99:
            newid = str(subscriberId + str(int(lastIdNumber) + 1))
            print(newid)
        return newid

        cur = conn.cursor()
        sql = """INSERT INTO subs(id) VALUES(%s);"""
        cur.execute(sql, [newid])
        conn.commit()

create()