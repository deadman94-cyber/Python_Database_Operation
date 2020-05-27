import psycopg2
# def test():
#     try:
#         conn=psycopg2.connect(host="localhost",database="newdb",user="postgres")
#         cur=conn.cursor()
#         d= input("enter a value, probably a name")
#         cur.execute("insert into parts (part_name) values ('%s');" % (str(d)))
#         #part_id=cur.fetchone()[0]
#         conn.commit()
#         cur.close()
#     except(Exception,psycopg2.DatabaseError) as error:
#         print(error)
#     print(" value has been inserted = ",d)
#     conn.close()

def test2():
    try:
        conn=psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur=conn.cursor()
        f = open("bunty.csv",'+a')
        for i in range (0,10):
            d= input("enter a value, probably some names = ")
            cur.execute("insert into parts (part_name) values ('%s');" %(str(d)))
            conn.commit()
            f.write(str(d) + '\n')
            print("value inserted ",d)
            #for g in i:
                
        f.close()        
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    print("all values inserted sucessfully")
    conn.close()


if __name__=='__main__':
    #test()
    test2()


