# Import necessary libraries
from transformers import pipeline  # Hugging Face's high-level API for quick model usage

# -----------------------------
# Text Emotion Detection
# -----------------------------

# Load the emotion classification pipeline once (at startup) for efficiency
# Model: distilroberta fine-tuned on English emotion datasets
# Labels: anger, disgust, fear, joy, neutral, sadness, surprise
# This is much more accurate and robust than the older rule-based text2emotion library
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False  # We only need the top prediction
)

def emotion_detection_text(text: str) -> str:
    """
    Detects the dominant emotion from input text using a fine-tuned transformer model.
    
    Args:
        text (str): Input text (e.g., tweet, message, caption)
    
    Returns:
        str: Dominant emotion in lowercase (e.g., 'joy', 'anger', 'neutral')
    """
    # Handle empty or whitespace-only input
    if not text or not text.strip():
        return "neutral"
    
    # Run inference: returns a list with one dict -> [{'label': 'joy', 'score': 0.98}]
    result = emotion_pipeline(text)[0]
    
    # Extract the predicted label and convert to lowercase for consistency
    dominant_emotion = result['label'].lower()
    
    return dominant_emotion
