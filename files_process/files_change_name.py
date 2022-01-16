def change(dir_path):
    names = os.listdir(dir_path)
    for name in names:
        if ' ' in name:
            new_name = name.replace(' ', '_')
            os.rename(os.path.join(dir_path, name), os.path.join(dir_path, new_name))

import os
path1 = '../VOCdevkit/VOC2007/Annotations'
path2 = '../VOCdevkit/VOC2007/JPEGImages'
change(path1)
change(path2)
