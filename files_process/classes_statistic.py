import os
path = '../VOCdevkit/VOC2007/JPEGImages'
def statistic(dir_path):
    count = 0
    names = os.listdir(dir_path)
    statis = {'普通腺瘤':0, '绒毛腺瘤': 0, '炎性息肉': 0, '增生息肉': 0, '齿状腺瘤': 0}
    statis_3 = {'腺瘤': 0, '增生': 0, '其他': 0}

    for name in names:
        count += 1
        if '绒毛' in name:
            statis['绒毛腺瘤'] += 1
            statis_3['其他'] += 1
        elif '增生' in name:
            statis['增生息肉'] += 1
            statis_3['增生'] += 1
        elif '炎性' in name:
            statis['炎性息肉'] += 1
            statis_3['其他'] += 1
        elif '齿状' in name:
            statis['齿状腺瘤'] += 1
            statis_3['其他'] += 1
        elif '腺瘤' in name:
            statis['普通腺瘤'] += 1
            statis_3['腺瘤'] += 1
    return statis, statis_3

print(statistic(path))