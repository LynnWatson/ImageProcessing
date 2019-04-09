import cv2
import sys
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow


class MainCode(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainCode, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('图像处理软件')  # 窗口名字
        self.chooseImgBtn.clicked.connect(self.onchooseImgBtnClicked)
        self.histBtn.clicked.connect(self.onhistBtnClicked)
        self.binaryBtn.clicked.connect(self.onbinaryBtnClicked)
        self.zoomscale = 1  # 图片放缩尺度

    def onchooseImgBtnClicked(self, remark):
        print(remark)
        print("load--file")

        # 加载图片，QFileDialog就是系统对话框的那个类
        # 第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
        src, _ = QFileDialog.getOpenFileName(self, '加载源图', 'F:\picture for lhr\\', 'Image files(*.jpg *.gif *.png)')

        # 使用OpenCV转换为灰度图
        img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)  # 读取图片，第二个参数表示以灰度图像读入
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        frame = QImage(img, x, y, QImage.Format_RGB888)

        # 创建图元和场景，显示图片
        # pix = QPixmap.fromImage(frame)  # 两条语句都可以
        pix = QPixmap(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.sourceView.setScene(self.scene)  # 将场景添加至视图

        # 参数:原图像 通道[0]-灰度图 掩码 BINS为256 像素范围0-255
        hist = cv2.calcHist(img, [0], None, [256], [0, 255])
        print(type(hist))
        print(hist.size)
        print(hist.shape)
        # print(hist)

        fig = plt.figure()  # 创建图形窗口的意思
        # 设置布局
        ax = fig.add_subplot(1,2,1)  # 用一个变量接收1行2列中的第1个绘图区
        ax.plot(hist)  # 在这个绘图区上作画

    def onhistBtnClicked(self):
        self.histView.setScene(self.scene)

    def onbinaryBtnClicked(self):
        self.Title.setText("Hello China")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())
