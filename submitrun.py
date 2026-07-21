import requests

API_URL = "https://www.speedrun.com/api/v1/runs"
API_KEY = "API KEY HERE"

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "run": {
        "category": "wdmjgwxd",
        "level": "d406qer9",
        "date": "2026-07-21",
        "platform": "8gej2n93",
        "verified": False,
        "times": {
            "realtime": 8},
        "emulated": False,
        "video": "VIDEO LINK",
        "comment": "DESCRIPTION",
        "variables": {
            "p85ygw0l": {
                "type": "pre-defined",
                "value": "le24xozl"
            },
            "5lyvgykl": {
                "type": "pre-defined",
                "value": "q8k09pkq"
            }
        }
    }
}

try:
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    print(f"Status Code: {response.status_code}")

    try:
        print(response.json())
    except ValueError:
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
