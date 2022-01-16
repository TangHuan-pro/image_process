import os
xml_path = r'C:\Users\pc\Documents\WeChat Files\wxid_xq1fwlovrbhv22\FileStorage\File\2021-12\图像标注\Annotations'
jpg_path = r'C:\Users\pc\Documents\WeChat Files\wxid_xq1fwlovrbhv22\FileStorage\File\2021-12\图像标注\JPEGImages'
all_xml = [name[:-4] for name in os.listdir(xml_path)]
all_xml =set(all_xml)
count = 0
for name in os.listdir(jpg_path):
    if name[:-4] not in all_xml:
        os.remove(os.path.join(jpg_path, name))
        continue
    count += 1
print('图片总数为：', count)

#
# import os
# from classes_statistic import statistic
# xml_path = '../VOCdevkit/VOC2007/Annotations'
# jpg_path = '../VOCdevkit/VOC2007/JPEGImages'
# statis_res = statistic(jpg_path)
# adenoma_nums = (statis_res['Hyperplastic_polyp']+statis_res['Other_polyps'])//2
# count = 0
# # for name in os.listdir(jpg_path):
# #     if '腺瘤' in name and count <= adenoma_nums:
# #         count += 1
# #         continue
# #     if '腺瘤' in name and count > adenoma_nums:
# #         os.remove(os.path.join(jpg_path, name))
# #         os.remove(os.path.join(xml_path, name[:-4]+'.xml'))
# print(statistic(jpg_path))