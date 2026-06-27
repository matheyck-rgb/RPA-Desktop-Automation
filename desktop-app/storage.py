import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
CLIENTS_FILE = DATA_DIR / "clientes.json"


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_clients() -> list[dict]:
    _ensure_data_dir()
    if not CLIENTS_FILE.exists():
        return []
    with CLIENTS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_client(client: dict) -> None:
    _ensure_data_dir()
    clients = load_clients()
    clients.append(client)
    with CLIENTS_FILE.open("w", encoding="utf-8") as f:
        json.dump(clients, f, ensure_ascii=False, indent=2)
