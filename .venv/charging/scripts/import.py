import psycopg2

# establish connection to postgresql database and insert charging points data
def run():
    conn = psycopg2.connect(
    database="charging_db",
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    sql1 = '''copy charging_chargingpoint(operator, street, house_number, zip_code, city, power, number_ports) from 'C:\Temp\charging_points.csv' delimiter ';';'''
    cursor.execute(sql1)

    conn.commit()
    conn.close()

