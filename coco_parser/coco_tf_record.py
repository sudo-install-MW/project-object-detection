import argparse
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
tf_record_save_path = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017'
img_source = ''
cat_dict = {1: 'person', 3: 'car'}


tf_record_creater = CocoRecordConverter(cat_dict, anno_path)
img_spec_dict, anno_dict = tf_record_creater.dict_initializer()
print("creating tf record")

create_tf_record(img_spec=img_spec_dict, img_anno=anno_dict, save_path=tf_record_save_path, img_source_path=img_source, cat_dict=cat_dict)

print("created tf record successfully")