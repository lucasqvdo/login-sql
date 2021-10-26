from  tkinter import *
from  tkinter import messagebox
from tkinter.font import Font
import Databaser

#Criar Janela#

janela = Tk()

janela.title("PAINEL DE ACESSO DOCE MEL")
janela.geometry("600x300")
janela.configure(background="yellow")

janela.resizable(width=False, height=False)


#Carregar Imagens#



logo = PhotoImage(file="logo.png")



#Criar Widget#
LeftFrame = Frame(janela, width=200, height=300, bg="white", relief="raise")
LeftFrame.pack(side=LEFT)
 
RightFrame = Frame(janela, width=395, height=300, bg="yellow", relief="raise")
RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=logo, bg="white")
LogoLabel.place(x=5, y=60)

UserLabel = Label(RightFrame, text="Usuário", font=("Comic Sans", 20), bg="yellow", fg="brown")
UserLabel.place(x=20, y=100)

PassLabel = Label(RightFrame, text="Senha", font=("Comic Sans", 20), bg="yellow", fg="brown")
PassLabel.place(x=20, y=150)

UserEntry = Entry(RightFrame,width=30)
UserEntry.place(x=130, y=110)

PassEntry = Entry(RightFrame,width=30, show="*")
PassEntry.place(x=130, y=160)

#Botões#
def Back():

    LoginButton.place(x=155, y=200)
    NewButton.place(x=155, y=235)
    
    UserLabel.place(x=20, y=100)
    PassLabel.place(x=20, y=150)
    UserEntry.place(x=130, y=110)
    PassEntry.place(x=130, y=160)
    

def Register():
    LoginButton.place(x=5000)
    NewButton.place(x=50000)
    UserLabel.place(y=150)
    PassLabel.place(y=200)
    UserEntry.place(y=160)
    PassEntry.place(y=210)
    NomeLabel = Label(RightFrame, text="Nome", font=("Comic Sans", 20), bg="yellow", fg="brown")
    NomeLabel.place(x=20, y=50)

    EmailLabel = Label(RightFrame, text="Email", font=("Comic Sans", 20), bg="yellow", fg="brown")
    EmailLabel.place(x=20, y=100)





    
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        DataBaser.cursor.execute("""  
        
        INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)  
        
        
        
         """, (Name, Email, User,Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title="INFORMAÇÃO DE CADASTRO", message="Cadastro Efetuado")
    
    NomeEntry = Entry(RightFrame,width=30)
    NomeEntry.place(x=130, y=50)

    EmailEntry = Entry(RightFrame,width=30)
    EmailEntry.place(x=130, y=100)
    

    RegistrarButton = Button(RightFrame, text="Registrar", width=20, command=RegisterToDataBase)
    RegistrarButton.place(x=155, y=235)

    VoltarButton = Button(RightFrame, text="Voltar", width=20, command=Back)
    VoltarButton.place(x=155, y=270)

    


LoginButton = Button(RightFrame, text="Login", width=20)
LoginButton.place(x=155, y=200)

NewButton = Button(RightFrame, text="Cadastrar", width=20, command=Register)
NewButton.place(x=155, y=235)

janela.mainloop()