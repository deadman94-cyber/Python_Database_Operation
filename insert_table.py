import psycopg2

def insert_tab():
    #conn = None
   # commands = (
        # """
        # CREATE TABLE vendors (
        #     vendor_id SERIAL PRIMARY KEY,
        #     vendor_name VARCHAR(255) NOT NULL
        # );
        # """,
        # """ CREATE TABLE parts (
        #         part_id SERIAL PRIMARY KEY,
        #         part_name VARCHAR(255) NOT NULL
        #         );
        # """,
        # """
        # CREATE TABLE part_drawings (
        #         part_id INTEGER PRIMARY KEY,
        #         file_extension VARCHAR(5) NOT NULL,
        #         drawing_data BYTEA NOT NULL,
        #         FOREIGN KEY (part_id)
        #         REFERENCES parts (part_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # );
        # """,
        # """
        # CREATE TABLE vendor_parts (
        #         vendor_id INTEGER NOT NULL,
        #         part_id INTEGER NOT NULL,
        #         PRIMARY KEY (vendor_id , part_id),
        #         FOREIGN KEY (vendor_id)
        #             REFERENCES vendors (vendor_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE,
        #         FOREIGN KEY (part_id)
        #             REFERENCES parts (part_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE
        # );
        # """)
    #conn=None
    try:
        conn = psycopg2.connect(host="localhost",database="newdb",user="postgres")
        cur = conn.cursor() 

        # com = (create table vendors (
        #     vendor_id SERIAL PRIMARY KEY,
        #     vendor_name VARCHAR(255) NOT NULL
        # )
        # ;
        #  CREATE TABLE parts (
        #         part_id SERIAL PRIMARY KEY,
        #         part_name VARCHAR(255) NOT NULL
        #         )
        # ;
        # CREATE TABLE part_drawings (
        #         part_id INTEGER PRIMARY KEY,
        #         file_extension VARCHAR(5) NOT NULL,
        #         drawing_data BYTEA NOT NULL,
        #         FOREIGN KEY (part_id)
        #         REFERENCES parts (part_id)
        #         ON UPDATE CASCADE ON DELETE CASCADE
        # );
        # CREATE TABLE vendor_parts (
        #         vendor_id INTEGER NOT NULL,
        #         part_id INTEGER NOT NULL,
        #         PRIMARY KEY (vendor_id , part_id),
        #         FOREIGN KEY (vendor_id)
        #             REFERENCES vendors (vendor_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE,
        #         FOREIGN KEY (part_id)
        #             REFERENCES parts (part_id)
        #             ON UPDATE CASCADE ON DELETE CASCADE
        # );)
        cur.execute("CREATE TABLE vendors (vendor_id SERIAL PRIMARY KEY,vendor_name VARCHAR(255) NOT NULL);CREATE TABLE parts (part_id SERIAL PRIMARY KEY,part_name VARCHAR(255) NOT NULL);CREATE TABLE part_drawings (part_id INTEGER PRIMARY KEY,file_extension VARCHAR(5) NOT NULL,drawing_data BYTEA NOT NULL,FOREIGN KEY (part_id)REFERENCES parts (part_id) ON UPDATE CASCADE ON DELETE CASCADE);CREATE TABLE vendor_parts (vendor_id INTEGER NOT NULL,part_id INTEGER NOT NULL, PRIMARY KEY (vendor_id , part_id),FOREIGN KEY (vendor_id)REFERENCES vendors (vendor_id)ON UPDATE CASCADE ON DELETE CASCADE,FOREIGN KEY (part_id)REFERENCES parts (part_id)ON UPDATE CASCADE ON DELETE CASCADE);")
        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    print("it's done bitch")
    conn.close()

if __name__ == "__main__":
    insert_tab()
    



