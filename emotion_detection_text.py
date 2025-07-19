def emotion_detection_text(text):
  emotions=te.get_emotion(text)
  if not emotions:
    return "neutral" # if no emotion detected
  return max(emotions, key=emotions.get) # return the emotions with the highset score and use emotions.get to compare values
