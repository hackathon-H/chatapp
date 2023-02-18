import pymysql

# データベースへの接続を定義するためのクラス
class DB:
    def getConnection():
        try:
            connection = pymysql.connect(host="localhost",
                                         user="user",
                                         password="password",
                                         database="chatapp",
                                         charset="utf8",
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except (ConnectionError):
            print("コネクションエラーです")
            connection.close()