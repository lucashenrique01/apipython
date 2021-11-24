import mysql.connector
from credentials import usr, pswd

def insert_db(nickname, jogoEscolhido, statusPartida, frag):
    try:  
        mydb = mysql.connector.connect(
            host = "localhost",
            user = usr,
            password = pswd,
            database = "lucasHenriqueAc3"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor()

            sql_query = "INSERT INTO tbPartidas() VALUES (null, %s, %s, %s, %s, now())"
            val = [nickname, jogoEscolhido, statusPartida, frag]
            mycursor.execute(sql_query, val)

            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")