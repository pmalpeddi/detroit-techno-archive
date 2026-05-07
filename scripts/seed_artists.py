import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_kevin_saunderson",
        "name": "Kevin Saunderson",
        "birth_name": "Kevin Maurice Saunderson",
        "born": "September 5, 1964",
        "origin": "Brooklyn, NY (raised in Belleville, MI)",
        "active_years": "1984 - present",
        "genres": ["Detroit Techno", "House", "Acid House", "Dance-Pop"],
        "aliases": ["Reese", "Reese Project", "Tronikhouse", "Kreem", "Essaray"],
        "associated_labels": ["KMS Records", "Metroplex", "Incognito Records", "Network Records"],
        "associated_acts": ["Inner City", "E-Dancer", "The Belleville Three"],
        "biography": "One third of the legendary Belleville Three alongside Juan Atkins and Derrick May. Known as The Elevator for bringing Detroit Techno to the mainstream. Founded KMS Records.",
        "notable_tracks": ["Big Fun", "Good Life", "Just Want Another Chance", "Velocity Funk"],
        "gear": ["Roland TR-909", "Roland TR-808", "Roland TR-727", "Yamaha DX100"],
        "image_url": ""
    },
    {
        "artist_id": "artist_juan_atkins",
        "name": "Juan Atkins",
        "birth_name": "Juan Atkins",
        "born": "September 12, 1962",
        "origin": "Detroit, MI",
        "active_years": "1980 - present",
        "genres": ["Detroit Techno", "Electronic"],
        "aliases": ["Model 500", "Infiniti", "Codename: Overlord"],
        "associated_labels": ["Metroplex", "Network Records"],
        "associated_acts": ["The Belleville Three", "Cybotron"],
        "biography": "The originator of Detroit Techno. Founded Metroplex Records in 1985, one of the first independent techno labels. His work as Model 500 defined the sound of Detroit Techno.",
        "notable_tracks": ["No UFOs", "Night Drive", "Berlin", "The Chase"],
        "gear": ["Roland TR-808", "Roland Juno-106", "Korg MS-20"],
        "image_url": ""
    },
    {
        "artist_id": "artist_derrick_may",
        "name": "Derrick May",
        "birth_name": "Derrick Bernard May",
        "born": "April 6, 1963",
        "origin": "Detroit, MI",
        "active_years": "1984 - present",
        "genres": ["Detroit Techno", "House"],
        "aliases": ["Rhythim Is Rhythim", "Mayday"],
        "associated_labels": ["Transmat", "KMS Records"],
        "associated_acts": ["The Belleville Three"],
        "biography": "One third of the Belleville Three. Founded Transmat Records. His track Strings of Life is widely considered one of the greatest electronic music records ever made.",
        "notable_tracks": ["Strings of Life", "Nude Photo", "It Is What It Is", "Kao-tic Harmony"],
        "gear": ["Roland TR-909", "Oberheim Xpander", "Roland Juno-106"],
        "image_url": ""
    }
]

def seed():
    for artist in artists:
        table.put_item(Item=artist)
        print(f"Seeded: {artist['name']}")
    print("Done!")

if __name__ == '__main__':
    seed()