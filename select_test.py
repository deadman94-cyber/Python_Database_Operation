import psycopg2


def con():
    conn = None

    try:
        conn = psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur = conn.cursor()
        print("Print databse db version")
        cur.execute("select version()")

        db_version=cur.fetchone()
        print(db_version)

        cur.close()
    except(Exception,   psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("database connection close")
if __name__ == "__main__":
    con()