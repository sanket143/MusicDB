import re;
import csv;
import datetime;
import random;

usersq = open("users.sql", "w");
preflangq = open("preflang.sql", "w");
followedbyq = open("followedby.sql", "w");

with open("Music DB - Users.csv") as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','));

    line_count = 0;

    for row in csv_reader:
        if line_count == 0:
            line_count += 1

        else:
            raw_date = row[7].split("-");
            join_date = datetime.datetime(int(raw_date[2]), int(raw_date[1]), int(raw_date[0])).strftime('%d/%m/%Y');
            usersq_str = f"INSERT INTO Users(username, password, firstname, lastname, email, gender, age, joindate, isPremium, profilePicUrl, country) VALUES ('{row[0]}', '{row[11]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}, TO_DATE('{join_date}', 'DD/MM/YYYY'), '{row[9].lower()}', '{row[10]}', '{row[6]}');\n";
            
            length = len(csv_reader);
            number_of_followers = random.randint(0, length - 2);
            followers = [];

            for i in range(number_of_followers):
                ind = random.randint(0, length - 2);
                follower = csv_reader[ind]
                if follower[0] not in followers:
                    followers.append(follower[0]);
                    followedbyq_str = f"INSERT INTO FollowedBy(username, follower) VALUES ('{row[0]}', '{follower[0]}');\n";
                    followedbyq.write(followedbyq_str);

            langs = row[8].split(',');
            for lang in langs:
                preflangq_str = f"INSERT INTO PreferredLanguages(username, language) VALUES ('{row[0]}', '{lang}');\n"
                preflangq.write(preflangq_str);

            usersq.write(usersq_str);

    usersq.close();
    preflangq.close();
    followedbyq.close();
    print("Done..");
