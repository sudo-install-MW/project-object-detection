#!/usr/bin/env bash

tf_rec_file_name=cocotrain_ped_car.tfrecord
save_path=/media/mash-compute/My\ Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/${tf_rec_file_name}
img_source_path=/media/mash-compute/My\ Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/train2017/train2017
anno_path=/media/mash-compute/My\ Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/annotations_trainval2017/annotations/instances_train2017.json

python3 coco_tf_record.py --anno_path="${anno_path}" --image_path="${img_source_path}" --tf_record_save_path="${save_path}"