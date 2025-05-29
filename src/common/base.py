from tkinter import Tk


class TkinterBase:
    def __init__(self, master: Tk) -> None:
        self.master = master

    def open_window(self, window=None, destroy=False, **kwargs) -> None:
        if not destroy:
            self.master.destroy()
        new_window = Tk()
        if kwargs:
            window(new_window, **kwargs)
            return
        window(new_window)
        return
