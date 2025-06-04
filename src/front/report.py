from tkinter import Label, Tk, Button
from src.common.base import TkinterBase
from src.services.user_service import UserService
from src.services import ActivitiesService
from src.common.utils import date_to_str, datetime_to_str
import logging

log = logging.getLogger(__name__)

class Report(TkinterBase):
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.master.title("Relatório")
        self.master.geometry("900x400")
        self.master.resizable(True, True)
        self.master.configure(bg="#2C3E50")

        button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold")}

        self.rows = []

        # Botão voltar
        self.button_voltar = Button(self.master, text="Voltar", command=self.list_activitie, **button_style)
        self.button_voltar.grid(row=0, column=0, padx=5, pady=5)

        # Renderiza usuários e atividades
        self.render_users()
        self.render_activities()

    def list_activitie(self):
        from src.front.activities import ListActivities
        return self.open_window(ListActivities)

    def render_users(self) -> None:
        headers = ["ID", "Nome de usuário", "email"]
        for col, text in enumerate(headers):
            Label(self.master, text=text, font=("Arial", 10, "bold"), bg="#2C3E50", fg="white").grid(row=1, column=col, padx=5, pady=5)

        service = UserService()
        data = service.get_all_user()
        log.info(data)
        if not data:
            return

        for idx, item in enumerate(data):
            values = [item["user_id"], item["username"], item["email"]]
            for col, val in enumerate(values):
                Label(self.master, text=val, bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=idx + 2, column=col, padx=5, pady=5)

        # Salva a próxima linha para atividades começarem abaixo
        self.next_row = len(data) + 4

    def render_activities(self) -> None:
        headers = ["ID", "Nome", "Descrição", "Início", "Fim", "Criado em", "Atualizado em"]
        for col, text in enumerate(headers):
            Label(self.master, text=text, font=("Arial", 10, "bold"), bg="#2C3E50", fg="white").grid(row=self.next_row, column=col, padx=5, pady=5)

        service = ActivitiesService()
        data = service.get_activities()
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
        log.info(data)

        for idx, item in enumerate(data):
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
                Label(self.master, text=val, bg="#2C3E50", fg="white", font=("Arial", 10)).grid(row=self.next_row + idx + 1, column=col, padx=5, pady=5)
