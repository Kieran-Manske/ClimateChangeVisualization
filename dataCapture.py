import requests
from bs4 import BeautifulSoup

url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

string = str(s)
dataByYear = []
lines = []
string.strip()



for letter in string:
    triplet = ""
    dataByYear.append(letter)

for character in dataByYear:
    if character.isnumeric() == False:
        dataByYear.pop(character)

print(dataByYear)