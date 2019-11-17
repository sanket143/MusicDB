import csv;
import requests;
from bs4 import BeautifulSoup;

playlistkeywordsq = open("playlistkeywords.sql", "w");
playlistq = open("playlist.sql", "w");

with open("Music DB - Playlists.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    playlist_count = 1;

    for row in csv_reader:
        playlist = row[0];
        playkeys = playlist.split(" ");

        print(playlist);
        for keys in playkeys:
            url = "https://www.thesaurus.com/misspelling?term=" + keys;
            r = requests.get(url);

            soup = BeautifulSoup(r.content, 'html.parser');

            keywords = soup.findAll("a", {"class": ["css-gkae64", "etbu2a31"]});
            keywords = keywords[:3];



            for keyword in keywords:
                word = keyword.get_text();
                playlistkeywordsq_str = f"INSERT INTO PlaylistKeywords(playlistId, pkeyword) VALUES ({playlist_count}, '{word}');\n"
                playlistkeywordsq.write(playlistkeywordsq_str);

        playlistq_str = f"INSERT INTO Playlist(playlistId, username, playlistName, createdOn) VALUES ({playlist_count}, '{row[1]}', '{row[0]}', TO_DATE('{row[2]}', 'MM/DD/YYYY'));\n"
        playlistq.write(playlistq_str);
        playlist_count += 1;

    playlistq.close();
    playlistkeywordsq.close();