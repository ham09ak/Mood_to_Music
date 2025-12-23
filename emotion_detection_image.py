# Import necessary libraries
from transformers import pipeline  # Hugging Face's high-level API for quick model usage
from PIL import Image              # For loading and handling image files

# -----------------------------
# Image Emotion Detection (Multimodal LLM Approach)
# -----------------------------

# Load a vision-language model (VLM) pipeline
# Example uses LLaVA-1.5 (7B) – a strong open-source multimodal model
# You can replace with newer/better models like llava-hf/llava-v1.6-mistral-7b-hf,
# microsoft/Phi-3.5-vision-instruct, or moondream2 for faster local inference
vlm_pipeline = pipeline(
    "image-to-text", 
    model="llava-hf/llava-1.5-7b-hf",  # Change to a more recent/faster model if needed
    max_new_tokens=50                 # Limit response length for speed and clarity
)

def emotion_detection_image(image_path: str) -> str:
    """
    Detects the dominant facial emotion from an image using a vision-language model.
    
    Args:
        image_path (str): Path to the image file (local path or URL if supported)
    
    Returns:
        str: Dominant emotion (e.g., 'happy', 'sad', 'angry', 'neutral')
             Returns error message if processing fails
    """
    try:
        # Open and load the image using PIL
        image = Image.open(image_path).convert("RGB")
        
        # Structured prompt to guide the model toward accurate emotion classification
        # Restricting output to specific emotions improves consistency and parsing
        prompt = (
            "USER: <image>\n"
            "Analyze the person's facial expression in this image. "
            "Respond with only one word: the dominant emotion from this list: "
            "angry, disgust, fear, happy, sad, surprise, neutral.\n"
            "ASSISTANT:"
        )
        
        # Generate response from the VLM
        output = vlm_pipeline(image, prompt=prompt)[0]['generated_text']
        
        # Extract the last meaningful word (the model's predicted emotion)
        # The model follows instructions and usually ends with the emotion word
        words = output.strip().split()
        predicted_emotion = words[-1].lower() if words else "neutral"
        
        # Optional: Validate against known emotions (fallback to neutral)
        valid_emotions = {"angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"}
        if predicted_emotion not in valid_emotions:
            return "neutral"
        
        return predicted_emotion
    
    except Exception as e:
        # Return error message instead of raising exception (matches your original style)
        return f"Error: {str(e)}"
