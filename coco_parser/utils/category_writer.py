import json

# path for annotations in the coco dataset
anno_path = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/annotations_trainval2017/annotations/instances_val2017.json'

with open(anno_path) as annotations:
    annotations = annotations.read()
    annotation_dict = json.loads(annotations)
    with open('./categories.txt', 'w') as f:
        for entries in annotation_dict['categories']:
            f.write('image id : {} '.format(entries['id']))
            f.write('category name : {}\n'.format(entries['name']))