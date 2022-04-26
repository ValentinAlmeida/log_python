import mysql.connector

con = mysql.connector.connect(host='192.168.1.19', database='radio', user='root', password='imtech123')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MYSQL, versão ", db_info)

    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()

    print("Conectado ao banco de dados ", linha)

if con.is_connected():
    cursor.close()
    con.close()

    print("Conexão encerrada")