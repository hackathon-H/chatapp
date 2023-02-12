import pymysql

# データベースへの接続を定義するためのクラス
class DB:
    def getConnection():
        try:
            connection = pymysql.connect(host="localhost",
                                         user="user",
                                         password="passwd",
                                         database="chatapp",
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except (ConnectionError):
            print("コネクションエラーです")
            connection.close()