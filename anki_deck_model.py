import genanki


def get_card_model():
    return genanki.Model(
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


def get_card_model_2():
    with open("style/front.html") as f:
        front = f.read()

    with open("style/back.html") as f:
        back = f.read()

    return genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Definition'},
            {'name': 'Sentence'},
            {'name': 'Synonym'},
            {'name': 'Antonym'},
            {'name': 'Part of Speech'},
            {'name': 'Transcription'},
            {'name': 'Source'},
            {'name': 'Picture'},
            {'name': 'Audio'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': front,

                'afmt': back,
            },
        ])
