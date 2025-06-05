from tkinter import Tk, Label, Button, messagebox, Entry
from src.domain.dtos import UpdateActivitieDTO
from src.services import ActivitiesService
from src.common.base import TkinterBase

from pydantic import ValidationError



class UpdateActivitie(TkinterBase):
    def __init__(self, master: Tk, **kwargs) -> None:
        #Foi importado aqui por causa de erro de importação circular.
        from .list_activities import ListActivities



        self.master = master
        self.item = kwargs["item"]
        self.master.title("Atualizar atividade")
        self.master.geometry("900x400")
        self.master.resizable(True, True)
        self.master.configure(bg="#2C3E50")

        label_style = {"bg": "#2C3E50", "fg": "white", "font": ("Arial", 12)}
        entry_style = {"bg": "#ECF0F1", "font": ("Arial", 12)}
        button_style = {"bg": "#3498DB", "fg": "white", "font": ("Arial", 12, "bold")}

        self.label_name = Label(self.master, text="Nome da Atividade:", **label_style)
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = Entry(self.master, **entry_style)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_name.insert(0, self.item["name"])

        self.label_description = Label(self.master, text="Descrição da Atividade:", **label_style)
        self.label_description.grid(row=1, column=0, padx=5, pady=5)

        self.entry_description = Entry(self.master, **entry_style)
        self.entry_description.grid(row=1, column=1, padx=5, pady=5)
        self.entry_description.insert(0, self.item.get("description", ""))

        self.label_start_date = Label(self.master, text="Data de inicio:", **label_style)
        self.label_start_date.grid(row=2, column=0, padx=5, pady=5)

        self.entry_start_date = Entry(self.master, **entry_style)
        self.entry_start_date.grid(row=2, column=1, padx=5, pady=5)
        self.entry_start_date.insert(0, self.item["start_date"])

        self.label_end_date = Label(self.master, text="Data de fim:", **label_style)
        self.label_end_date.grid(row=3, column=0, padx=5, pady=5)

        self.entry_end_date = Entry(self.master, **entry_style)
        self.entry_end_date.grid(row=3, column=1, padx=5, pady=5)
        self.entry_end_date.insert(0, self.item["end_date"])

        self.button_add = Button(self.master, text="Atualizar", command=self.update_activitie, **button_style)
        self.button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.button_can = Button(self.master, text="Cancelar", command=lambda: self.open_window(ListActivities), **button_style)
        self.button_can.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    def update_activitie(self) -> None:
        from .list_activities import ListActivities
        
        try:
            data = UpdateActivitieDTO(
                activitie_id=self.item["activitie_id"],
                name=self.entry_name.get(),
                description=self.entry_description.get(),
                start_date=self.entry_start_date.get(),
                end_date=self.entry_end_date.get(),
                created_at=self.item["created_at"],
            )
            service = ActivitiesService()
            service.update_activitie(data, data.activitie_id)
            messagebox.showinfo("Sucesso", "Atividade atualizada com sucesso!")
            self.master.destroy()
            self.open_window(ListActivities, destroy=True)
        except (ValidationError, ValueError) as e:
            if type(e) == ValueError:
                messagebox.showerror("Erro", f"{e}")
            else:
                dict = {
                    f"{error['loc'][0]}_message": error["msg"].replace("Value error, ", "")
                    for error in e.errors()
                }
                for message in dict.values():
                    messagebox.showerror("Erro", f"{message}")