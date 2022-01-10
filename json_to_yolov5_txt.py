import json
import numpy as np
from glob import glob
from tqdm import tqdm

def json_to_yolov5_txt(json_folder_path,save_txt_folder_path):
    json_list=glob(json_folder_path+'/*.json')
    for i in tqdm(range(len(json_list))):
        f=open(json_file_path)
        data=json.load(f)
        txt_nmae=str(save_txt_folder_path)+'/'+data['label_info']['image']['file_name'][:-4]+'.txt'
        new_txt=open(txt_nmae,'w')
        width=data['label_info']['image']['width']
        height=data['label_info']['image']['height']
        for i in data['label_info']['annotations']:
            category_id=i['category_id']
            bbox=np.array(i['bbox'],dtype=np.float32)
            bbox_to_resize=np.array([1/width,1/height,1/width,1/height],dtype=np.float32)
            rebbox=bbox*bbox_to_resize
            new_txt.write(str(category_id)+' '+str(rebbox[0])+' '+str(rebbox[1])+' '+str(rebbox[2])+' '+str(rebbox[3])+'\n')
    
