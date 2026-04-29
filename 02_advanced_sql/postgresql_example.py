import psycopg2


drop_table_sql = "DROP TABLE IF EXISTS customer;"

create_table_sql =  """CREATE TABLE customer (
    c_id INT PRIMARY KEY,
    c_name VARCHAR(50),
    zip_code VARCHAR(20)
);"""

insert_sql = "INSERT INTO customer VALUES (1, 'Sarah', 10963);"


connection = psycopg2.connect("dbname='demo_db_internals' user='postgres' host='localhost'")

cursor = connection.cursor()
cursor.execute(drop_table_sql)
cursor.execute(create_table_sql)
cursor.execute(insert_sql)


cursor.execute("SELECT * FROM customer")
result = cursor.fetchall()

print(result)
