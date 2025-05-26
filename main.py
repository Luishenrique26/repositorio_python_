from database.migrations import run_migrations
from src.front.login import Login
from tkinter import Tk


def main():
    run_migrations()
    root = Tk()
    Login(root)
    root.mainloop()


if __name__ == "__main__":
    main()
