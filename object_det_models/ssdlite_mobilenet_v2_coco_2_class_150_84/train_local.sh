#!/usr/bin/env bash
PIPELINE_CONFIG_PATH=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssdlite_mobilenet_v2_coco_2_class_150_84/pipeline.config

MODEL_DIR=/home/mash-compute/universe/sandbox/project-object-detection/object_det_models/ssd_test/checkpoints

NUM_TRAIN_STEPS=200000
SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python3 /home/mash-compute/universe/tensorflow_models/models/research/object_detection/model_main.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --num_train_steps=${NUM_TRAIN_STEPS} \
    --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr
