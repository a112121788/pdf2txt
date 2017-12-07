# encoding=utf8

# 引入文字识别OCR SDK
import os
import re
from aip import AipOcr
import CONFIG

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 读取文件夹
def read_files(dir, output_filename):
    # 初始化ApiOcr对象
    aipOcr = AipOcr(CONFIG.APP_ID, CONFIG.API_KEY, CONFIG.SECRET_KEY)
    files = []
    # imag sort
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            file = os.path.join(parent, filename)
            m = re.search(r"\.(png|jpg)", str(file))
            if m:
                files.append(os.path.join(parent, filename))
    files.sort()

    # ocr
    output_file = open(output_filename, 'a+')
    for f in files:
        print(f)
        options = {
            'probability': 'true',
        }
        result = aipOcr.basicGeneral(get_file_content(f), options=options)
        if (None is not result) and (result['words_result'] is not None):
            for word in result['words_result']:
                output_file.write(word["words"])
                output_file.write("\n")
            os.remove(f)
    output_file.close();
