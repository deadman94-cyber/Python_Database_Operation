import psycopg2

def insert_single(vendor_name):
    sql="insert into vendors(vendor_name) values(%s) RETURNING vendor_id"
    try:
        conn=psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur = conn.cursor()
        cur.execute(sql,(vendor_name))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    print("once value inserted")
    conn.close()
def insert_list(vendor_list):
    sql="insert into vendors(vendor_name) values(%s)"
    try:
        conn=psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur = conn.cursor()
        cur.executemany(sql,(vendor_list))
        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    print("list inserted")
    conn.close()
if __name__=="__main__":
    insert_single("3M CO.")
    insert_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])

