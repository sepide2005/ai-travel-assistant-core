from detect_season import detect_season

def classify_message(message: str) -> str:
    message = message.lower()
    if "plan" in message or "trip" in message:
        return "plan"
    elif "hotel" in message or "food" in message:
        return "general"
    return "irrelevant"

def generate_response(message: str, history: list[str]) -> str:
    category = classify_message(message)

    if category == "plan":
        return "Here is a travel plan based on your preferences."

    elif category == "general":
        return "Here are some travel tips and recommendations."

    return "Sorry, I can only help with travel-related questions."
