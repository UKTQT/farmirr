import psycopg2
import time


"""def create():
    try:
        conn = psycopg2.connect("dbname='SIS-TEST'user='postgres'host='45.158.14.218'password='Sonofantonv1'")
        print("Bağlanıldı")

    except:
        print("Bağlantı Hatası")
    subsCreateDay = time.strftime("%y" + "%m" + "%d")
    subscriberId = "SB" + subsCreateDay
    cur = conn.cursor()
    cur.execute(SELECT id  FROM subs)
    rows = cur.fetchall()
    print(rows)
    lastId = rows[-1]
    cur.close()
    lastId = lastId[0]
    lastIdNumber = lastId[8:]
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

        cur = conn.cursor()
        sql = INSERT INTO subs(id) VALUES(%s);
        cur.execute(sql, [newid])
        conn.commit()
        return newid


create()"""
subsCreateDay = time.strftime("%y" + "%m" + "%d")
subscriberId = "SB" + subsCreateDay
lasId = '003'
id = subscriberId + lasId
newid = subscriberId + ("00" + (str(int(lasId) + 1)))
print(id)
print(newid)

