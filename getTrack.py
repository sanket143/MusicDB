import requests;
import json; 

artist_id = "69GGBxA162lTqCwzJG5jLp";
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer BQDlSk3RWlBPGd_aHUGk7-uDYhuW64TYae26uBwamK2iYm0M4eJkwaQ94ltlVcA8XSTiLF2vdfubznLxzrXq_jI2uyz2Z1UgpU67Izz3-Wk30cS6OlfE1deFO1WP2r7bSDJOFm-B2purLd3fTVN1pAAoT9itnTs"
}

while(1):
    query = input("Search Track: ");
    print("Searching " + query + "...");
    r = requests.get("https://api.spotify.com/v1/search?q=" + query + "&type=track", headers=headers);

    tracks = json.loads(r.content)["tracks"]["items"];

    track = tracks[0];
    print(track["name"], track["duration_ms"]);
    artists = track["artists"];

    print("Artists:");
    for artist in artists:
        print(artist["name"]);

    print();
