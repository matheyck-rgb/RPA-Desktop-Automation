import tkinter as tk
from tkinter import messagebox

VALID_USER = "admin"
VALID_PASSWORD = "1234"


class LoginScreen(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, bg="#f0f0f0")
        self.on_login_success = on_login_success

        tk.Label(
            self,
            text="Login",
            font=("Segoe UI", 18, "bold"),
            bg="#f0f0f0",
        ).pack(pady=(40, 20))

        form = tk.Frame(self, bg="#f0f0f0")
        form.pack(padx=40)

        tk.Label(form, text="Usuário:", bg="#f0f0f0", anchor="w").grid(
            row=0, column=0, sticky="ew", pady=5
        )
        self.entry_user = tk.Entry(form, width=30)
        self.entry_user.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Senha:", bg="#f0f0f0", anchor="w").grid(
            row=1, column=0, sticky="ew", pady=5
        )
        self.entry_password = tk.Entry(form, width=30, show="*")
        self.entry_password.grid(row=1, column=1, pady=5)

        tk.Button(
            self,
            text="Entrar",
            width=15,
            command=self._login,
        ).pack(pady=20)

        self.entry_password.bind("<Return>", lambda _: self._login())

    def _login(self) -> None:
        user = self.entry_user.get().strip()
        password = self.entry_password.get().strip()

        if user == VALID_USER and password == VALID_PASSWORD:
            self.on_login_success()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
