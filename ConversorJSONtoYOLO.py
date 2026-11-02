import pandas as pd
import json
import os
from glob import glob

def convert_json_to_yolo(json_file, output_dir, image_width, image_height):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data['objects'])
    
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(json_file))[0] + '.txt')
    
    with open(output_file, 'w') as f:
        for _, obj in df.iterrows():
            class_id = 13304 if obj['classTitle'] == 'Platelets' else 0
            x1, y1 = obj['points']['exterior'][0]
            x2, y2 = obj['points']['exterior'][1]
            
            width = x2 - x1
            height = y2 - y1
            
            x_center = (x1 + width / 2) / image_width
            y_center = (y1 + height / 2) / image_height
            norm_width = width / image_width
            norm_height = height / image_height
            
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")

def main():
    json_dir = r'D:\Pla_AI\NinjaData\train\ann'
    output_dir = r'C:\Pla_AI\ModelIA\output_yolo'
    
    os.makedirs(output_dir, exist_ok = True)
    
    image_width = int(input("Digite a largura das imagens: "))
    image_height = int(input("Digite a altura das imagens: "))
    
    json_files = glob(os.path.join(json_dir, '*.json'))
    
    for json_file in json_files:
        convert_json_to_yolo(json_file, output_dir, image_width, image_height)
    
    print("Conversão concluída!")

if __name__ == "__main__":
    main()
