def detect_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"


# Example usage
if __name__ == "__main__":
    user_month = int(input("Enter month (1-12): "))
    season = detect_season(user_month)
    print(f"Season: {season}")
