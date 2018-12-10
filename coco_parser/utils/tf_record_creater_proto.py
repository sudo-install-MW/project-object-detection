import tensorflow as tf
from object_detection.utils import dataset_util
import cv2
import os


def create_tf_example(tf_rec_dict):
    # TODO(user): Populate the following variables from your example.
    height = tf_rec_dict['height'] # Image height
    width = tf_rec_dict['width'] # Image width
    filename = tf_rec_dict['filename'] # Filename of the image. Empty if image is not from file
    encoded_image_data = tf_rec_dict['encoded_image_data'] # Encoded image bytes
    image_format = tf_rec_dict['image_format'] # b'jpeg' or b'png'
    classes_text = tf_rec_dict['classes_text']  # List of string class name of bounding box (1 per box)
    classes = tf_rec_dict['classes']  # List of integer class id of bounding box (1 per box)

    # bbox to rel logic goes here
    # TODO
    # END TODO
    print(tf_rec_dict)



    # xmins = [] # List of normalized left x coordinates in bounding box (1 per box)
    # xmaxs = [] # List of normalized right x coordinates in bounding box
    #          # (1 per box)
    # ymins = [] # List of normalized top y coordinates in bounding box (1 per box)
    # ymaxs = [] # List of normalized bottom y coordinates in bounding box
    #          # (1 per box)
    #
    #
    # tf_example = tf.train.Example(features=tf.train.Features(feature={
    #   'image/height': dataset_util.int64_feature(height),
    #   'image/width': dataset_util.int64_feature(width),
    #   'image/filename': dataset_util.bytes_feature(filename),
    #   'image/source_id': dataset_util.bytes_feature(filename),
    #   'image/encoded': dataset_util.bytes_feature(encoded_image_data),
    #   'image/format': dataset_util.bytes_feature(image_format),
    #   'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
    #   'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
    #   'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
    #   'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
    #   'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
    #   'image/object/class/label': dataset_util.int64_list_feature(classes),
    # }))

    tf_example = None

    return tf_example


def create_tf_record(img_spec=None,img_anno=None, save_path=None, img_source_path=None,cat_dict=None):

    #writer = tf.python_io.TFRecordWriter(save_path)
    # iterate through every image in the dataset
    for images, annotations in img_anno.items():
        # iterate over every bbox for each image if image has multiple bbox
        for n_annotations in annotations:
            tf_rec_dict = dict()
            img_src_path = os.path.join(img_source_path, img_spec[images]['file_name'])
            tf_rec_dict['encoded_image_data'] = cv2.imread(img_src_path)
            tf_rec_dict['height'] = img_spec[images]['height']  # Image height
            tf_rec_dict['width'] = img_spec[images]['width']  # Image width
            tf_rec_dict['filename'] = img_spec[images]['file_name']  # Filename of the image. Empty if image is not from file
            tf_rec_dict['image_format'] = 'jpeg'
            tf_rec_dict['bbox'] = n_annotations['bbox']
            tf_rec_dict['classes_text'] = cat_dict[n_annotations['category_id']]
            tf_rec_dict['classes'] = n_annotations['category_id']

            tf_example = create_tf_example(tf_rec_dict)
            #writer.write(tf_example.SerializeToString())

    #writer.close()

