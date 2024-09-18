import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyCanvas(FigureCanvas):
    def __init__(self, parent=None,dpi=100):
        """
        Initialize a Canvas widget.

        Parameters
        ----------
        parent : None or QWidget
            The parent widget of the Canvas.
        width : float
            The width of the canvas in inches.
        height : float
            The height of the canvas in inches.
        dpi : int
            The dots per inch of the canvas.

        Returns
        -------
        A Canvas widget.
        """
        self.fig,self.axes=plt.subplots()
        #self.axes = fig.add_subplot(111)
        super(MyCanvas, self).__init__(self.fig)