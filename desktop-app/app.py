import tkinter as tk

from screens.cadastro_cliente import CadastroClienteScreen
from screens.login import LoginScreen
from screens.menu import MenuScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RPA Desktop - Sistema de Clientes")
        self.geometry("480x400")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames: dict[str, tk.Frame] = {}
        for Screen, name in (
            (LoginScreen, "login"),
            (MenuScreen, "menu"),
            (CadastroClienteScreen, "cadastro"),
        ):
            frame = Screen(container, **self._screen_kwargs(name))
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")

    def _screen_kwargs(self, name: str) -> dict:
        if name == "login":
            return {"on_login_success": lambda: self.show_frame("menu")}
        if name == "menu":
            return {
                "on_cadastro": lambda: self.show_frame("cadastro"),
                "on_logout": lambda: self.show_frame("login"),
            }
        if name == "cadastro":
            return {"on_voltar": lambda: self.show_frame("menu")}
        return {}

    def show_frame(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()
