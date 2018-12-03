import json

# path for annotations in the coco dataset
anno_path = '/media/mash-compute/My Passport/Andromeda/dataset/object_det/ms_coco/ms_coco_2017/annotations_trainval2017/annotations/instances_val2017.json'


with open(anno_path) as json_file:
    json_file = json_file.read()
    data = json.loads(json_file)

annotations = data['annotations']
print(type(annotations))
print(type(annotations[1]))
image_anno_dict = dict()

one_image = []

for i in range(len(annotations)):
    search_dict = annotations[i]
    
    if search_dict['image_id'] == 289343:
        one_image.append(search_dict)

#print(search_dict)
        
