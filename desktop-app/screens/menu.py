import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, parent, on_cadastro, on_logout):
        super().__init__(parent, bg="#f0f0f0")
        self.on_cadastro = on_cadastro
        self.on_logout = on_logout

        tk.Label(
            self,
            text="Menu Principal",
            font=("Segoe UI", 18, "bold"),
            bg="#f0f0f0",
        ).pack(pady=(40, 30))

        buttons = tk.Frame(self, bg="#f0f0f0")
        buttons.pack()

        tk.Button(
            buttons,
            text="Cadastro de Clientes",
            width=25,
            command=self.on_cadastro,
        ).pack(pady=8)

        tk.Button(
            buttons,
            text="Sair",
            width=25,
            command=self.on_logout,
        ).pack(pady=8)
