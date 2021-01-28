from banco import Banco

class Usuarios(object):
    def __init__(self, id_usuario = 0, nome="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.id_usuario = id_usuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("INSERT INTO usuarios (nome, telefone, email, usuario, senha) VALUES ('"+ self.nome +"', '"+ self.telefone +"', '"+ self.email +"', '"+ self.usuario +"', '"+ self.senha +"')")

            banco.conexao.commit()
            c.close()

            return "Usuario cadastrado com sucesso!"
        except:
            return "Ocorre um erro na inserção do usuário"
    
    def updateUser(self):
        
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email +
                "', usuario = '" + self.usuario + "', senha = '" + self.senha +
                "' where id_usuario = " + self.id_usuario + " ")
            banco.conexao.commit()
            c.close()
            
            return "Usuario atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
        
    def deleteUser(self):
        
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("DELETE FROM usuarios WHERE id_usuario = "+ self.id_usuario +"")

            banco.conexao.commit()
            c.close()

            return "Usuario excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário!"
    
    def selectUser(self, id_usuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM usuarios WHERE id_usuario = "+ id_usuario +"")

            for linha in c:
                self.id_usuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"