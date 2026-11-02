# Plaquet.AI - Detecção e Contagem Automática de Plaquetas

> Sistema de Visão Computacional baseado em YOLO para detecção, segmentação e contagem automática de plaquetas em imagens de esfregaço sanguíneo.

## Visão Geral

O **Plaquet.AI** é uma solução tecnológica voltada para o diagnóstico hematológico pediátrico, com foco no suporte a crianças com leucemia. Em cenários em que o tempo é um fator determinante para a tomada de decisão médica, o projeto visa proporcionar rapidez e exatidão no processo analítico.

Anualmente, cerca de 280 mil crianças são diagnosticadas com cancro no mundo (dados GLOBOCAN 2020 / OMS). A leucemia altera significativamente a composição sanguínea, exigindo a contagem rigorosa de componentes como hemácias, leucócitos e plaquetas. Em regiões ou laboratórios com recursos limitados ou áreas remotas, o acesso a equipamentos de grande porte e de alto custo torna-se um desafio operacional.


Para contornar a margem de erro humano e os atrasos na contagem manual ou no envio de amostras, o Plaquet.AI emprega inteligência artificial para realizar a identificação e a contagem de plaquetas diretamente a partir de imagens de amostras sanguíneas. Esta automação reduz o tempo de resposta e apoia a conduta médica em tratamentos imediatos.

### Diferencial Tecnológico e Financeiro

Enquanto os contadores hematológicos tradicionais de grande porte exigem um investimento inicial elevado (com custos na ordem dos R$ 55.000,00), a proposta do Plaquet.AI baseia-se num modelo acessível. Esta abordagem democratiza o acesso ao diagnóstico preciso em contextos laboratoriais variados.

<img width="1049" height="718" alt="image" src="https://github.com/user-attachments/assets/f124f216-f16a-4c73-ab8f-9f18f392b3f8" />

## Funcionalidades

* **Detecção Automática:** Localização e contagem precisa de plaquetas via modelos YOLO otimizados.
* **Pipeline de Conversão de Dados:** Scripts utilitários para conversão de anotações (JSON/JPEG para formato YOLO).
* **Treinamento Customizado:** Scripts prontos para re-treinamento e validação de datasets.
* **Modelo Pré-treinado Otimizado:** Pesos pré-treinados (`modelo_plaquetas_ultra_otimizado.pt`) prontos para inferência imediata.

##  Estrutura do Repositório

```text
Plaquet.AI/
├── src/                                 
├── modelo_plaquetas_ultra_otimizado.pt  # Pesos do modelo treinado e otimizado
├── MainIA.py                            # Execução principal / Pipeline de inferência da IA
├── plaquetasYOLO.yaml                   # Arquivo de configuração das classes e caminhos do YOLO
├── treinar_modelo_plaquetas.py          # Script de treinamento do modelo
├── ConversorJSONtoYOLO.py               # Utilitário para conversão de anotações JSON -> YOLO
├── ConversorJPEGtoTXT.py                # Utilitário para conversão/formatação de rótulos
├── find_labels.py                       # Verificação e mapeamento de labels no dataset
└── README.md                            
```

> **Nota:** Pastas de datasets (`Amostras_dataset/`, `output_yolo/`) e históricos de treino (`runs/`) foram omitidos do repositório remoto para otimização de espaço.

## Como Executar

### 1. Pré-requisitos

* Python 3.10 ou superior
* Git

### 2. Instalação

Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/seu-usuario/plaquet-ai.git
cd plaquet-ai
```

Crie e ative um ambiente virtual:

```bash
# Windows (PowerShell)
python -m venv env
.\env\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv env
source env/bin/activate
```

Instale as dependências:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*(Caso não possua o `requirements.txt` gerado, instale as bibliotecas principais)*:
```bash
pip install ultralytics opencv-python pillow numpy matplotlib
```

### 3. Inferência (Executando a IA)

Para rodar a detecção utilizando o modelo otimizado pré-treinado:

```bash
python MainIA.py
```

### 4. Treinamento do Modelo

Caso queira treinar o modelo com seu próprio dataset:

1. Certifique-se de configurar o arquivo `plaquetasYOLO.yaml` com os caminhos corretos das imagens.
2. Execute o script de treinamento:

```bash
python treinar_modelo_plaquetas.py
```

## Ferramentas e Conversões

O repositório inclui scripts utilitários para preparação e inspeção dos dados:

* **`ConversorJSONtoYOLO.py`**: Converte anotações no formato JSON (ex.: LabelMe / VIA) para o formato padrão `.txt` do YOLO.
* **`find_labels.py` & `verify_dir.py`**: Ajudam a inspecionar a integridade das pastas de imagens e rotulagem antes do treino.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Visão Computacional & AI:** Ultralytics YOLO (YOLOv8 / YOLOv5), OpenCV, PyTorch
* **Manipulação de Dados & Imagens:** NumPy, Pillow, Matplotlib

## Isenção de Responsabilidade (Medical Disclaimer)

> **Importante:** Esta aplicação é um projeto acadêmico/experimental de apoio tecnológico e **não substitui** a avaliação e laudo de um profissional patologista ou hematologista habilitado.
