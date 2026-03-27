def normalize_preferences(text: str) -> list[str]:
    if not text:
        return []
    return [t.strip() for t in text.lower().replace(" and ", ",").split(",")]

def build_user_profile(data: dict) -> dict:
    return {
        "origin": data.get("origin"),
        "destination": data.get("destination"),
        "budget": data.get("budget"),
        "preferences": normalize_preferences(data.get("preferences", "")),
        "season": data.get("season")
    }
