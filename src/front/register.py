from tkinter import Button, Entry, Label, Tk, messagebox
from pydantic import ValidationError
from src.domain.dtos import UserDTO
from src.services import UserService
from src.common.base import TkinterBase
from .activies import ListActivies

class Register(TkinterBase):
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Tela de Cadastro")
        self.master.geometry("300x200")
        self.master.resizable(True, True)

        # Usuário
        self.label_username = Label(master, text="Usuário:")
        self.label_username.pack(pady=(20, 5))
        self.entry_username = Entry(master)
        self.entry_username.pack()

        # Email
        self.label_email = Label(master, text="Email:")
        self.label_email.pack(pady=(20, 5))
        self.entry_email = Entry(master)
        self.entry_email.pack()

        # Senha
        self.label_password = Label(master, text="Senha:")
        self.label_password.pack(pady=(10, 5))
        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        # Botão de login
        self.button_register = Button(master, text="Entrar", command=self.register)
        self.button_register.pack(pady=20)

        self.button_register = Button(master, text="Login", command=self.login)
        self.button_register.pack(pady=20)

    def login(self):
        from .login import Login
        return self.open_window(Login)
    def register(self):
        try:
            data = UserDTO(
                username=self.entry_username.get(),
                email=self.entry_email.get(),
                password=self.entry_password.get(),
            )

            service = UserService()
            service.create_user(data)
            messagebox.showinfo("Cadastro bem-sucedido", f"Bem-vindo, {data.username}!")
            self.master.destroy()
            self.open_window(ListActivies, destroy=True)
        except (ValidationError,ValueError) as e:
            if type(e) == ValueError:
                messagebox.showerror("Erro", f"{e}")
            else:
                dict = {
                    f"{error['loc'][0]}_message": error["msg"].replace("Value error, ", "")
                    for error in e.errors()
                }
                for message in dict.values():
                    messagebox.showerror("Cadastro falhou", f"{message}")
