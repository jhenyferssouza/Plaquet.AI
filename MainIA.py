import tkinter as tk
from tkinter import ttk, filedialog, font
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import os
import numpy as np

caminho_modelo = r'D:\modeloIA_Plaquet.AI\runs\detect\train6\weights\best.pt'
if not os.path.exists(caminho_modelo):
    raise FileNotFoundError(f"Arquivo do modelo não encontrado: {caminho_modelo}")
modelo = YOLO(caminho_modelo)

def detectar_plaquetas_yolo(imagem_path):
    if not os.path.isfile(imagem_path):
        raise FileNotFoundError(f"Arquivo de imagem não encontrado: {imagem_path}")
    
    imagem = cv2.imread(imagem_path)
    if imagem is None:
        raise ValueError(f"Não foi possível ler a imagem: {imagem_path}")
    
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    resultados = modelo(imagem_rgb)
    deteccoes = resultados[0].boxes.data
    
    plaquetas_detectadas = []
    for deteccao in deteccoes:
        x1, y1, x2, y2, confianca, classe = deteccao
        if int(classe) == 0:
            plaquetas_detectadas.append((float(x1), float(y1), float(x2-x1), float(y2-y1), float(confianca)))
    
    return imagem_rgb, plaquetas_detectadas

def processar_imagem():
    caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens JPEG", "*.jpeg")])
    if not caminho_imagem:
        return

    try:
        tempo_inicio = time.time()
        imagem_rgb, plaquetas_detectadas = detectar_plaquetas_yolo(caminho_imagem)
        tempo_processamento = time.time() - tempo_inicio

        # Acurácia
        if plaquetas_detectadas:
            acuracia_media = sum(conf for _, _, _, _, conf in plaquetas_detectadas) / len(plaquetas_detectadas)
        else:
            acuracia_media = 0

        
        num_plaquetas_detectadas = len(plaquetas_detectadas)
        info_text.set(f"Plaquetas detectadas: {num_plaquetas_detectadas}\n"
                      f"Tempo de processamento: {tempo_processamento:.2f} segundos\n"
                      f"Acurácia média: {acuracia_media:.2%}")

        # Gráfico: Infos
        ax_imagem.clear()
        ax_imagem.imshow(imagem_rgb)
        for (x, y, w, h, _) in plaquetas_detectadas:
            rect = plt.Rectangle((x, y), w, h, fill=False, edgecolor='#FF00FF', linewidth=1)
            ax_imagem.add_patch(rect)
        ax_imagem.axis('off')
        ax_imagem.set_title("Detecções", color='white', fontsize=12)

        # Gráfico: histograma
        ax_hist.clear()
        tamanhos = [w * h for _, _, w, h, _ in plaquetas_detectadas]
        ax_hist.hist(tamanhos, bins=20, edgecolor='white', color='#9370DB')  # Medium Purple
        ax_hist.set_title("Distribuição de Tamanhos", color='white', fontsize=12)
        ax_hist.set_xlabel("Área (pixels²)", color='white', fontsize=10)
        ax_hist.set_ylabel("Frequência", color='white', fontsize=10)

        # Gráfico de dispersão de confiança x tamanho
        ax_scatter.clear()
        confiancas = [conf for _, _, _, _, conf in plaquetas_detectadas]
        ax_scatter.scatter(tamanhos, confiancas, color='#BA55D3', s=30)  
        ax_scatter.set_title("Confiança x Tamanho", color='white', fontsize=12)
        ax_scatter.set_xlabel("Área (pixels²)", color='white', fontsize=10)
        ax_scatter.set_ylabel("Confiança", color='white', fontsize=10)

        ajustar_layout()
        canvas.draw()

    except Exception as e:
        info_text.set(f"Erro: {str(e)}")

# Tkinter p/ interface de usaurio
root = tk.Tk()
root.title("Detector de Plaquetas - Plaquet.AI")
root.geometry("1200x800")
root.configure(bg='#4B0082')  
title_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

style = ttk.Style(root)
style.theme_use('clam')
style.configure('TFrame', background='#4B0082')
style.configure('TButton', background='#8A2BE2', foreground='white', font=button_font)
style.configure('TLabel', background='#4B0082', foreground='white', font=label_font)

# Frame principal
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="Detector de Plaquetas - Plaquet.AI", font=title_font)
title_label.pack(pady=10)

btn_selecionar = ttk.Button(frame, text="Selecionar Imagem", command=processar_imagem)
btn_selecionar.pack(pady=10)

info_text = tk.StringVar()
info_label = ttk.Label(frame, textvariable=info_text, wraplength=800, justify='center')
info_label.pack(pady=10)

fig = plt.figure(figsize=(15, 5))
fig.patch.set_facecolor('#4B0082')  
ax_imagem = fig.add_subplot(131)
ax_hist = fig.add_subplot(132)
ax_scatter = fig.add_subplot(133)

for ax in [ax_imagem, ax_hist, ax_scatter]:
    ax.set_facecolor('#663399')  
    ax.tick_params(colors='white', labelsize=8)

def ajustar_layout():
    plt.tight_layout(pad=3.0)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

btn_fechar = ttk.Button(frame, text="Fechar", command=root.quit)
btn_fechar.pack(pady=10)

root.mainloop()
