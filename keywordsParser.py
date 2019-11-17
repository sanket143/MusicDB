import re;
import csv;
import datetime;

albumkeywordq = open("albumkeyword.sql", "w");

csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0;

for row in csv_reader:
    if line_count == 0:
        line_count += 1

    else:
        raw_date = row[7].split("-");
        join_date = datetime.datetime(int(raw_date[2]), int(raw_date[1]), int(raw_date[0])).strftime('%d/%m/%Y');
        usersq_str = f"INSERT INTO Users(username, password, firstname, lastname, email, gender, age, joindate, isPremium, profilePicUrl) VALUES ('{row[0]}', '{row[11]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', {row[5]}, TO_DATE('{join_date}', 'DD/MM/YYYY'), '{row[9].lower()}', '{row[10]}');\n";

        langs = row[8].split(',');
        for lang in langs:
            preflangq_str = f"INSERT INTO PreferredLanguages(username, language) VALUES ('{row[0]}', '{lang}');\n"
            preflangq.write(preflangq_str);

        usersq.write(usersq_str);

usersq.close();
preflangq.close();
print("Done..");
