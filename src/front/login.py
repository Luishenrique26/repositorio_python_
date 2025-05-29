from tkinter import Button, Entry, Label, Tk, messagebox
from pydantic import ValidationError
from src.domain.dtos import LoginDTO
from src.services import AuthService
from .activies import ListActivies
from .register import Register
from src.common.base import TkinterBase

class Login(TkinterBase):
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("350x250")
        self.master.resizable(True, True)
        self.master.configure(bg="#2C3E50")  # Cor de fundo moderna

        label_style = {"bg": "#2C3E50", "fg": "white", "font": ("Arial", 12)}
        entry_style = {"bg": "#ECF0F1", "font": ("Arial", 12)}
        button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold")}

        # Usuário
        self.label_username = Label(master, text="Usuário:", **label_style)
        self.label_username.pack(pady=5)
        self.entry_username = Entry(master, **entry_style)
        self.entry_username.pack(pady=5)

        # Senha
        self.label_password = Label(master, text="Senha:", **label_style)
        self.label_password.pack(pady=5)
        self.entry_password = Entry(master, show="*", **entry_style)
        self.entry_password.pack(pady=5)

        # Botões
        self.button_login = Button(master, text="Entrar", command=self.login, **button_style)
        self.button_login.pack(pady=10)

        self.button_register = Button(master, text="Cadastrar", command=lambda: self.open_window(Register), **button_style)
        self.button_register.pack(pady=10)

    def login(self) -> None:
        try:
            data = LoginDTO(username=self.entry_username.get(), password=self.entry_password.get())
            service = AuthService()
            service.login(data.username, data.password)
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo {data.username}!")
            self.master.destroy()
            self.open_window(ListActivies, destroy=True)
        except (ValidationError, ValueError) as e:
            if isinstance(e, ValueError):
                messagebox.showerror("Erro", f"{e}")
            else:
                dict_errors = {f"{error['loc'][0]}_message": error["msg"].replace("Value error, ", "") for error in e.errors()}
                for message in dict_errors.values():
                    messagebox.showerror("Login falhou", f"{message}")

