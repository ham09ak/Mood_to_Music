
from transformers import pipeline  # Hugging Face's high-level API for quick model usage
from PIL import Image              # For loading and handling image files



# -----------------------------
# Optional: Combined Multimodal Emotion (Text + Image)
# -----------------------------
# If you have both image and text (e.g., social media post), you can fuse them:
def combined_emotion_detection(image_path: str, text: str) -> str:
    """
    Optional: Combines emotion from image and text for more robust prediction.
    Simple majority or weighted fusion can be applied.
    """
    img_emotion = emotion_detection_image(image_path)
    txt_emotion = emotion_detection_text(text)
    
    # Simple rule: prioritize image if confident, fallback to text
    if "Error" not in img_emotion:
        return img_emotion  # Image usually more reliable for facial emotion
    return txt_emotion
