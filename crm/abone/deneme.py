import psycopg2
import time



def create():
    try:
        conn = psycopg2.connect("dbname='farmirr'user='postgres'host='127.0.0.1'password='ufuk123456'")
        print("Bağlanıldı")
    except:
        print("Bağlantı Hatası")

    subsCreateDay = time.strftime("%y" + "%m" + "%d") # BUGÜNÜN TARİHİ
    subscriberId = "10" + subsCreateDay # 10 + BUGÜNÜN TARİHİ
    cur = conn.cursor()
    cur.execute("""SELECT subscriber_id FROM abone_subscribercreate""")
    rows = cur.fetchall()
    lastId = rows[-1]
    cur.close()
    lastId = lastId[0]
    print("Son ID  "+lastId)
    lastIdNumber = lastId[8:] #8den sonrasını alıyor


    if not lastIdNumber: #çekilen id boşsa
        subscriberId = subscriberId + "001"
        cur = conn.cursor()
        cur.execute("UPDATE abone_subscribercreate SET subscriber_id = %s WHERE subscriber_id = %s",(subscriberId, lastId))
        conn.commit()


    lastIdDate = lastId[2:8]
    if lastIdDate != subsCreateDay: # Yeni güne geçilmiş ise
        subscriberId = subscriberId + "001"

    else: #aynı gündeysen
        newid = str()
        if (int(lastIdNumber) + 1) < 10:
            newid = str(subscriberId[:8] + ("00" + (str(int(lastIdNumber) + 1))))
            print(newid)

        elif (int(lastIdNumber) + 1) >= 10:
            print("bakbura")
            newid = str(subscriberId + ("0" + (str(int(lastIdNumber) + 1))))
            print(newid)

        elif (int(lastIdNumber) + 1) > 99:
            newid = str(subscriberId + str(int(lastIdNumber) + 1))
            print(newid)
        return newid

        cur = conn.cursor()
        cur.execute("UPDATE abone_subscribercreate SET subscriber_id = %s WHERE subscriber_id = %s",(newid, lastId))
        conn.commit()
create()