import tensorflow as tf
from tensorflow.keras import backend as K
from PIL import Image
import cv2
import numpy as np

from src.ui.U_Net.extra_function import iou, precision, recall, f1_score

model = tf.keras.models.load_model(
    "model/model.h5",
    custom_objects={
        "iou": iou,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
    },
)


def UNet(image: Image):
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = cv2.resize(open_cv_image, (336, 256)) / 255.0
    predict = model.predict(np.expand_dims(image, axis=0))[0]
    normalized_prediction = (predict - np.min(predict)) / (
        np.max(predict) - np.min(predict)
    )
    scaled_prediction = (normalized_prediction * 255).astype(np.uint8)
    ret2, th2 = cv2.threshold(scaled_prediction, 0, 255, cv2.THRESH_OTSU)
    return th2
