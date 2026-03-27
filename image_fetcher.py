import requests

def fetch_image(query: str) -> str:
    """
    Simulated image fetcher (Unsplash-style)
    """
    return f"https://via.placeholder.com/400x300?text={query.replace(' ', '+')}"
