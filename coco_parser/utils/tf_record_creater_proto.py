import tensorflow as tf
from object_detection.utils import dataset_util
import cv2
import os

def create_tf_example(tf_rec_dict):

    tf_example = tf.train.Example(features=tf.train.Features(feature={
      'image/height': dataset_util.int64_feature(tf_rec_dict['height']),
      'image/width': dataset_util.int64_feature(tf_rec_dict['width']),
      'image/filename': dataset_util.bytes_feature(tf_rec_dict['filename']),
      'image/source_id': dataset_util.bytes_feature(tf_rec_dict['filename']),
      'image/encoded': dataset_util.bytes_feature(tf_rec_dict['encoded_image_data']),
      'image/format': dataset_util.bytes_feature(tf_rec_dict['image_format']),
      'image/object/bbox/xmin': dataset_util.float_list_feature(tf_rec_dict['xmins']),
      'image/object/bbox/xmax': dataset_util.float_list_feature(tf_rec_dict['xmaxs']),
      'image/object/bbox/ymin': dataset_util.float_list_feature(tf_rec_dict['ymins']),
      'image/object/bbox/ymax': dataset_util.float_list_feature(tf_rec_dict['ymaxs']),
      'image/object/class/text': dataset_util.bytes_list_feature(tf_rec_dict['classes_text']),
      'image/object/class/label': dataset_util.int64_list_feature(tf_rec_dict['classes']),
    }))

    return tf_example


def create_tf_record(img_spec=None,img_anno=None, save_path=None, img_source_path=None,cat_dict=None):
    """
    creates tf_record
    :param img_spec: dictionary containing image specifications
    :param img_anno: dictionary containing image annotations
    :param save_path: path to save tfrecord file
    :param img_source_path: source path for the image
    :param cat_dict: dictionary containing category required for dataset extraction
    :return: None
    """
    writer = tf.python_io.TFRecordWriter(save_path)
    # iterate through every image in the dataset
    count = 0
    for images, annotations in img_anno.items():
        if count % 100 == 0:
            print("created tf record for {} images out of {} total images".format(count, len(img_anno.items())))
        # iterate over every bbox for each image if image has multiple bbox
        tf_rec_dict = dict()
        img_src_path = os.path.join(img_source_path, img_spec[images]['file_name'])

        with tf.gfile.GFile(img_src_path, 'rb') as fid:
            tf_rec_dict['encoded_image_data'] = fid.read()

        tf_rec_dict['xmins'] = []
        tf_rec_dict['ymins'] = []
        tf_rec_dict['xmaxs'] = []
        tf_rec_dict['ymaxs'] = []
        tf_rec_dict['height'] = img_spec[images]['height']  # Image height
        tf_rec_dict['width'] = img_spec[images]['width']  # Image width
        tf_rec_dict['image_format'] = 'jpeg'.encode()
        tf_rec_dict['filename'] = img_spec[images]['file_name'].encode() # Filename of the image. Empty if image is not from file
        tf_rec_dict['classes_text'] = []
        tf_rec_dict['classes'] = []

        for n_annotations in annotations:

            tf_rec_dict['xmins'].append(n_annotations['bbox'][0] / img_spec[images]['width'])
            tf_rec_dict['ymins'].append(n_annotations['bbox'][1] / img_spec[images]['height'])
            tf_rec_dict['xmaxs'].append((n_annotations['bbox'][0] + n_annotations['bbox'][2]) / img_spec[images]['width'])
            tf_rec_dict['ymaxs'].append((n_annotations['bbox'][1] + n_annotations['bbox'][3]) / img_spec[images]['height'])

            tf_rec_dict['classes_text'].append(cat_dict[n_annotations['category_id']].encode())
            tf_rec_dict['classes'].append(n_annotations['category_id'])

        #test_plot(img_src_path, tf_rec_dict)
        print(tf_rec_dict)
        tf_example = create_tf_example(tf_rec_dict)
        writer.write(tf_example.SerializeToString())
        count += 1

    writer.close()

def test_plot(img_src_path, tf_rec_dict):

    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


    img = cv2.imread(img_src_path)
    # test plot bbox
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'test',
                (int(tf_rec_dict['bbox'][0]), int(tf_rec_dict['bbox'][1])),
                font, 2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.rectangle(img, (int(tf_rec_dict['bbox'][0]), int(tf_rec_dict['bbox'][1])),
                  (int(tf_rec_dict['bbox'][0] + tf_rec_dict['bbox'][2]),
                   int(tf_rec_dict['bbox'][1] + tf_rec_dict['bbox'][3])), (255, 0, 0), 2)


    cv2.imshow(tf_rec_dict[''], img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()