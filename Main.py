import requests
import urllib.request
import time
import bs4
import genanki


url = input("input list url: ")


response = requests.get(url)
print(response)
words = []
soup = bs4.BeautifulSoup(response.text, "html.parser")
for i, li in enumerate(soup.select('li')):
    words.append(li.text)

words = words[21:]
length = len(words)
list = [['','',''] for i in range(length)]
for i in range(length):
    if words[i] == "Play the Challenge":
      print("The list constains " + str(i) + " Words")
      break
    print(str(i + 1), words[i])
    list[i][0:2] = words[i].split('\n')[1:3]
    list[i][2] = ''.join(words[i].split('\n')[3:5])



my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Term'},
    {'name': 'definition'},
    {'name': 'Example'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Term}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{definition}}<br><br>{{Example}}',
    },
  ])

my_deck = genanki.Deck(2059400110,"unamed")

for i in list:
    my_deck.add_note(genanki.Note(
        model=my_model,
        fields=i))

genanki.Package(my_deck).write_to_file('output.apkg')


