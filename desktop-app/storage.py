import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DB_FILE = DATA_DIR / "clientes.db"


class CPFDuplicadoError(Exception):
    pass


def _normalize_cpf(cpf: str) -> str:
    return "".join(c for c in cpf if c.isdigit())


def _get_connection() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL
            )
            """
        )


def cpf_existe(cpf: str) -> bool:
    cpf_norm = _normalize_cpf(cpf)
    with _get_connection() as conn:
        row = conn.execute(
            "SELECT 1 FROM clientes WHERE cpf = ?",
            (cpf_norm,),
        ).fetchone()
    return row is not None


def save_client(client: dict) -> None:
    cpf_norm = _normalize_cpf(client["cpf"])
    if not cpf_norm:
        raise ValueError("CPF inválido.")

    if cpf_existe(cpf_norm):
        raise CPFDuplicadoError()

    with _get_connection() as conn:
        try:
            conn.execute(
                """
                INSERT INTO clientes (nome, cpf, email, telefone, endereco)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    client["nome"],
                    cpf_norm,
                    client["email"],
                    client["telefone"],
                    client["endereco"],
                ),
            )
        except sqlite3.IntegrityError:
            raise CPFDuplicadoError() from None


init_db()
