import argparse
import time
import sys
sys.path.append('..')
from coco_parser.utils.util_script import CocoTFRecordConverter as CocoRecordConverter
from coco_parser.utils.tf_record_creater_proto import create_tf_record

parser = argparse.ArgumentParser()
parser.add_argument("--anno_path", help="provide path for the coco .json anno file")
parser.add_argument("--image_path", help="path for images from the coco dataset")
parser.add_argument("--tf_record_save_path", help="path where tf record needs to be saved")
args = parser.parse_args()

# path for annotations in the coco dataset
anno_path = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/' \
            'annotations_trainval2017/annotations/instances_val2017.json'
tf_record_save_path = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/cocoval.tfrecord'
img_source = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/val2017'

# add categories to customize dataset
cat_dict = {1: 'person', 3: 'car'}


tf_record_creater = CocoRecordConverter(cat_dict, args.anno_path)
img_spec_dict, anno_dict = tf_record_creater.dict_initializer()

print("################### creating tf record ###################")
print("creating record for categories {}".format(cat_dict))

for i in range(5):
    print("exit if you want in {} secs".format(5-i))
    time.sleep(1)

create_tf_record(img_spec=img_spec_dict, img_anno=anno_dict, save_path=args.tf_record_save_path,
                 img_source_path=args.image_path, cat_dict=cat_dict)
print("################### created tf record successfully ###################")
