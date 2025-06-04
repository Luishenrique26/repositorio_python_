from tkinter import Tk, Label, Button, messagebox
from src.common.utils import date_to_str, datetime_to_str
from src.services import ActiviesService
from src.common.base import TkinterBase
from .update_activies import UpdateActivitie

class ListActivies(TkinterBase):
    def __init__(self, master: Tk) -> None:
        from .add_activies import AddActivitie

        self.master = master
        self.master.title("Lista de atividades do Projeto social")
        self.master.geometry("900x400")
        self.master.resizable(True, True)
        self.master.configure(bg="#2C3E50")

        self.rows = []

        button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold")}

        self.btn_add = Button(self.master, text="Adicionar", command=lambda: self.open_window(AddActivitie), **button_style)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_add = Button(self.master, text="Logout", command=self.logout, **button_style)
        self.btn_add.grid(row=0, column=1, padx=5, pady=5)

        self.btn_add = Button(self.master, text="Relatório", command=self.report, **button_style)
        self.btn_add.grid(row=0, column=2, padx=5, pady=5)

        self.render_header()
        self.render_data()

    def logout(self) -> None:
        from src.front.login import Login
        return self.open_window(Login)

    def report(self):
        from src.front.report import Report
        return self.open_window(Report)
    
    def render_header(self) -> None:
        headers = ["ID", "Nome", "Descrição", "Início", "Fim", "Criado em", "Atualizado em", "", ""]
        for col, text in enumerate(headers):
            Label(self.master, text=text, font=("Arial", 10, "bold"), bg="#2C3E50", fg="white").grid(row=1, column=col, padx=5, pady=5)

    def render_data(self) -> None:
        service = ActiviesService()
        data = service.get_activies()
        if not data:
            return
        data = [
            {
                key: date_to_str(value, "%d/%m/%Y")
                if key in ["start_date", "end_date"]
                else datetime_to_str(value, "%d/%m/%Y - %H:%M:%S")
                if key in ["created_at", "updated_at"]
                else value
                for key, value in x.items()
            }
            for x in data
        ]

        # 👉 Linha única de log adicionada
        import logging; logging.getLogger(__name__).info(data)

        for idx, item in enumerate(data):
            self.add_row(item, idx + 2)

    def add_row(self, item:dict, row_idx: int) -> None:
        labels = []
        values = [
            item["activitie_id"],
            item["name"],
            item["description"],
            item["start_date"],
            item["end_date"],
            item["created_at"],
            item["updated_at"],
        ]

        for col, val in enumerate(values):
            lbl = Label(self.master, text=val, bg="#2C3E50", fg="white", font=("Arial", 10))
            lbl.grid(row=row_idx, column=col, padx=5, pady=5)
            labels.append(lbl)

        btn_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 10, "bold")}

        btn_update = Button(self.master, text="Update", command=lambda i=item: self.update_item(i), **btn_style)
        btn_update.grid(row=row_idx, column=7, padx=5)

        btn_delete = Button(self.master, text="Delete", command=lambda r=row_idx: self.delete_row(r), **btn_style)
        btn_delete.grid(row=row_idx, column=8, padx=5)

        self.rows.append((labels, btn_update, btn_delete))

    def update_item(self, item:dict) -> None:
        self.open_window(UpdateActivitie, False, item=item)
        print(f"Atualizar item: {item['activitie_id']}")

    def delete_row(self, row_idx: int) -> None:
        row = self.rows[row_idx - 2]  # -2 porque agora cabeçalho ocupa linha 1

        keys = [
            "activitie_id",
            "name",
            "description",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
        values = {k: lbl.cget("text") for k, lbl in dict(zip(keys, row[0])).items()}

        print(f"rows: {values}")

        response = messagebox.askyesno("Confirmar exclusão", f"Tem certeza que deseja excluir o item {row[0][0].cget('text')}?")
        if response is False:
            return

        for widget in row[0]:
            service = ActiviesService()
            service.delete_activie(values["activitie_id"])
            widget.destroy()

        row[1].destroy()
        row[2].destroy()
        self.rows[row_idx - 2] = None
        messagebox.showinfo("Deletado com sucesso!", "Atividade deletada com sucesso!")
