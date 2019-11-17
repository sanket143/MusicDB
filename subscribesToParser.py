import re;
import csv;
import datetime;
import requests;
import random;

from bs4 import BeautifulSoup;

subscribestoq = open("subscribesto.sql", "w");


with open("Music DB - Users.csv") as csv_file:
    users = list(csv.reader(csv_file, delimiter=','));


with open("Music DB - Songs.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0;
    artist_count = 1;
    genre_count = 1;
    album_count = 1;

    artists = [];
    albums = {};

    for row in csv_reader:
        if line_count == 0:
            line_count += 1

        else:
            artist_list = row[1].split(", ");
            genre_list = row[4].split(", ");

            for artist in artist_list:
                if artist not in artists:
                    uss = [];
                    
                    user_len = random.randint(0, len(users) - 1);
                    for i in range(user_len):
                        uid = random.randint(1, len(users) - 1);
                        if uid not in uss:
                            subscribestoq_str = f"INSERT INTO subscribesTo(username, artistId) VALUES ('{users[uid][0]}', {artist_count});\n"
                            subscribestoq.write(subscribestoq_str);
                            uss.append(uid);
                    artists.append(artist);
                    artist_count += 1;