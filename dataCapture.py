import requests
from bs4 import BeautifulSoup

url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

raw = str(s)
dataByYear = []
lines = []




for letter in raw:
    dataByYear.append(letter)
    if letter == "\n":
        lines.append(dataByYear)
        dataByYear = []

for line in lines:
    for letter in line:
        if letter == " ":
            line.remove(letter)

for line in lines:
    lines[lines.index(line)] = ''.join(line)

#remove line 1-4 from lines
lines = lines[5:]

for i in range(len(lines)):
    print(lines[i])