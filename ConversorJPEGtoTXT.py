import os
from pathlib import Path

# Usa o diretório atual
label_dir = Path.cwd() / 'D:\modeloIA_Plaquet.AI\src\Imagens_dataset\output_yolo'

print(f"Buscando arquivos em: {label_dir}")

arquivos_processados = 0
arquivos_ignorados = 0

try:
    # Lista todos os arquivos no diretório
    todos_arquivos = list(label_dir.glob("*"))
    print(f"Total de arquivos encontrados: {len(todos_arquivos)}")
    print("Arquivos encontrados:")
    for arquivo in todos_arquivos:
        print(f"  - {arquivo.name}")

    # Processa os arquivos .jpeg.txt
    for label_file in label_dir.glob("*.jpeg.txt"):
        new_name = label_file.stem.replace('.jpeg', '') + '.txt'
        new_path = label_file.with_name(new_name)
        
        if not new_path.exists():
            os.rename(str(label_file), str(new_path))
            print(f"Renomeado: {label_file.name} para {new_name}")
            arquivos_processados += 1
        else:
            print(f"Arquivo já existe: {new_name}")
            arquivos_ignorados += 1

except Exception as e:
    print(f"Erro ao processar arquivos: {e}")

print(f"Processo concluído. Arquivos renomeados: {arquivos_processados}, Ignorados: {arquivos_ignorados}")

if arquivos_processados == 0:
    print("Nenhum arquivo foi renomeado. Verifique se existem arquivos .jpeg.txt no diretório especificado.")
