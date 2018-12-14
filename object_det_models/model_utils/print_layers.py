import tensorflow as tf


def printtensors(pb_file):

    # read pb into graph_def
    with tf.gfile.GFile(pb_file, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # import graph_def
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def)

    # print operations
    for op in graph.get_operations():
        print(op.name)


printtensors("/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/frozen_model/frozen_inference_graph.pb")