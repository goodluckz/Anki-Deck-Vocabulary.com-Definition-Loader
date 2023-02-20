import requests
import bs4
import genanki
import re
import anki_deck_model
import text_to_speech

"""
genanki allows you to programatically generate decks in Python 3 for Anki.
https://github.com/kerrickstaley/genanki
"""


if __name__ == "__main__":
    my_model = anki_deck_model.get_card_model_2()

    with open("style/style.css") as f:
        css = f.read()

    my_model.css = css

    my_deck = genanki.Deck(2059400110, title)

    for pack in word_list:
        word, definition, example = pack

        my_deck.add_note(
            genanki.Note(
                model=my_model,
                fields=[
                    word.upper(),
                    definition,
                    example,
                ],
            )
        )

    dirt = ["Vocabulary List", " ", "'", "-", ":", '"', ","]
    for d in dirt:
        title = title.replace(d, "")

    package = genanki.Package(my_deck)
    package.media_files = [r".\sound\\" + w[0] + ".mp3" for w in word_list]
    package.write_to_file(title + ".apkg")
    print("Deck has been created!")
