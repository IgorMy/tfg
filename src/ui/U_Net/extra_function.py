import tensorflow as tf
from tensorflow.keras import backend as K


punto_de_corte = 0.90  # % seguro de que se ha detectado un pixel de cara, utilizado para las metricas de evaluacion


def iou(y_true, y_pred):

    y_true_binary = tf.math.greater_equal(y_true, punto_de_corte)
    y_pred_binary = tf.math.greater_equal(y_pred, punto_de_corte)

    intersection = K.sum(
        tf.cast(tf.logical_and(y_true_binary, y_pred_binary), tf.float32)
    )
    union = K.sum(tf.cast(tf.logical_or(y_true_binary, y_pred_binary), tf.float32))

    iou = (intersection + 1e-15) / (union + 1e-15)  # avoid division by zero
    return iou


def precision(y_true, y_pred):

    y_true_binary = tf.math.greater_equal(y_true, punto_de_corte)
    y_pred_binary = tf.math.greater_equal(y_pred, punto_de_corte)
    intersection = tf.logical_and(y_true_binary, y_pred_binary)

    tp = K.sum(tf.cast(intersection, tf.float32))
    fpAndTp = K.sum(tf.cast(y_pred_binary, tf.float32))

    return (tp + 1e-15) / (fpAndTp + 1e-15)


def recall(y_true, y_pred):

    y_true_binary = tf.math.greater_equal(y_true, punto_de_corte)
    y_pred_binary = tf.math.greater_equal(y_pred, punto_de_corte)

    intersection = tf.logical_and(y_true_binary, y_pred_binary)
    not_y_pred_binary = tf.math.logical_not(y_pred_binary)

    tp = K.sum(tf.cast(intersection, tf.float32))

    fn = K.sum(tf.cast(tf.logical_and(y_true_binary, not_y_pred_binary), tf.float32))

    return (tp + 1e-15) / (tp + fn + 1e-15)


def f1_score(y_true, y_pred):

    def recall(y_true, y_pred):

        y_true_binary = tf.math.greater_equal(y_true, punto_de_corte)
        y_pred_binary = tf.math.greater_equal(y_pred, punto_de_corte)

        intersection = tf.logical_and(y_true_binary, y_pred_binary)
        not_y_pred_binary = tf.math.logical_not(y_pred_binary)

        tp = K.sum(tf.cast(intersection, tf.float32))

        fn = K.sum(
            tf.cast(tf.logical_and(y_true_binary, not_y_pred_binary), tf.float32)
        )

        return (tp + 1e-15) / (tp + fn + 1e-15)

    def precision(y_true, y_pred):

        y_true_binary = tf.math.greater_equal(y_true, punto_de_corte)
        y_pred_binary = tf.math.greater_equal(y_pred, punto_de_corte)
        intersection = tf.logical_and(y_true_binary, y_pred_binary)

        tp = K.sum(tf.cast(intersection, tf.float32))
        fpAndTp = K.sum(tf.cast(y_pred_binary, tf.float32))

        return (tp + 1e-15) / (fpAndTp + 1e-15)

    prec = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)

    score = (2 * prec * recall + 1e-15) / (prec + recall + 1e-15)
    return score
