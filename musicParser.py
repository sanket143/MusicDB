import re;
import csv;
import datetime;
import requests;

from bs4 import BeautifulSoup;

songq = open("song.sql", "w");
artistq = open("artist.sql", "w");
songbyq = open("songby.sql", "w");
genreq = open("genre.sql", "w");
albumq = open("album.sql", "w");
isinalbumq = open("isinalbum.sql", "w");
songkeywordsq = open("songkeywords.sql", "w");
albumkeywordsq = open("albumkeywords.sql", "w");
artistkeywordsq = open("artistkeywords.sql", "w");

with open("Music DB - Songs.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0;
    artist_count = 1;
    genre_count = 1;
    album_count = 1;

    artists = {};
    albums = {};

    for row in csv_reader:
        if line_count == 0:
            line_count += 1

        else:
            song_name = row[0].replace('\'', "''");
            songq_str = f"INSERT INTO Song(songId, songName, duration, language) VALUES ({line_count}, '{song_name}', {row[6]}, '{row[7]}');\n";


            artist_list = row[1].split(", ");
            genre_list = row[4].split(", ");
            album = row[5];

            print(song_name, "by", ", ".join(artist_list));

            release_date = datetime.datetime.strptime(row[3], '%B %d, %Y').strftime('%d/%m/%Y');

            if album in albums:
                albums[album]["numberofsongs"] += 1;

            else:
                albums[album] = {
                    "albumid": album_count,
                    "numberofsongs": 1,
                    "name": album.replace('\'', "''"),
                    "release_date": release_date
                }
                album_keys = album.split(" ");
                key = album_keys[0];
                url = "https://www.thesaurus.com/misspelling?term=" + key;
                r = requests.get(url);
                soup = BeautifulSoup(r.content, 'html.parser');

                keywords = soup.findAll("a", {"class": ["css-gkae64", "etbu2a31"]});
                keywords = keywords[:3];
                for keyword in keywords:
                    word = keyword.get_text();
                    albumkeywordsq_str = f"INSERT INTO AlbumKeywords(albumId, akeyword) VALUES ({album_count}, '{word}');\n"
                    albumkeywordsq.write(albumkeywordsq_str);


                album_count += 1;

            for artist in artist_list:
                if artist not in artists:
                    r = requests.get("https://genius.com/artists/" + artist.replace(" ", "-"));
                    soup = BeautifulSoup(r.content, 'html.parser');
                    try:
                        bios = soup.findAll("div", {"class": "rich_text_formatting"});
                        bio = bios[0].get_text().strip().replace("'", "''");
                    except:
                        bio = "";
                    
                    keywords = artist.split(" ");
                    artists[artist] = artist_count;
                    artistq_str = f"INSERT INTO Artist(artistId, artistName, briefBio, ranking) VALUES ({artist_count}, '{artist}', '{bio}', {artist_count});\n";
                    for word in keywords:
                        artistkeywordsq_str = f"INSERT INTO ArtistKeywords(artistId, akeyword) VALUES ({artist_count}, '{word}');\n"
                        artistkeywordsq.write(artistkeywordsq_str);

                    artistq.write(artistq_str);
                    artist_count += 1;

                labels = row[2].split(", ");
                songbyq_str = f"INSERT INTO SongBy(songId, artistId, label, releaseDate) VALUES ({line_count}, '{artists[artist]}', '{labels[0]}', TO_DATE(\'{release_date}\', 'DD/MM/YYYY'));\n";
                
                songbyq.write(songbyq_str);

                isinalbumq_str = f"INSERT INTO isInAlbum(songId, artistId, albumId) VALUES ({line_count}, {artists[artist]}, {albums[album]['albumid']});\n";
                isinalbumq.write(isinalbumq_str);

            for genre in genre_list:
                genreq_str = f"INSERT INTO Genre(songId, sgenre) VALUES ({line_count}, '{genre}');\n";
                genreq.write(genreq_str);

            songq.write(songq_str);
            line_count += 1;

    for album in albums:
        albumq_str = f"INSERT INTO Album(albumId, albumName, numberOfSongs, releaseDate) VALUES ({albums[album]['albumid']}, '{albums[album]['name']}', {albums[album]['numberofsongs']}, TO_DATE('{albums[album]['release_date']}', 'DD/MM/YYY'));\n";
        albumq.write(albumq_str);

    songq.close();
    artistq.close();
    songbyq.close();
    genreq.close();
    albumq.close();
    artistq.close();
    print("Done..");
