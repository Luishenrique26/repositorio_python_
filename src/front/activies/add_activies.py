from tkinter import Tk, Label, Button, messagebox, Entry
from pydantic import ValidationError
from src.domain.dtos import ActiviesDTO
from src.services import ActiviesService
from src.common.base import TkinterBase

class AddActivitie(TkinterBase):
    def __init__(self, master: Tk) -> None:
        from .list_activies import ListActivies
        


        self.master = master

        self.master.title("Adicionar atividade ao projeto social")
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

        self.label_description = Label(self.master, text="Descrição da Atividade:", **label_style)
        self.label_description.grid(row=1, column=0, padx=5, pady=5)

        self.entry_description = Entry(self.master, **entry_style)
        self.entry_description.grid(row=1, column=1, padx=5, pady=5)

        self.label_start_date = Label(self.master, text="Data de inicio:", **label_style)
        self.label_start_date.grid(row=2, column=0, padx=5, pady=5)

        self.entry_start_date = Entry(self.master, **entry_style)
        self.entry_start_date.grid(row=2, column=1, padx=5, pady=5)

        self.label_end_date = Label(self.master, text="Data de fim:", **label_style)
        self.label_end_date.grid(row=3, column=0, padx=5, pady=5)

        self.entry_end_date = Entry(self.master, **entry_style)
        self.entry_end_date.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = Button(self.master, text="Adicionar", command=self.add_activitie, **button_style)
        self.button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.button_can = Button(self.master, text="Cancelar", command=lambda: self.open_window(ListActivies), **button_style)
        self.button_can.grid()

    def add_activitie(self) -> None:
        from .list_activies import ListActivies
        
        name = self.entry_name.get()
        start_date = self.entry_start_date.get()
        end_date = self.entry_end_date.get()
        description = self.entry_description.get()

        try:
            dto = ActiviesDTO(name=name, start_date=start_date, end_date=end_date, description=description)

            service = ActiviesService()
            service.create_activie(dto)
            messagebox.showinfo("Cadastro bem-sucedido", "Atividade cadastrada com sucesso!")
            self.master.destroy()
            self.open_window(ListActivies, destroy=True)
        except (ValidationError, ValueError) as e:
            if type(e) == ValueError:
                messagebox.showerror("Erro", f"{e}")
            else:
                dict = {
                    f"{error['loc'][0]}_message": error["msg"].replace("Value error, ", "")
                    for error in e.errors()
                }
                for message in dict.values():
                    messagebox.showerror("Cadastro falhou", f"{message}")