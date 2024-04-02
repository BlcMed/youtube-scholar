from langdetect import detect


def detect_language_from_text(text):
    try:
        detected_language = detect(text)
        return detected_language
    except:
        # Handle exceptions if language detection fails
        return None


# Detect accent for a playlist with ML (help in filtering the playlists based on personal prefrences)
def detect_language_from_audio():
    pass
