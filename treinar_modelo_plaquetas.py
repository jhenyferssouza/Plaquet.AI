from ultralytics import YOLO
import os
import torch
import yaml

# Imprimir o conteúdo do arquivo YAML
yaml_path = 'D:/modeloIA_Plaquet.AI/src/plaquetasYOLO.yaml'
with open(yaml_path, 'r') as file:
    yaml_content = yaml.safe_load(file)
    print("Conteúdo do arquivo YAML:")
    print(yaml.dump(yaml_content, default_flow_style=False))

# Configurar o caminho para o arquivo YAML
caminho_yaml = 'D:/modeloIA_Plaquet.AI/src/plaquetasYOLO.yaml'

# Inicializar o modelo
modelo = YOLO('yolov8n.pt')  # Usando o modelo nano pré-treinado do YOLOv8

# Configurações altamente otimizadas para treinamento
config_treinamento = {
    'data': 'D:/modeloIA_Plaquet.AI/src/plaquetasYOLO.yaml',
    'epochs': 30,
    'imgsz': 320,
    'batch': 16,
    'device': 'cpu',
    'workers': 8,
    'verbose': True,
    'patience': 50,
    'rect': False,  # Remova esta opção ou defina como False
}

# Treinar o modelo
resultados = modelo.train(**config_treinamento)

# Salvar o modelo treinado
modelo.save('modelo_plaquetas_ultra_otimizado.pt')

print("Treinamento concluído. Modelo salvo como 'modelo_plaquetas_ultra_otimizado.pt'")