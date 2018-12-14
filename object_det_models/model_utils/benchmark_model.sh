#!/usr/bin/env bash
frozen_model_path=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/frozen_model/frozen_inference_graph.pb

bazel-bin/tensorflow/tools/benchmark/benchmark_model \
  --graph=$frozen_model_path \
  --input_layer="input:0" \
  --input_layer_shape="1,224,224,3" \
  --input_layer_type="float" \
  --output_layer="output:0"