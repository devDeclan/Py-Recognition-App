import cv2
import imutils
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array

CLASSES = [
	"Archery",
	"BalanceBeam",
	"BaseballPitch",
	"Basketball",
	"Biking",
	"Bowling",
	"BoxingPunchingBag",
	"BoxingSpeedBag",
	"BreastStroke",
	"CliffDiving",
	"CricketBowling",
	"CricketShot",
	"Diving",
	"Fencing",
	"FieldHockeyPenalty",
	"GolfSwing",
	"HammerThrow",
	"HighJump",
	"HorseRace",
	"IceDancing",
	"JavelinThrow",
	"JugglingBalls",
	"JumpRope",
	"Kayaking",
	"LongJump",
	"Lunges",
	"ParallelBars",
	"PoleVault",
	"Rafting",
	"Rowing",
	"Shotput",
	"SkateBoarding",
	"Skiing",
	"SkyDiving",
	"SoccerJuggling",
	"SoccerPenalty",
	"Surfing",
	"TableTennisShot",
	"TennisSwing",
	"VolleyballSpiking",
]
class VideoReader(object):
  def __init__(self, filename=0):
    self.video = cv2.VideoCapture(filename)
    json_file = open("/home/declvn/Desktop/projects/Py-Recognition-App/recognition/model/model.json", "r")
    loaded_json_file = json_file.read()
    json_file.close()
    self.model = keras.models.model_from_json(loaded_json_file)

  def __del__(self):
    self.video.release()

  def get_frame(self):
    success,frame = self.video.read()
    output_frame = frame.copy()
    filename = "/home/declvn/Desktop/projects/Py-Recognition-App/recognition/temp/frame.jpg"
    cv2.imwrite(filename, frame)
    img = load_img(filename, target_size = (128, 128))
    img = img_to_array(frame)
    img = np.expand_dims(img, axis=0)
    prediction = np.argmax(self.model.predict(img), axis=-1)
    label= "activity: {}".format(CLASSES[prediction[0]])
    output_frame = imutils.resize(output_frame, width=600)
    cv2.rectangle(output_frame, (0, 0), (250, 30), (255, 255, 255), -1)
    cv2.putText(output_frame, label, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_4)
    success,jpeg_frame = cv2.imencode('.jpg',output_frame)
    return jpeg_frame.tobytes()