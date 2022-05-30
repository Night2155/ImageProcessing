import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import matplotlib.pyplot as plt

class Figure_Canvas(FigureCanvas):

    def __init__(self):
        fig = Figure(figsize=(10, 10), dpi=100)
        FigureCanvas.__init__(self, fig)

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

