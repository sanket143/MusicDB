import re;
import csv;
import datetime;
import requests;
import random;

from bs4 import BeautifulSoup;

listenbyq = open("listenby.sql", "w");

with open("Music DB - Users.csv") as csv_file:
    users = list(csv.reader(csv_file, delimiter=','));

with open("Music DB - Songs.csv") as csv_file:
    songs = list(csv.reader(csv_file, delimiter=','));
    songid = 1;

    listenedBy = [];
    for row in songs:
        user_len = random.randint(5, 16);

        for i in range(user_len):
            uid = random.randint(1, len(users) - 1);
            if uid not in listenedBy:
                listenbyq_str = f"INSERT INTO listenby(songid, username) VALUES ({songid}, '{users[uid][0]}');\n"
                listenbyq.write(listenbyq_str);
                listenedBy.append(uid);
        songid += 1;