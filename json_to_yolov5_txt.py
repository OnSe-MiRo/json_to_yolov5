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
            bbox=np.array(i['bbox'],dtype=np.int)
            bbox=np.array([bbox[0]+bbox[2], bbox[1]+bbox[3], np.abs(bbox[2]-bbox[0]), np.abs(bbox[3]-bbox[1])], dtype=np.int)
            bbox_to_resize=np.array([width*2,height*2,width,height],dtype=np.int)
            rebbox=np.divide(bbox,bbox_to_resize)
            new_txt.write(str(category_id)+' '+str(rebbox[0])+' '+str(rebbox[1])+' '+str(rebbox[2])+' '+str(rebbox[3])+'\n')
    
