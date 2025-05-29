from tkinter import Label, Tk, Button
from src.common.base import TkinterBase
from src.services.user_service import UserService
class Report(TkinterBase):
    def __init__(self, master: Tk) -> None:
        self.master = master

        self.master = master
        self.master.title("Relatório")
        self.master.geometry("900x400")
        self.master.resizable(True, True)
        self.master.configure(bg="#2C3E50")

        button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold")}
        

        self.rows = []

        self.render_header()
        self.render_data()

        self.button = Button(self.master, text="Voltar", command=self.list_activie, **button_style)
        self.button.grid()

    def list_activie(self):
        from src.front.activies import ListActivies
        return self.open_window(ListActivies)

    def render_header(self) -> None:
        headers = [
            "ID", 
            "Nome de usuário", 
            "email"
        ]

        for col, text in enumerate(headers):
            Label(self.master, text=text, font=("Arial", 10, "bold"), bg="#2C3E50", fg="white").grid(row=1, column=col, padx=5, pady=5)

        
    def render_data(self) -> None:
        service = UserService()
        data = service.get_all_user()
        print(data)
        if not data:
            return
        

        for idx, item in enumerate(data):
            self.add_row(item, idx + 2)
        
        
        
    def add_row(self, item:dict, row_idx: int) -> None:
        labels = []
        values = [
            item["user_id"],
            item["username"],
            item["email"]
        ]

        for col, val in enumerate(values):
            lbl = Label(self.master, text=val, bg="#2C3E50", fg="white", font=("Arial", 10))
            lbl.grid(row=row_idx, column=col, padx=5, pady=5)
            labels.append(lbl)

        self.rows.append((labels))