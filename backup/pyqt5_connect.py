import mysql.connector
from sshtunnel import SSHTunnelForwarder
import pymysql

# try:
#     server = SSHTunnelForwarder(
#       ssh_address=('kenflix.xyz', 22),
#       ssh_username='kenflixx_pyqt5',
#       ssh_password='Evans1324$M',
#       remote_bind_address=('127.0.0.1', 3306))
    
#     server.start()

#     con= pymysql.connect(host='188.165.52.14', user='kenflixx_pyqt5', passwd='Evans1324$M', db='kenflixx_pyqt5', port=3306)
#     print('connected')
# except:
#     print(Exception)

# with SSHTunnelForwarder(
#     ('****.ucd.ie',22),  
#     ssh_password='****',
#     ssh_username='s****t',
#     remote_bind_address=('127.0.0.1', 3306)) as server:  
 
#     db_connect = pymysql.connect(host='51.69.29.218',  
#                                  port="",
#                                  user='kenflixx_pyqt5',
#                                  passwd='Evans1324$M',
#                                  db='kenflixx_pyqt5')
 
#     cur = db_connect.cursor()
#     cur.execute('SELECT stop_num FROM dublinbus.stops limit 10;')
#     data=cur.fetchone()
#     print(data[0])

try:
  mydb = mysql.connector.connect(
    host="197.136.58.40",
    user="kenflixx_pyqt5",
    password="Evans1324$M",
    database="kenflixx_pyqt5"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO users (id, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
  val = (1, "John", "Doe", "john@example.com", "123456")

  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
except Exception as e:
  print("Data not inserted:", str(e))
