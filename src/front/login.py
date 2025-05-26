from tkinter import Button, Entry, Label, Tk, messagebox
from pydantic import ValidationError
from src.domain.dtos import LoginDTO
from src.services import AuthService
from .activies import ListActivies
from .register import Register
from src.common.base import TkinterBase


class Login(TkinterBase):
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x200")
        self.master.resizable(True, True)

        # Usuário
        self.label_username = Label(master, text="Usuário:")
        self.label_username.pack(pady=(20, 5))
        self.entry_username = Entry(master)
        self.entry_username.pack()

        # Senha
        self.label_password = Label(master, text="Senha:")
        self.label_password.pack(pady=(10, 5))
        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        # Botão de login
        self.button_login = Button(master, text="Entrar", command=self.login)
        self.button_login.pack(pady=20)

        # Botão de cadastro
        self.button_register = Button(
            master, text="Cadastrar", command=lambda: self.open_window(Register)
        )
        self.button_register.pack(pady=20)

    def login(self):
        try:
            data = LoginDTO(
                username=self.entry_username.get(), password=self.entry_password.get()
            )

            service = AuthService()
            service.login(data.username, data.password)
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo {data.username}!")
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
                    messagebox.showerror("Login falhou", f"{message}")
