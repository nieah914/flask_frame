import pymssql
conn = pymssql.connect(server='211.49.99.25', user='nieah914', password='godls914!!', database='city')
cursor = conn.cursor()
cursor.execute(
    'SELECT * FROM test')
row = cursor.fetchone()

print(row)