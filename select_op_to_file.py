import psycopg2

def my():
    #conn = None
    try:
        conn = psycopg2.connect(host="localhost",database="newdb",user="postgres")

        cur = conn.cursor()

        print ("lets print a select query")
        cur.execute("select call_history.phone,call_history.date_added,cm_cdr_history.voice_resource_id from call_history inner join cm_cdr_history on call_history.call_leg_id=cm_cdr_history.call_leg_id where call_history.date_added::date = '2020-03-12' and call_history.system_disposition = 'CONNECTED' order by call_history.date_added")
        
        f = open("mytest3.csv",'w')
        
        for r in range (0,20):
            row = cur.fetchone()
            print(str(row))
            f.write(str(row)+ '\n\r')

        f.close()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    #finally:
        #if conn is not None:
    print("connection closed bitch")
    conn.close()


if __name__ == "__main__":
    my()


