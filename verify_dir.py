import os

base_dir = 'D:/modeloIA_Plaquet.AI/src'
output_dir = os.path.join(base_dir, 'output_yolo')

def check_directory(path):
    if os.path.exists(path):
        print(f"O diretório {path} existe.")
        files = os.listdir(path)
        print(f"Contém {len(files)} arquivos/pastas.")
        if len(files) > 0:
            print(f"Primeiros 5 itens: {files[:5]}")
    else:
        print(f"O diretório {path} não existe!")

print("Verificando estrutura de diretórios:")
check_directory(os.path.join(output_dir, 'train'))
check_directory(os.path.join(output_dir, 'val'))

yaml_path = os.path.join(base_dir, 'plaquetasYOLO.yaml')
if os.path.exists(yaml_path):
    print(f"O arquivo YAML existe em {yaml_path}")
else:
    print(f"O arquivo YAML não foi encontrado em {yaml_path}")
