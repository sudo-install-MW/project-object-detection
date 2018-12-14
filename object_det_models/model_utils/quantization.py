import tensorflow as tf
model_path = '/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/frozen_model/frozen_inference_graph.pb'

input_arrays = ["image_tensor:0"]
output_arrays = ["detection_boxes:0", "detection_scores:0", "detection_classes:0", "num_detections:0"]

converter = tf.contrib.lite.TocoConverter.from_frozen_graph(model_path, input_arrays=input_arrays, output_arrays=output_arrays)
converter.post_training_quantize = True
tflite_quantized_model = converter.convert()
open("quantized_model.tflite", "wb").write(tflite_quantized_model)


# import tensorflow as tf
#
# converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
# tflite_model = converter.convert()
# open("converted_model.tflite", "wb").write(tflite_model)

# input_arrays = ["input"]
# output_arrays = ["MobilenetV1/Predictions/Softmax"]
#
# converter = tf.lite.TFLiteConverter.from_frozen_graph(
#   graph_def_file, input_arrays, output_arrays)
# tflite_model = converter.convert()
# open("converted_model.tflite", "wb").write(tflite_model)