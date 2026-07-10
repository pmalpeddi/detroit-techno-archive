import requests
import time
import os
import argparse

DISCOGS_TOKEN = os.environ.get("DISCOGS_TOKEN", "")

headers = {
    "User-Agent": "DetroitTechnoArchiveBot/1.0 (pranavmalpeddi@gmail.com) research-script"
}

def check_commons(name):
    resp = requests.get(
        "https://commons.wikimedia.org/w/api.php",
        params={
            "action": "query", "format": "json", "list": "search",
            "srnamespace": 6, "srsearch": name, "srlimit": 3
        },
        headers=headers
    )
    if resp.status_code != 200:
        return None, f"HTTP {resp.status_code} — {resp.text[:200]}"
    try:
        return resp.json()["query"]["search"], None
    except requests.exceptions.JSONDecodeError:
        return None, f"non-JSON response — {resp.text[:200]}"

def check_discogs(name, entity_type="artist"):
    if not DISCOGS_TOKEN:
        return None
    resp = requests.get(
        "https://api.discogs.com/database/search",
        params={"q": name, "type": entity_type, "token": DISCOGS_TOKEN},
        headers=headers
    )
    try:
        return resp.json().get("results", [])
    except Exception:
        return []

def check_musicbrainz_release(artist, title):
    resp = requests.get(
        "https://musicbrainz.org/ws/2/release/",
        params={"query": f'artist:"{artist}" AND release:"{title}"', "fmt": "json"},
        headers=headers
    )
    try:
        releases = resp.json().get("releases", [])
        if releases:
            mbid = releases[0]["id"]
            cover_url = f"https://coverartarchive.org/release/{mbid}/front"
            if requests.head(cover_url).status_code == 200:
                return cover_url
        return None
    except Exception:
        return None

def search_entity(name, entity_type):
    print(f"\n{name}:")
    results, error = check_commons(name)
    if error:
        print(f"  Commons: {error}")
    elif results:
        print(f"  Commons: found {len(results)} candidate(s)")
        for r in results:
            print(f"    - {r['title']}")
    else:
        print("  Commons: NOTHING")

    discogs = check_discogs(name, entity_type)
    if discogs is None:
        print("  Discogs: skipped (no DISCOGS_TOKEN set)")
    elif discogs:
        top = discogs[0]
        print(f"  Discogs: found — {top.get('title')} (id: {top.get('id')})")
        print(f"    Profile: https://www.discogs.com/{entity_type}/{top.get('id')}")
        img = top.get("cover_image") or top.get("thumb")
        if img and "spacer.gif" not in img:
            print(f"    Image:   {img}")
        else:
            print("    Image:   none available in search result")
    else:
        print("  Discogs: none")

    time.sleep(1.5)

def search_release(artist, title):
    print(f"\n{artist} — {title}:")

    cover = check_musicbrainz_release(artist, title)
    print(f"  MusicBrainz/CAA: {cover}" if cover else "  MusicBrainz/CAA: not found")

    discogs = check_discogs(f"{artist} {title}", "release")
    if discogs is None:
        print("  Discogs: skipped (no DISCOGS_TOKEN set)")
    elif discogs:
        top = discogs[0]
        print(f"  Discogs: found — {top.get('title')} (id: {top.get('id')})")
        print(f"    Profile: https://www.discogs.com/release/{top.get('id')}")
        img = top.get("cover_image") or top.get("thumb")
        if img and "spacer.gif" not in img:
            print(f"    Image:   {img}")
        else:
            print("    Image:   none available in search result")
    else:
        print("  Discogs: none")

    time.sleep(1.5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check Commons/Discogs/MusicBrainz for existing images before manual sourcing."
    )
    parser.add_argument("names", nargs="*", help="Artist or label names to search")
    parser.add_argument("--type", choices=["artist", "label"], default="artist",
                         help="Entity type for Discogs search (default: artist)")
    parser.add_argument("--release", nargs=2, metavar=("ARTIST", "TITLE"),
                         action="append", default=[],
                         help='Check a release, e.g. --release "Moodymann" "Forevernevermore" (repeatable)')
    args = parser.parse_args()

    if args.names:
        print(f"=== {args.type.upper()}S ===")
        for name in args.names:
            search_entity(name, args.type)

    if args.release:
        print("\n=== RELEASES ===")
        for artist, title in args.release:
            search_release(artist, title)

    if not args.names and not args.release:
        parser.print_help()
