import sys
import logging
import os
from PyQt5 import QtWidgets
from tensorflow import keras
from tensorflow.keras import layers, Model
from tensorflow.keras.models import load_model
from MainWindow import Ui_MainWindow
import numpy as np

# hard coded values
DEFAULT_INPUT_SHAPE = (96,96,1)
DEFAULT_MODEL_FILE = r"sample/baseline-LeNet5.h5"
logger = logging.getLogger(__name__)

class FacialPointViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super(FacialPointViewer, self).__init__() # by including an instance, super returns a bound method
        self._model_name = DEFAULT_MODEL_FILE
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
        self.setupUI()
        self.setupModel()
        self.predict()

    def predict(self):
        for a in range(100):
            input = np.random.rand(1,96,96,1)
            y_label = self._model.predict(input)
            logger.info(f"{a}: predicted {y_label}")

    def startCapture(self):
        pass

    def setupUI(self):
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        logger.info(f"Loaded UI")

        pass

    def setupModel(self):
        self._model = load_model(self._model_name)
        logger.info(f"Loaded model: {self._model_name}")

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    facialviewer = FacialPointViewer()
    facialviewer.show()
    sys.exit(app.exec())