import os
import re
def trans_classes(dir_path):
    paths = os.listdir(dir_path)
    pattern = re.compile('<name>(.*?)</name>')
    for path in paths:
        with open(os.path.join(dir_path, path), 'r', encoding='utf-8') as f:
            text = f.read()
            if '腺瘤' in text:
                text = pattern.sub('<name>adenoma</name>', text)
            else:
                text = pattern.sub('<name>others</name>', text)
        with open(os.path.join(dir_path, path), 'w', encoding='utf-8') as f:
            f.write(text)
trans_classes('../VOCdevkit/VOC2007/Annotations')

