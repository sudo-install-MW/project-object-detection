import json


class CocoTFRecordConverter:
    """

    """
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