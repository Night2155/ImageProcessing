import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import matplotlib.pyplot as plt

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键

    def __init__(self, parent=None, width=6, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def Show_Histogram(self, oriimg):
        if len(oriimg.shape) == 3:
            color = ('b', 'g', 'r')
            alpha = (0.6, 0.6, 0.5)
            for i, col in enumerate(color):
                hist_graphic = cv2.calcHist([oriimg], [i], None, [256], [0, 256])
                plt.bar(range(0, 256), hist_graphic.ravel(), color=color[i], alpha=alpha[i])
            plt.title("RGB Histogram")
            plt.show()
        else:
            color = 'gray'
            alpha = 0.6
            hist_graphic = cv2.calcHist([oriimg], [0], None, [256], [0, 256])
            plt.figure()
            plt.bar(range(0, 256), hist_graphic.ravel(), color=color, alpha=alpha)
            plt.title("Gray Histogram")
            plt.show()

