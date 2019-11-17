import re;
import csv;
import datetime;
import requests;

from bs4 import BeautifulSoup;

songkeywordsq = open("songkeywords.sql", "w");

with open("Music DB - Songs.csv") as csv_file:
    line_count = 0;
    csv_reader = list(csv.reader(csv_file, delimiter=','));

    for row in csv_reader:
        if line_count == 0:
            line_count += 1;
        else:
            song = row[0];
            print(song);
            keys = song.split(" ");
            for key in keys:
                url = "https://www.thesaurus.com/misspelling?term=" + key;
                r = requests.get(url);
                soup = BeautifulSoup(r.content, 'html.parser');

                keywords = soup.findAll("a", {"class": ["css-gkae64", "etbu2a31"]});
                keywords = keywords[:3];

                for keyword in keywords:
                    word = keyword.get_text();
                    songkeywordsq_str = f"INSERT INTO songKeywords(songId, skeyword) VALUES ({line_count}, '{word}');\n"
                    songkeywordsq.write(songkeywordsq_str);
        line_count += 1;
