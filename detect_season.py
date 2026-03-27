def detect_season(date_str: str) -> str:
    try:
        month = int(date_str.split("-")[1])
    except Exception:
        return "winter"

    if month in [3,4,5]:
        return "spring"
    elif month in [6,7,8]:
        return "summer"
    elif month in [9,10,11]:
        return "autumn"
    else:
        return "winter"
