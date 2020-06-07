import cv2
import imutils
import tensorflow as tf

class VideoReader(object):
  def __init__(self, filename=0):
  	self.video = cv2.VideoCapture(filename)
  	self.model = tf.keras.models.load_model("/tmp/model")

  def __del__(self):
    self.video.release()

  def get_frame(self):
  	success,frame = self.video.read()
  	frame = imutils.resize(frame, width=600)
  	output_frame = frame.copy()
  	# manipulate frame in here


  	# after return output
  	label= "activity: {}".format("GENGING")
  	cv2.rectangle(output_frame, (0, 0), (250, 30), (255, 255, 255), -1)
  	cv2.putText(output_frame, 'GENGING', (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_4)
  	success,jpeg_frame = cv2.imencode('.jpg',output_frame)
  	return jpeg_frame.tobytes()