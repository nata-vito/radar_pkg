#!/usr/bin/env python2.7
from turtle import pu
import rospy
from stereo_msgs.msg import DisparityImage
from sensor_msgs.msg import CameraInfo, Image


rospy.init_node('ueye')
pub_disparity = rospy.Publisher('~disparity', DisparityImage, queue_size=10)
pub_left_info = rospy.Publisher('~left/camera_info', CameraInfo, queue_size=10)
pub_left_image = rospy.Publisher('~left/image_rect_color', Image, queue_size=10)
pub_right_info = rospy.Publisher('~right/camera_info', CameraInfo, queue_size=10)

def callback_left_info(data):

   pub_left_info.publish(data)


def callback_right_info(data):

    pub_right_info.publish(data)

def callback_disparity(data):
    
    pub_disparity.publish(data)
    #print("disparity")

def callback_left_image(data):
    """ image = Image()
    image.header.frame_id = 'velodyne'
    image.header.stamp = rospy.Time.now()
    print(' Width ')
    print(data.width)
    print('Height ') """
    pub_left_image.publish(data)
    print(data.encoding)
    
    
    


def talker():
    
    rospy.Subscriber('/zed2/zed_node/disparity/disparity_image', DisparityImage, callback_disparity)
    rospy.Subscriber('/zed2/zed_node/left/camera_info', CameraInfo, callback_left_info)
    rospy.Subscriber('/zed2/zed_node/right/camera_info', CameraInfo, callback_right_info) 
    rospy.Subscriber('/zed2/zed_node/left/image_rect_color', Image, callback_left_image)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass