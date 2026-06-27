import openpyxl

# Carrega um arquivo Excel e retorna o workbook
def load_excel_file(file_path):
    return openpyxl.load_workbook(file_path)

# Salva um workbook em um arquivo Excel
def save_excel_file(workbook, file_path):
    workbook.save(file_path)

# Obtém os dados da planilha ativa
def get_active_sheet_data(workbook, row):
    sheet = workbook.active
    nome = sheet[f'A{row}'].value
    cpf = sheet[f'B{row}'].value
    email = sheet[f'C{row}'].value
    telefone = sheet[f'D{row}'].value

    return {
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'telefone': telefone,
    }