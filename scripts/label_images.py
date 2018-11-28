import os
import shutil

path = 'neg_depressing'
new_dir = 'neg_dep_label'
imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
dir = os.listdir(path)

for i in dir:
    imgpath = path+ '\\'+ str(i) + '\\' + 'gsv_0.jpg'
    try:
        shutil.copy(imgpath, new_dir+'\\'+str(i)+'.jpg')
    except:
        pass
    
    




