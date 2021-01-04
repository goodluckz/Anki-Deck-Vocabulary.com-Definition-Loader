import requests
import bs4
import genanki
import re

isGoodUrl = False
while not isGoodUrl:
    url = input("input list url: ")
    # url = "http://vocabulary.com/lists/236361"  # fixed url for testing
    pattern = re.compile('(https?://)?(www\\.)?vocabulary\\.com/lists/\\d{4,8}')
    match = re.match(pattern, url)
    boolean = bool(match)
    print(boolean)
    isGoodUrl = boolean

if not 'http' in url:
    url = 'http://' + url

response = requests.get(url)
print(response)
if response.status_code == 200:
    words = []
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    title = soup.select('title')[0].text
    title = title.replace(" : Vocabulary.com", "")  # remove suffix
    print('Title of list: ' + title)
    for i, li in enumerate(soup.select('li')):
        words.append(li.text)

    lastIndex = words.index('Play the Challenge')
    words = words[21: lastIndex]
    length = len(words)
    list = [['','',''] for i in range(length)]
    for i in range(length):
        list[i][0:2] = words[i].split('\n')[1:3]
        list[i][2] = ''.join(words[i].split('\n')[4:6])



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

    my_deck = genanki.Deck(2059400110, title)

    for i in list:
        my_deck.add_note(genanki.Note(
            model=my_model,
            fields=i))
    title = title.replace("Vocabulary List", "")
    title = title.replace(" ", "")
    title = title.replace("'", "")
    title = title.replace("-", "")
    title = title.replace(":", "")

    genanki.Package(my_deck).write_to_file(title+'.apkg')


