class Usuarios:
    def __init__(self, email, senha):
        self.id = None  # Inicialmente None, será atribuído depois
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'ID: {self.id}, Email: {self.email}'
