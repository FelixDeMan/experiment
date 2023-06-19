
import os
import numpy as np

from PIL import Image, ImageDraw, ImageFont

def image_grid_with_labels(imgs, rows, cols, row_labels, col_labels):
    assert len(imgs) == rows * cols
    assert len(row_labels) == rows
    assert len(col_labels) == cols

    w, h = imgs[0].size
    label_size = 150  # the size of the area to draw the label, adjust as needed

    # create the grid, adding extra space for labels
    #grid = Image.new('RGB', size=(cols*w + label_size, rows*h + label_size), color='black')
    grid = Image.new('RGB', size=(cols*w + label_size, rows*h ), color='black')
    draw = ImageDraw.Draw(grid)

    #font = ImageFont.truetype(font_path, 20)  # replace font_path with the path to a .ttf font file
    font = ImageFont.FreeTypeFont("Swansea-q3pd.ttf", 35)

    # paste the images into the grid
    for i, img in enumerate(imgs):
        #grid.paste(img, box=(i%cols*w + label_size, i//cols*h + label_size))
        grid.paste(img, box=(i%cols*w + label_size, i//cols*h ))

    # draw the row labels
    for i, label in enumerate(row_labels):
        draw.text((0, i*h + label_size), label, fill="white", font=font)

    # # draw the column labels
    # for i, label in enumerate(col_labels):
    #     draw.text((i*w + label_size, 0), label, fill="white", font=font)

    return grid


def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

# main_folder = r"C:\Users\Jan-FelixdeMan\experiment\db_output01"
# for folder in os.listdir(main_folder):
#     imgs = []
#     path = os.path.join(main_folder, folder,"sample")
#     if os.path.exists(path) == False: continue
#     for img in os.listdir(path):
#         if img.endswith(".png"):
#             img = Image.open(os.path.join(path, img))
#             imgs.append(img)
#     print(imgs)
#     grid = image_grid(imgs, 10, 6)
#     grid.save('grid_db_{}.png'.format(folder))
# imgs = [r"C:\Users\Jan-FelixdeMan\experiment\runs\detect\predict6\im_20230517130329_002_1863244118.png",r"C:\Users\Jan-FelixdeMan\experiment\runs\detect\predict6\im_20230517130412_003_165327925.png", r"C:\Users\Jan-FelixdeMan\experiment\runs\detect\predict6\im_20230517130510_001_323334274.png",r"C:\Users\Jan-FelixdeMan\experiment\runs\detect\predict6\im_20230517131103_001_1515800448.png"]
# pils = []
# for img in imgs:
#     pils.append(Image.open(img))



# grid = image_grid(pils, 2, 2)
# grid.save('yolo_example.png')
imgs = []
path = r"db_output01\lr0_00002\21"
for img_path in os.listdir(path):
    if img_path.endswith(".png"):
        img = Image.open(os.path.join(path, img_path))
        imgs.append(img)
grid= image_grid(imgs, 1,6)   
grid.save('grid_db_lr0_00002_21.png')                  
    

# data = [["UNet5e-05TE5e-06dim4", 30],
#         ["UNet5e-05TE5e-06dim8", 30],
#         ["UNet5e-05TE5e-06dim16", 30],
#         ["UNet5e-05TE5e-06dim32", 30],
#         ["UNet5e-05TE5e-06dim64", 30]]
#         # ["UNet5e-05TE5e-06dim16", 6]]
#         # ["UNet5e-05TE5e-06dim16", 9],
#         # ["UNet5e-05TE5e-06dim16", 12],
#         # ["UNet5e-05TE5e-06dim16", 15],
#         # ["UNet5e-05TE5e-06dim16", 18],
#         # ["UNet5e-05TE5e-06dim16", 21],
#         # ["UNet5e-05TE5e-06dim16", 24],
#         # ["UNet5e-05TE5e-06dim16", 27],
#         # ["UNet5e-05TE5e-06dim16", 30]
#         # ]

# # data = [
# #     ['UNet1e-05TE1e-05dim64' , 30],
# #      ['UNet1e-05TE1e-05dim4' , 30],
# #     ['UNet1e-05TE1e-05dim64' , 15],
# #     ['UNet1e-05TE1e-05dim64' , 3],
# #     ['UNet1e-05TE1e-05dim64' , 9],
# #     ['UNet1e-05TE1e-05dim64' , 21], 
# #     # ["UNet5e-06TE0_0001dim16", 30],
# #     # ["UNet5e-06TE0_0001dim16", 21],
# #     # ["UNet5e-06TE0_0001dim16", 15]
# #     # ["UNet5e-06TE0_0001dim16", 3],
# #     # ["UNet5e-05TE5e-06dim16", 21],
# #     # ["UNet5e-06TE0_0001dim16", 6],
# #     # ["UNet5e-05TE5e-06dim8", 24],
# #     # ["UNet5e-05TE5e-06dim32", 18],
# #     # ["UNet5e-05TE5e-06dim64", 27],
# #     # ["UNet5e-06TE5e-05dim4", 18],
# #     # ["UNet5e-06TE0_0001dim16", 9],
# #     # ["UNet5e-06TE5e-05dim16", 6],
# #     # ["UNet5e-06TE1e-05dim64", 15],
# #     # ["UNet0_0001TE0_0001dim8", 3],
# #     # ["UNet5e-05TE5e-06dim64", 15],
# #     # ["UNet5e-06TE5e-06dim64", 27],
# #     # ["UNet5e-05TE5e-06dim32", 15],
# #     # ["UNet5e-05TE5e-06dim64", 12],
# #     # ["UNet5e-06TE5e-05dim16", 9],
# #     # ["UNet5e-06TE0_0001dim8", 3],
# #     # ["UNet5e-05TE5e-06dim64", 30],
# #     # ["UNet5e-06TE0_0001dim4", 6],
# #     # ["UNet5e-05TE5e-06dim16", 24],
# #     # ["UNet5e-06TE0_0001dim4", 9],
# #     # ["UNet5e-06TE1e-05dim64", 21],
# #     # ["UNet5e-05TE5e-06dim16", 18],
# #     # ["UNet5e-05TE5e-06dim64", 9],
# #     # ["UNet5e-06TE5e-06dim32", 30],
# #     # ["UNet5e-05TE5e-06dim64", 3]
# # ]

# models_epoch = {}

# for item in data:
#     git_value = item[0]
#     epoch_value = item[1]
    
#     if git_value in models_epoch:
#         models_epoch[git_value].append(epoch_value)
#     else:
#         models_epoch[git_value] = [epoch_value]

# # 3
# # 21
# # 6
# # 24
# # 18
# print(models_epoch)
# imgs = []
# for model in models_epoch.keys(): 
#     print(model, models_epoch[model])
    
#     epochs = models_epoch[model]
    
#     for epoch in epochs:
#         print(epoch)
#         #imgs = []
#         folder = f'lora_output/{model}/red_hugo_logo-00000{epoch}'
#         if len(str(epoch)) == 2:
#             folder = f'lora_output/{model}/red_hugo_logo-0000{epoch}'
#         if epoch == 30:
#             folder = f'lora_output/{model}/red_hugo_logo'
       
#         print(folder)
#         for  file in (os.listdir(folder)):
            
#                 if file.endswith('.png'):
#                     #print(file)
#                     if '000' in file:
#                         img = Image.open(f'{folder}/{file}')
#                         imgs.append(img)
                    
# rows = 5 
# print(len(imgs))
# cols = len(imgs)//rows # this is a floor division, so we lose the last row
# print(cols)
# # row_labels = np.linspace(3, 30, rows, dtype=int)
# # row_labels = ["epoch " +str(label) for label in row_labels]
# row_labels = ["Rank " +str(rank) for rank in [4, 8, 16, 32, 64]]
# print(row_labels)
# col_labels = np.linspace(1, 5, cols, dtype=str)
# grid = image_grid_with_labels(imgs, rows, cols, row_labels, col_labels)
# grid.save(f'grids/{model}_epoch{epoch}_dim_compare.png')
#     #print(f'../lora_output/{model}/red_hugo_logo-0000{epoch}.png')