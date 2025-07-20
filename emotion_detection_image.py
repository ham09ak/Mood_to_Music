from deepface import DeepFace
def emotion_detection_image(image_path):
  try:
     emotions=DeepFace.analyze(image_path,actions=['emotion'], enforce_detection=False) # analyze methode detect emotions , age, gender, race
     #  enforce_detection=False allows to continue even if no face is detected
     return emotions[0]['dominant_emotion'] # return the dominant emotions
  except Exception as e:
    return f"Error: {str(e)}"
