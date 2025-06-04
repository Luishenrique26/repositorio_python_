from database.migrations import run_migrations
from src.front.login import Login
from tkinter import Tk
import logging


def main():
    logging.basicConfig(
filename='relatorio.log', filemode='a', 
level=logging.DEBUG, 
format='%(asctime)s - %(levelname)s - %(message)s'
)
    run_migrations()
    root = Tk()
    Login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
