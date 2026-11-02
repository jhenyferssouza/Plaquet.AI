from pathlib import Path

# Corrigindo os caminhos
base_dir = Path("D:/modeloIA_Plaquet.AI/src")
img_dir_train = base_dir / "output_yolo" / "train"
img_dir_val = base_dir / "output_yolo" / "val"

def analisar_diretorio(diretorio, nome):
    print(f"\nAnalisando diretório {nome}: {diretorio}")
    if not diretorio.exists():
        print(f"O diretório {diretorio} não existe!")
        return

    imagens = list(diretorio.glob("*.jpeg"))
    rotulos = list(diretorio.glob("*.txt"))

    print(f"Total de imagens JPEG: {len(imagens)}")
    print(f"Total de rótulos TXT: {len(rotulos)}")

    if imagens:
        print("Exemplos de imagens:")
        for img in imagens[:5]:
            print(f"  {img.name}")

    if rotulos:
        print("Exemplos de rótulos:")
        for rot in rotulos[:5]:
            print(f"  {rot.name}")

    # Verificar correspondência
    for img in imagens:
        rotulo = diretorio / (img.stem + ".txt")
        if not rotulo.exists():
            print(f"Rótulo ausente para: {img.name}")

analisar_diretorio(img_dir_train, "Treinamento")
analisar_diretorio(img_dir_val, "Validação")