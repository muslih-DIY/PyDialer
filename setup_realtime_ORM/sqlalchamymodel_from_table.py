import psycopg2

con = psycopg2.connect(**{
    'dbname': 'PYPBX-RDB',
    'user': 'AsteriskPBX',
    'password': 'PyPbX-secret',
    'host': 'DB-PYPBX'
    }
)

sql = "SELECT * FROM ps_endpoint limit 0"
  
with con.cursor() as cur:   
    cur.execute(sql)
    column_names = [desc[0] for desc in cur.description]
    for i in column_names:
        print(i)
con.commit()
con.close()