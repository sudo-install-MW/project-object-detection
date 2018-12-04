# COCO dataset processing
## COCO .json under the hood
The coco dataset is annotated using .json file format which hosts five key values, the dictionary subset is represented as below:
```
'annotation':[{'area': 702.1057499999998, 'segmentation': [[ 9,...,423.01]], 'category_id': 18, 'iscrowd': 0, 'id': 1768, 'image_id': 289343, 'bbox': [473.07, 395.93, 38.65, 28.67]}]
'categories':[{'name': 'person', 'id': 1, 'supercategory': 'person'}...{}]
'images':[{'license': 4, 'coco_url': 'http://...0133.jpg', 'id': 397133, 'file_name': '000000397133.jpg', 'date_captured': '2013-11-14 17:02:52', 'height': 427, 'flickr_url': 'http://...e_z.jpg', 'width': 640}]
'info':{'date_created': '2017/09/01', 'year': 2017, 'url': 'http://cocodataset.org', 'contributor': 'COCO Consortium', 'version': '1.0', 'description': 'COCO 2017 Dataset'}
'liscense':[{'url': 'http://creativecommons.org/licenses/by-nc-sa/2.0/', 'id': 1, 'name': 'Attribution-NonCommercial-ShareAlike License'}]
```
The category and image id information is available <a href="https://github.com/sudo-install-MW/project-object-detection/blob/data-processing/coco_parser/utils/categories.txt">here</a>
## .json to yolo format conversion
