import psycopg2
import xlsxwriter  
import csv  



def sel():
    conn = None
    try:

        #with open('Python.csv', 'w') as csvfile: 
        #writer = csv.DictWriter(csvfile) 

        conn = psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur = conn.cursor()
        print("lets run a select query")
        cur.execute("select call_history.phone,call_history.date_added,cm_cdr_history.voice_resource_id from call_history inner join cm_cdr_history on call_history.call_leg_id=cm_cdr_history.call_leg_id where call_history.date_added::date = '2020-03-12' and call_history.system_disposition = 'CONNECTED' order by call_history.date_added")
        #workbook = xlsxwriter.Workbook('select_with_join.xlsx')
        #worksheet = workbook.add_worksheet()  
        

        #row = 0  
        #column = 0  
        f = open("new.csv","w")
        for r in range (1,20):
            row = cur.fetchone()
            #print(row)
            #f = open("python.txt","w")
            #for g in range (1,20):
            f.write(str(row) + "\r\n")

            
                #writer.writerow(row)
         #   worksheet.write(row,r)
          #  row+=1
        #print("The data is =",cur.rowcount())
        #for row in rows:
         #   print(row)
                      
        cur.close()
        f.close()

    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("connection lost")
        
if __name__ == "__main__":
    sel()
