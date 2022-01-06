import mysql.connector

host = '127.0.0.1'
user= 'root'
password= 'tocar123'
database = 'bd_mercado'


def connectaDB():
    conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
    return conexao