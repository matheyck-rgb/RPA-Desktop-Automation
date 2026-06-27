import tkinter as tk
from tkinter import messagebox

from storage import CPFDuplicadoError, save_client


class CadastroClienteScreen(tk.Frame):
    def __init__(self, parent, on_voltar):
        super().__init__(parent, bg="#f0f0f0")
        self.on_voltar = on_voltar

        header = tk.Frame(self, bg="#f0f0f0")
        header.pack(fill="x", padx=20, pady=(20, 10))

        tk.Button(header, text="Voltar", command=self.on_voltar).pack(side="left")

        tk.Label(
            self,
            text="Cadastro de Clientes",
            font=("Segoe UI", 18, "bold"),
            bg="#f0f0f0",
        ).pack(pady=(10, 20))

        form = tk.Frame(self, bg="#f0f0f0")
        form.pack(padx=40)

        fields = [
            ("Nome", "entry_nome"),
            ("CPF", "entry_cpf"),
            ("Email", "entry_email"),
            ("Telefone", "entry_telefone"),
            ("Endereço", "entry_endereco"),
        ]

        for row, (label, attr) in enumerate(fields):
            tk.Label(form, text=f"{label}:", bg="#f0f0f0", anchor="w", width=12).grid(
                row=row, column=0, sticky="ew", pady=6
            )
            entry = tk.Entry(form, width=35)
            entry.grid(row=row, column=1, pady=6)
            setattr(self, attr, entry)

        tk.Button(
            self,
            text="Salvar",
            width=15,
            command=self._salvar,
        ).pack(pady=25)

    def _salvar(self) -> None:
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()

        if not all([nome, cpf, email, telefone, endereco]):
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            save_client(
                {
                    "nome": nome,
                    "cpf": cpf,
                    "email": email,
                    "telefone": telefone,
                    "endereco": endereco,
                }
            )
        except CPFDuplicadoError:
            messagebox.showerror("Erro", "CPF já cadastrado.")
            return

        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        self._limpar_campos()

    def _limpar_campos(self) -> None:
        for entry in (
            self.entry_nome,
            self.entry_cpf,
            self.entry_email,
            self.entry_telefone,
            self.entry_endereco,
        ):
            entry.delete(0, tk.END)
