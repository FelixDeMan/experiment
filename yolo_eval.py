from ultralytics import YOLO
import pandas as pd
import os
from statistics import mean
import json
import easyocr




def init_models(weights = "yolo_weights/iteration_03/best.pt"):
    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
    return YOLO(weights), reader

def run_yolo_eval_lora(yolo_model, ocr_model, folder, conf = 0.7, outfile = 'yolo_eval.csv', start_step = 0):

   


    rows = []
    df = pd.DataFrame()
    for i, subfolder in enumerate(os.listdir(folder)):
        if start_step > i:
            continue

        if start_step == i:
            df = pd.read_csv(f"step_{i}_{outfile}")
            rows = df.to_dict('records')
            continue

        row = {}
        print(subfolder)
        row['model'] = folder.split("_")[0]
        row['git'] = subfolder
        print(row['model'])
       
        row['UNet_lr'] = (subfolder.split("UNet")[1].split("TE")[0])
        row['TE_lr'] = (subfolder.split("TE")[1].split("dim")[0])
        row['dim'] = (subfolder.split("dim")[1])
        path = os.path.join(folder, subfolder)
       
        for image_folder in (os.listdir(path)):
            
            full_path = os.path.join(path, image_folder)
            if os.path.isdir(full_path) and image_folder != 'logs':
                if 'git' in image_folder:
                    continue
                results = yolo_model(full_path, save = True, conf = conf)
                confidence_scores_original =[(result.boxes.conf.tolist()) for result in results]
                epoch = image_folder.split("-")[-1]
                if epoch == 'red_hugo_logo': epoch = '000030'
                row['epoch'] = epoch
                confidence_scores_processed = [0 if len(score) == 0 else max(score) for score in confidence_scores_original]
                row['mean_confidence_score'] = mean(confidence_scores_processed)
                row['confidence_scores_processed'] = confidence_scores_processed
                row['confidence_scores'] = confidence_scores_original

                # OCR
                #Loop over all images in the folder
                ocr_results = []
                ocr_scores = []
                for image in os.listdir(full_path):
                    if image.endswith(".png"):
                        image_path = os.path.join(full_path, image)
                        result = ocr_model.readtext(image_path, detail = 0)
                        ocr_score = 0
                        for string in result:
                            if string.lower().replace('0', 'o') == 'hugo':
                                ocr_score = 1
                        ocr_results.append(result)
                        ocr_scores.append(ocr_score)
                row['ocr_results'] = ocr_results
                row['ocr_scores'] = ocr_scores
                row['mean_ocr_score'] = mean(ocr_scores)

                
              
                rows.append(row.copy())
                with open(f'{full_path}/yolo_eval.json', 'w') as f:
                    json.dump(row, f)
               
        df = pd.DataFrame(rows)
        print(df)
        df.to_csv(f"step_{i}_{outfile}")
    df = pd.DataFrame(rows)
    df.to_csv(outfile)
    return df

def place_imgs_per_epoch(folder):
    for i, subfolder in enumerate(os.listdir(folder)):

        path = os.path.join(folder, subfolder)
        if 'sample' in os.listdir(path):
            
            epochs = []
            full_path = os.path.join(path, 'sample')
            for pic in os.listdir(full_path):
                if not pic.endswith(".png"):
                    continue
                pic_path = os.path.join(full_path, pic)

                #red_hugo_logo_db_20230524090008_e000003_00
                #red_hugo_logo_db_20230524091425_e000030_04
                epoch = pic.split("e0000")[1].split("_")[0]
                print(epoch)
                epochs.append(epoch)
            for epoch in epochs:
                os.makedirs(os.path.join(path, epoch), exist_ok = True)
            
                for pic in os.listdir(full_path):
                    if not pic.endswith(".png"):
                        continue
                    if epoch in pic.split("e0000")[1].split("_")[0]:
                        print(epoch, subfolder)
                        os.rename(os.path.join(full_path, pic), os.path.join(path, epoch, pic))

    return
                

def run_yolo_eval(yolo_model, ocr_model, folder, conf = 0.7, outfile = 'yolo_eval.csv', start_step = 0):

   


    rows = []
    df = pd.DataFrame()
    for i, subfolder in enumerate(os.listdir(folder)):
        if start_step > i:
            continue

        if start_step == i and start_step != 0:
            df = pd.read_csv(f"step_{i}_{outfile}")
            rows = df.to_dict('records')
            continue

        row = {}
        print(subfolder)
        row['model'] = folder.split("_")[0]
        row['git'] = subfolder
        print(row['model'])
       
        row['UNet_lr'] = (subfolder)
       
        path = os.path.join(folder, subfolder)
       
        for image_folder in (os.listdir(path)):
            
            full_path = os.path.join(path, image_folder)
            if os.path.isdir(full_path) and image_folder != 'logs' and image_folder != 'sample':
                if 'git' in image_folder:
                    continue
                results = yolo_model(full_path, save = True, conf = conf)
                confidence_scores_original =[(result.boxes.conf.tolist()) for result in results]
                epoch = image_folder
                row['epoch'] = epoch
               
                confidence_scores_processed = [0 if len(score) == 0 else max(score) for score in confidence_scores_original]
                row['mean_confidence_score'] = mean(confidence_scores_processed)
                row['confidence_scores_processed'] = confidence_scores_processed
                row['confidence_scores'] = confidence_scores_original

                # OCR
                #Loop over all images in the folder
                ocr_results = []
                ocr_scores = []
                for image in os.listdir(full_path):
                    if image.endswith(".png"):
                        image_path = os.path.join(full_path, image)
                        result = ocr_model.readtext(image_path, detail = 0)
                        ocr_score = 0
                        for string in result:
                            if string.lower().replace('0', 'o') == 'hugo':
                                ocr_score = 1
                        ocr_results.append(result)
                        ocr_scores.append(ocr_score)
                row['ocr_results'] = ocr_results
                row['ocr_scores'] = ocr_scores
                row['mean_ocr_score'] = mean(ocr_scores)

                
                print(row)
                rows.append(row.copy())
                with open(f'{full_path}/yolo_eval.json', 'w') as f:
                    json.dump(row, f)
               
        df = pd.DataFrame(rows)
        print(df)
        df.to_csv(f"step_{i}_{outfile}")
    df = pd.DataFrame(rows)
    df.to_csv(outfile)
    return df



if __name__ == '__main__':
    place_imgs_per_epoch('ti_output')
    yolo_model, ocr_model = init_models()
    #yolo_model = None
    df = run_yolo_eval(yolo_model, ocr_model, 'ti_output', outfile = 'yolo_eval_ti.csv', start_step = 0)


    place_imgs_per_epoch('ti_output')



    # base = r'C:\Users\Jan-FelixdeMan\experiment\lora_output\UNet0_0001TE0_0001dim16'
    # for thing in os.listdir(r'C:\Users\Jan-FelixdeMan\experiment\lora_output\UNet0_0001TE0_0001dim16'):
    #     print(thing, os.path.isdir(os.path.join(base,thing)))
    