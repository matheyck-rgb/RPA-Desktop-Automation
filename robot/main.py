from scripts.planilha.utils import (
    load_excel_file, 
    get_active_sheet_data,
)

def main():
    workbook = load_excel_file('assets/clientes.xlsx')
    row = 2  # Começa na segunda linha
    while True:
        data = get_active_sheet_data(workbook, row)
        nome = data['nome']
        cpf = data['cpf']
        email = data['email']
        telefone = data['telefone']
        
        if not all([nome, cpf, email, telefone]):
            break

        print(f"Nome: {nome}, CPF: {cpf}, Email: {email}, Telefone: {telefone}, Linha: {row}")
        row += 1

if __name__ == "__main__":
    main()