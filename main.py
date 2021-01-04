import requests
import bs4
import genanki
import re

again = True
txt = "Welcome, to create an Anki Vocabulary deck please select a deck from vocabulary.com"\
      "\nGo to the page that contains the vocab list and copy the URL of that page."\
    "\nIt should look like this http://vocabulary.com/lists/236361"
print(txt)

while again:
    isGoodUrl = False
    while not isGoodUrl:
        url = input("Input list URL: ")
        # url = "http://vocabulary.com/lists/236361"  # fixed url for testing
        pattern = re.compile('(https?://)?(www\\.)?vocabulary\\.com/lists/\\d{4,8}')
        match = re.match(pattern, url)
        boolean = bool(match)
        if boolean:
            print("Is valid URL")
        isGoodUrl = boolean

    if not 'http' in url:
        url = 'http://' + url

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        print("Processing Wordlist!")
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
        print("Deck has been created!")

    answer = input("Do you want to create another deck? y/n ").lower()
    if answer != "y" and answer != "yes":
        again = False

    print("\n\n###########################\n\n")


