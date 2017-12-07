import pdf2img
import baidu_ocr
import fire

class Pdf2txt(object):
    def file(self, pdf_path):
        imgs_path = "/Users/gaoshuaipeng/peng/my/mini_task/input"
        txt_path = "/Users/gaoshuaipeng/peng/my/mini_task/output/1.txt"
        pdf2img.convert_pdf_to_jpg(pdf_path)
        baidu_ocr.read_files(imgs_path, txt_path)
if __name__ == '__main__':
    fire.Fire(Pdf2txt)