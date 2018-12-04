import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--anno_path", help="provide path for the coco .json anno file")
parser.add_argument("--image_path", help="path for images from the coco dataset")
args = parser.parse_args()

# path for annotations in the coco dataset
anno_path = '/media/maheshwaran/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/annotations_trainval2017/annotations/instances_val2017.json'

# open the .json file
with open(anno_path) as json_file:
    json_file = json_file.read()
    data = json.loads(json_file)

anno_dict = dict()
img_spec = dict()
cat_dict = {1:'person', 3:'car'}

# loop creates a dictionary with image id as key and file_name and h, w as inner dict
for image_spec in data['images']:
    buff_dict = dict()
    for key, value in image_spec.items():
        if key == 'file_name':
            buff_dict['file_name'] = value
        if key == 'height':
            buff_dict['height'] = value
        if key == 'width':
            buff_dict['width'] = value

    img_spec[image_spec['id']] = buff_dict

for anno in data['annotations']:
    # if annotations category id matches with what we want
    # add it to the annotation dictionary
    if anno['category_id'] in cat_dict:
        anno_buff_dict = dict()
        for key, value in anno.items():
            if key == 'category_id':
                anno_buff_dict['category_id'] = value
            if key == 'bbox':
                anno_buff_dict['bbox'] = value

        # if image has no entry of annotation
        if anno['image_id'] not in anno_dict:
            anno_dict[anno['image_id']] = [anno_buff_dict]

        # if image has an annotation already
        else:
            anno_dict[anno['image_id']].append(anno_buff_dict)


print(anno_dict)