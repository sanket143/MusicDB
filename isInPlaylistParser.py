import re;
import csv;
import datetime;
import requests;
import random;

from bs4 import BeautifulSoup;

isinplaylistq = open("isinplaylist.sql", "w");

with open("Music DB - Songs.csv") as csv_file:
    songs = list(csv.reader(csv_file, delimiter=','));

print(songs);
with open("Music DB - Playlists.csv") as csv_file:
    playlists = list(csv.reader(csv_file, delimiter=','));
    playlistid = 1;
    for row in playlists:
        songs_in_playlist = random.randint(5, 16);
        current_playlist = [];

        for song in range(songs_in_playlist):
            songind = random.randint(0, len(songs) - 1);
            if songid not in current_playlist:
                isinplaylistq_str = f"INSERT INTO isInPlaylist(playlistid, songid) VALUES ({playlistid}, {songind});\n"
                isinplaylistq.write(isinplaylistq_str);
                current_playlist.append(songid);
        playlistid += 1;