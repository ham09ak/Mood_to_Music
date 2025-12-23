import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
sp= spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='4842612bd3c64d5786467aaefafef870',
            client_secret='61548d789e6f4cc3a46e6edddc2ea46f',
            redirect_uri='https://localhost:8888/callback',
            scope="user-library-read" #read the user saved tracks
            ))
# Emotion to target audio features mapping (based on Valence-Arousal model)
EMOTION_TO_FEATURES = {
    'happy':     {'target_valence': 0.8, 'target_energy': 0.7, 'target_danceability': 0.7},
    'joy':       {'target_valence': 0.9, 'target_energy': 0.8, 'target_danceability': 0.8},  # If your model outputs 'joy'
    'sad':       {'target_valence': 0.2, 'target_energy': 0.3, 'target_danceability': 0.3},
    'angry':     {'target_valence': 0.3, 'target_energy': 0.9, 'target_danceability': 0.6},
    'fear':      {'target_valence': 0.3, 'target_energy': 0.5, 'target_acousticness': 0.7},  # Darker/ambient
    'surprise':  {'target_valence': 0.7, 'target_energy': 0.9, 'target_danceability': 0.8},
    'excited':   {'target_valence': 0.8, 'target_energy': 0.9, 'target_danceability': 0.8},
    'neutral':   {'target_valence': 0.5, 'target_energy': 0.4, 'target_acousticness': 0.6},
    'disgust':   {'target_valence': 0.2, 'target_energy': 0.8},  # Intense like angry
}

# Optional fallback genres (valid Spotify seeds)
EMOTION_TO_GENRES = {
    'happy': ['pop', 'dance-pop'],
    'sad': ['sad', 'acoustic', 'blues'],
    'angry': ['rock', 'metal', 'punk'],
    'fear': ['ambient', 'classical', 'soundtrack'],
    'surprise': ['electronic', 'edm'],
    'excited': ['house', 'techno'],
    'neutral': ['chill', 'jazz', 'indie'],
    'disgust': ['hardcore', 'grindcore', 'death-metal'],
}

def get_the_music(emotion: str, limit: int = 20):
    """
    Get music recommendations based on detected emotion using audio features (primary) + genres (fallback).
    """
    try:
        features = EMOTION_TO_FEATURES.get(emotion.lower(), EMOTION_TO_FEATURES['neutral'])
        genres = EMOTION_TO_GENRES.get(emotion.lower(), EMOTION_TO_GENRES['neutral'])

        # Primary: Use target audio features for precise mood matching
        recommendations = sp.recommendations(
            seed_genres=genres[:2],  # Up to 5 allowed, but 2 is fine
            limit=limit,
            **features  # Unpack targets like target_valence=0.8
        )
        return recommendations['tracks']
    
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return None

def display_recommendations(tracks):
    if not tracks:
        print("No recommendations available.")
        return
    
    print("\nRecommended Tracks:")
    for i, track in enumerate(tracks, 1):
        artists = ", ".join([artist['name'] for artist in track['artists']])
        print(f"{i}. {track['name']} by {artists}")
        print(f"   Album: {track['album']['name']}")
        print(f"   Listen: {track['external_urls']['spotify']}\n")
