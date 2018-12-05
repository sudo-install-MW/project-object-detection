import json
import argparse
from coco_parser.utils.util_script import CocoTFRecordConverter as CocoRecordConverter


parser = argparse.ArgumentParser()
parser.add_argument("--anno_path", help="provide path for the coco .json anno file")
parser.add_argument("--image_path", help="path for images from the coco dataset")
args = parser.parse_args()

# path for annotations in the coco dataset
anno_path = '/media/maheshwaran/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/annotations_trainval2017/annotations/instances_val2017.json'
cat_dict = {1: 'person', 3: 'car'}

tf_record_creater = CocoRecordConverter(cat_dict, anno_path)
img_spec_dict, anno_dict = tf_record_creater.dict_initializer()
