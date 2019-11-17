import re;
import csv;
import datetime;
import requests;

from bs4 import BeautifulSoup;

with open("Music DB - Songs.csv") as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','))


    for row in csv_reader:
        row
