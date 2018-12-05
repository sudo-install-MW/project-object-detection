import json


class CocoTFRecordConverter:

    def __init__(self, cat_dict, anno_path):

        # TODO can you create tf_rec_img_dict with one dictionary?
        self.anno_dict = dict()
        self.img_spec = dict()
        self.tf_rec_img_dict = dict()
        self.cat_dict = cat_dict

        # open the .json file
        with open(anno_path) as json_file:
            json_file = json_file.read()
            self.data = json.loads(json_file)

    def dict_initializer(self):

        # loop creates a dictionary with image id as key and file_name and h, w as inner dict
        for image_spec in self.data['images']:
            buff_dict = dict()
            for key, value in image_spec.items():
                if key == 'file_name':
                    buff_dict['file_name'] = value
                if key == 'height':
                    buff_dict['height'] = value
                if key == 'width':
                    buff_dict['width'] = value

            self.img_spec[image_spec['id']] = buff_dict

        for anno in self.data['annotations']:
            # if annotations category id matches with what we want
            # add it to the annotation dictionary
            if anno['category_id'] in self.cat_dict:
                anno_buff_dict = dict()
                for key, value in anno.items():
                    if key == 'category_id':
                        anno_buff_dict['category_id'] = value
                    if key == 'bbox':
                        anno_buff_dict['bbox'] = value

                # if image has no entry of annotation
                if anno['image_id'] not in self.anno_dict:
                    self.anno_dict[anno['image_id']] = [anno_buff_dict]

                # if image has an annotation already
                else:
                    self.anno_dict[anno['image_id']].append(anno_buff_dict)

        return self.img_spec, self.anno_dict

    def absolute_bbox_converter(self):

        for images, annotations in self.anno_dict.items():
            abs_anno_list = []
            abs_anno_buff_dict = dict()

            # get image specs from self.img_spec
            file_name = self.img_spec[images]['file_name']
            img_height = self.img_spec[images]['height']
            img_width = self.img_spec[images]['width']

            # create the dictionary with absolute annotations
            for sub_annotations in annotations:
                x_max, y_max, x_min, y_min = sub_annotations['bbox']
                cat_id = sub_annotations['category_id']
                abs_bbox = [x_max/img_height, x_max/img_height, y_max/img_width, x_min/img_width]

                abs_anno_buff_dict['abs_bbox'] = abs_bbox
                abs_anno_buff_dict['category_id'] = cat_id

                abs_anno_list.append(abs_anno_buff_dict)

            self.tf_rec_img_dict[file_name] = abs_anno_list

        return self.tf_rec_img_dict