#!/usr/bin/env python2.7
import rospy
from radar_OHW_pkg.msg import RadarData, RadarDataArray, VehicleData,VehicleArray
from visualization_msgs.msg import Marker, MarkerArray
from radar_msgs.msg import RadarDetectionArray, RadarDetection

rospy.init_node('radar_converter')
pub_radar = rospy.Publisher('~detections', RadarDetectionArray, queue_size=10)

def convert_data(detections):
    detect = RadarDetection()
    detectArray = RadarDetectionArray()
    detectArray.header.frame_id = "velodyne"
    for detection in detections.radarDatas:
        detect = RadarDetection()
        detect.detection_id = detection.id
        detect.position.x = detection.dx
        detect.position.y = detection.dy
        detect.velocity.x = detection.vx
        detect.velocity.y = detection.vy
        detect.amplitude = detection.rcs
        detectArray.detections.append(detect)

    return detectArray


def callback_radar(data):
    global pub_radar
    arrayDetections = convert_data(data)
    #rospy.loginfo(arrayMarker)
    pub_radar.publish(arrayDetections)

def talker():
    
    rospy.Subscriber('/radar_OHW_publisher/radar_msgs', RadarDataArray, callback_radar)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass