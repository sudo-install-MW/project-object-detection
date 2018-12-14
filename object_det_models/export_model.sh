#!/usr/bin/env bash

# From tensorflow/models/research/
INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/pipeline.config
TRAINED_CKPT_PREFIX=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/checkpoints/model.ckpt-170085
EXPORT_DIR=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/frozen_model
python3 /home/mash-compute/universe/tensorflow_models/models/research/object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}