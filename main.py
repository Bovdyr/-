
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap
from random import*
import os

workdir = None

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = "Modified"

    def loagImage(self, filename):
        global image_part
        self.filename = filename
        image_part = os.path.join(workdir, filename)
        self.image = Image.open(image_part)

    def showImage(self, path):
        picture.hide()
        pixmapimage = QPixmap(path)
        w, h = picture.width(),  picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)
        picture.show()

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def flip_left_right(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def ROTATEl(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def ROTATEr(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def Contrast(self):
        self.image = self.image.ImageEnhance.Contrast(pic_original)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def Rezkost(self):
        enchancer = ImageEnhance.Sharpness(self.image)
        self.image = enchancer.enhance(5)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
        
    
    '''def BLUR(self):
        w = self.original.filter(ImageFilter.BLUR)
        w.save('dog2.jpg')
        self.changet.append(w)
        w.show()

    def ROTATE(self):
        t = self.original.transpose(Image.ROTATE_180)
        t.save('dog3.jpg')
        self.changet.append(t)
        t.show()

    def FLIP_LEFT_RIGHT(self):
        r = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        r.save('dog4.jpg')
        self.changet.append(r)
        r.show()'''

def filterq(felenames, extension):
    result = []
    for i in felenames:
        for o in extension:
            if i.endswith(o):
                result.append(i)
    return result

def showFilenamesList():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    felenames = os.listdir(workdir)
    extension = ['png', 'jpg', 'gif', 'jpeg']
    result=filterq(felenames, extension)
    teg.clear()
    for i in result:
        teg.addItem(i)

def showChosenImage():
    if teg.currentRow() >= 0 :
        filename = teg.currentItem().text()
        workimage.loagImage(filename)
        workimage.showImage(image_part)




 

pp = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')

teg = QListWidget()

picture = QLabel('Картинка')
createsam = QPushButton("Лево")
delsam = QPushButton("Право")
savesam = QPushButton("Зеркало")
addsam = QPushButton("Папка")
anpinsam = QPushButton("Резкость")
opensamteg = QPushButton("Ч/Б")
workimage = ImageProcessor()

layout_main = QHBoxLayout()
layout_main_left = QVBoxLayout()
layout_main_pravo = QVBoxLayout()
layout_main_nis = QHBoxLayout()

layout_main_left.addWidget(addsam)
layout_main_left.addWidget(teg)

layout_main_nis.addWidget(createsam, stretch=10)
layout_main_nis.addWidget(delsam, stretch=10)
layout_main_nis.addWidget(savesam, stretch=10)
layout_main_nis.addWidget(anpinsam, stretch=10)
layout_main_nis.addWidget(opensamteg, stretch=10)

layout_main_pravo.addWidget(picture)
layout_main_pravo.addLayout(layout_main_nis)

layout_main.addLayout(layout_main_left)
layout_main.addLayout(layout_main_pravo)

main_win.resize(700, 400)
main_win.setLayout(layout_main)

addsam.clicked.connect(showFilenamesList)
opensamteg.clicked.connect(workimage.do_bw)
savesam.clicked.connect(workimage.flip_left_right)
createsam.clicked.connect(workimage.ROTATEl)
delsam.clicked.connect(workimage.ROTATEr)
anpinsam.clicked.connect(workimage.Rezkost)

teg.currentRowChanged.connect(showChosenImage)
main_win.show()
pp.exec_()

