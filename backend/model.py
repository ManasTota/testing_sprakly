from transformers import pipeline

# Use Helsinki-NLP model
swedish_to_english = pipeline("translation_sv_to_en", model="Helsinki-NLP/opus-mt-sv-en")
english_to_swedish = pipeline("translation_en_to_sv", model="Helsinki-NLP/opus-mt-en-sv")

def translate(text, direction="sv-en"):
    if direction == "sv-en":
        return swedish_to_english(text)[0]["translation_text"]
    elif direction == "en-sv":
        return english_to_swedish(text)[0]["translation_text"]
    else:
        return "Invalid direction"
