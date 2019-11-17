import csv;
import json;
import requests;
from bs4 import BeautifulSoup;

api_key = "BQDlSk3RWlBPGd_aHUGk7-uDYhuW64TYae26uBwamK2iYm0M4eJkwaQ94ltlVcA8XSTiLF2vdfubznLxzrXq_jI2uyz2Z1UgpU67Izz3-Wk30cS6OlfE1deFO1WP2r7bSDJOFm-B2purLd3fTVN1pAAoT9itnTs";
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

songsData = [];

with open("Music DB - Songs.csv", "r") as readFile:
    reader = csv.reader(readFile);
    songsData = list(reader);
    for i in range(len(songsData)):
        if i == 0:
            continue;
        row = songsData[i];
        song = row[0];
        artist = row[1].split(" ");
        query = song;
        r = requests.get("https://api.spotify.com/v1/search?q=" + query + "&type=track", headers=headers);

        songsData[i][0] = songsData[i][0].strip();
        try:
            tracks = json.loads(r.content)["tracks"]["items"];
            track = tracks[0];
            if len(songsData[i][6].strip()) == 0:
                songsData[i][6] = track["duration_ms"];
        except:
            songsData[i][6] = '0';
        
        print(songsData[i]);

with open("Updated SongsDB.csv", "w") as writeFile:
    writer = csv.writer(writeFile);
    for row in songsData:
        print(row);
        writer.writerow(row);

readFile.close();    
writeFile.close();
