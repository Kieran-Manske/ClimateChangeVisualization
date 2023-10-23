import requests
from bs4 import BeautifulSoup

url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
html = requests.get(url)
# print(html.text)

# s = BeautifulSoup(html.content, 'html.parser')

# raw = str(s)
# dataByYear = []
# lines = []

# for letter in raw:
#     dataByYear.append(letter)
#     if letter == "\n":
#         lines.append(dataByYear)
#         dataByYear = []

for line in html.text.split('\n'):
#     line = str(line)
    # print(line)
    print(line.split('\s+'))
    # for letter in line:
    #     if letter == " ":
    #         print(line.split('\s+'))




# for line in lines:
#     lines[lines.index(line)] = ''.join(line)

# lines = lines[5:]

# for i in range(len(lines)):
#     print(lines[i])