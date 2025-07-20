import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
sp= spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='4842612bd3c64d5786467aaefafef870',
            client_secret='61548d789e6f4cc3a46e6edddc2ea46f',
            redirect_uri='https://localhost:8888/callback',
            scope="user-library-read" #read the user saved tracks
            ))
EMOTION_TO_GENRE = {
    'happy': ['pop', 'dance', 'upbeat'],
    'sad': ['blues', 'acoustic', 'soul'],
    'angry': ['rock', 'metal', 'punk'],
    'surprise': ['electronic', 'edm', 'experimental'],
    'fear': ['ambient', 'classical', 'soundtrack'],
    'neutral': ['jazz', 'chill', 'indie'],
    'excited': ['house', 'techno', 'trance'],
    'disgust': ['heavy-metal', 'hardcore', 'grunge']
}
def get_the_music(emotions):
  try:
    seed_genres=EMOTION_TO_GENRE.get(emotions, EMOTION_TO_GENRE['neutral'])
    #get recommendations
    recommendations=sp.recommendations(seed_genres=seed_genres[:2]) #use the first 2 geners
    return recommendations['tracks']
  except Exception as e:
    print(f"cant get the spotify recommendations; {e}")
    return None
def display_recommendations(tracks):
  if not tracks:
    print("No recommendations is available.")
    return
  print("\nRecommended Tracks:")
  for i, track in enumerate(tracks, 1):
    artists=", ".join([artist['name'] for artist in track['artists']])
    print(f"{i}. {track['name']} by {artists}")
    print(f"   Listen: {track['external_urls']['spotify']}")
    print(f"   Album: {track['album']['name']}\n")
