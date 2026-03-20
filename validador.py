import os
import csv
from dotenv import load_dotenv
from config.data_types import DATA_TYPES

load_dotenv()

raw_file_name = os.getenv("RAW_FILE_NAME")
processed_file_name = os.getenv("PROCESSED_FILE_NAME")

# Lista de arquivos para validar
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

arquivos = [
    os.path.join('data_types', data_type, 'data', file_name)
    for data_type in DATA_TYPES
    for file_name in (raw_file_name, processed_file_name)
]

# Cabeçalho esperado
cabecalho_esperado = ["date", "description", "death_date"]

for caminho in arquivos:
    print(caminho)
    pasta = os.path.dirname(caminho)
    print(pasta)
    caminho_erros = os.path.join(pasta, "erros.csv")

    erros = []

    with open(caminho, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Verifica cabeçalho
        try:
            cabecalho = next(reader)
        except StopIteration:
            print(f"Arquivo vazio: {caminho}")
            continue

        if cabecalho != cabecalho_esperado:
            print(f"Cabeçalho incorreto em {caminho}")
            continue

        # Validação das linhas
        for numero_linha, linha in enumerate(reader, start=2):  # começa no 2 por causa do cabeçalho
            if len(linha) != 3:
                erros.append([numero_linha] + linha)

    # Se houver erros, cria/escreve erros.csv
    if erros:
        with open(caminho_erros, "w", newline='', encoding='utf-8') as errofile:
            writer = csv.writer(errofile)
            writer.writerow(["numero_linha", "dados"])
            for erro in erros:
                writer.writerow(erro)

        print(f"Foram encontrados erros em {caminho}. Verifique {caminho_erros}")
    else:
        print(f"{caminho} validado com sucesso.")