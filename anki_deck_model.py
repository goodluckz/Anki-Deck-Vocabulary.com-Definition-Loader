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
    return genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Definition'},
            {'name': 'Synonym'},
            {'name': 'Antonym'},
            {'name': 'Sentence'},
            {'name': 'Part of Speech'},
            {'name': 'Transcript'},
            {'name': 'Source'},
            {'name': 'Picture'},
            {'name': 'Audio'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Term}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{definition}}<br><br>{{Example}}',
            },
        ])
