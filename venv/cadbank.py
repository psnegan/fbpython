import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'fbradesco',
    database = 'bank'

)
cursor = conexao.cursor()
 