import psycopg2
import pprint
try:
    connection = psycopg2.connect(user = "201701247",
        password = "onlysanket",
        host = "10.100.71.21",
        port = "5432",
        database = "201701247");

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties

    # Print PostgreSQL version
    cursor.execute("set search_path to music");

    while(1):
        
        print("""
            0)Retrieve all the songs by a given Artist and given album name.
            1)Artist with max subscribers.
            2)Retrieve all the songs in a given playlist (playlistid = 1)
            3)Retrieve mutually liked artists between given users.
            4)Retrieve all the songs in all the playlist of your friend ( Two users are considered friend when both are following each other ).
            5)Retrieve Global top 10 Artist (Ranking is determined by the number of listeners).
            6)Number of songs by given Record Label
            7)Number of songs in all Genres
            8)The total number of songs in a genre produced by a given label
            9)Names of playlists of those premium users who are following the given artist.
            10)Most played song in a given genre
            11)Most active record label 
            12)Major age group in our database
            13)Most preferred language among users
            14)Sex Ratio
            15)Exit

        """)
        option = int(input("Enter: "));        
        queries = [
            "SELECT songname FROM artist NATURAL JOIN isinalbum NATURAL JOIN album NATURAL JOIN song WHERE (artistname = 'The Chainsmokers' AND albumname = 'World War Joy');",
            "SELECT artistName FROM (SELECT artistid, COUNT(username) AS subscribers FROM subscribesto GROUP BY artistid) AS r1 NATURAL JOIN artist ORDER BY subscribers DESC limit 1;",
            "SELECT songname FROM (SELECT * FROM isinplaylist WHERE (playlistid = 1)) AS r1 NATURAL JOIN Song;",
            "select artistname from (select artistid, count(username) from subscribesto where (username = 'kajju58' or username = 'Rach80') group by artistid) as r1 natural join artist where(count = 2);",
            "select songname from (select r1.follower as username from followedby as r1 join followedby as r2 on(r1.follower = r2.username) where (r1.username = 'Shivi_1899' and r1.username = r2.follower)) as r3 natural join playlist natural join isinplaylist natural join song;",
            "select artistname from artist where (ranking < 11) order by ranking;",
            "select label, count(songid) as numberOfSongs from songby where(label = 'Columbia') group by label;",
            "select sgenre, count(songid) as numberofsongs from genre group by sgenre order by numberofsongs desc;",
            "select sgenre, count(songid) from songby natural join genre where label = 'Disruptor' group by sgenre order by count desc;",
            "select playlistname from subscribesto natural join artist natural join users natural join playlist where (artistname = 'Ed Sheeran' and ispremium = true);",
            "select songid, songname, count(username) from genre natural join listenby natural join song where(sgenre = 'Pop') group by (songid, songname) order by count desc limit 1;",
            "select label, count(songid) from songby group by label order by count desc limit 1;",
            "select age, count(username) from users group by age order by count desc limit 1;",
            "select language, count(username) from preferredlanguages group by language order by count desc;",
            "select gender, count(username) from users group by gender;"
        ];
        if option < 15:
            cursor.execute(queries[option])
            record = cursor.fetchall()
            print(record)
        elif option==15:
            break
        else:
            print("Invalid")    

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
