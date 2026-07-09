import requests

artists = [
    "Moodymann", "Theo Parrish", "Rick Wilhite", "Marcellus Pittman",
    "Kai Alcé", "Delano Smith", "DJ Godfather", "DJ Assault"
]

headers = {
    "User-Agent": "DetroitTechnoArchiveBot/1.0 (pranavmalpeddi@gmail.com) research-script"
}

for name in artists:
    resp = requests.get(
        "https://commons.wikimedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "list": "search",
            "srnamespace": 6,
            "srsearch": name,
            "srlimit": 3
        },
        headers=headers
    )

    if resp.status_code != 200:
        print(f"{name}: HTTP {resp.status_code} — {resp.text[:200]}")
        continue

    try:
        results = resp.json()["query"]["search"]
    except requests.exceptions.JSONDecodeError:
        print(f"{name}: non-JSON response — {resp.text[:200]}")
        continue

    if results:
        print(f"{name}: found {len(results)} candidate(s)")
        for r in results:
            print(f"  - {r['title']}")
    else:
        print(f"{name}: NOTHING on Commons — needs manual sourcing")
