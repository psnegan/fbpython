import pymysql

def limpatela():
    # Clearing the screen
    # os.system('cls')  # You may skip this line if not needed

    # Establishing database connection
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='fbradesco',
        database='agenda'
    )

    # Creating cursor
    cursor = conexao.cursor()

    # Fetching data
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    print(resultados)

    # Inserting data
    dados = ("Maria Aparecida", "ma@gmail.com", "11982728728", "Exemplo usando inserção no python")
    cursor.execute("INSERT INTO usuarios(nome, email, telefone, mensagem) VALUES (%s, %s, %s, %s)", dados)

    # Committing changes
    conexao.commit()

    # Closing connection
    conexao.close()

# Calling the function
limpatela()
