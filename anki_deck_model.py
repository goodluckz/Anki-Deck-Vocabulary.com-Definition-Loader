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
                'qfmt': '<div class="header">\n'
                '<span class="word">{{Word}}</span>\n'
                '</div>\n'
                
                '<div class="header">\n'
                '<span class="transcription">{{Transcription}}</span>\n'
                '<span class="part-of-speech">{{Part of Speech}}</span>\n'
                '</div>\n'
                '<span class="audio">{{Audio}}</span>\n',

                'afmt': '{{FrontSide}}\n'
                
                '<hr id="answer">\n'
                '<div class="sub-header">\n'
                '<span class="definition">{{Definition}}</span>\n'
                '</div>\n'                
                '{{#Synonym}}\n'
                '<div class="sub-header">\n'
                '<span class="synonym"><b>Synonym</b> {{Synonym}}</span>\n'
                '</div>\n'
                '{{/Synonym}}\n'
                '{{#Antonym}}\n'
                '<div class="sub-header">\n'
                '<span class="antonym"><b>Antonym:</b> {{Antonym}}</span>\n'
                '</div>\n'                
                '{{/Antonym}}\n'
                '<div class="sentence">{{Sentence}}</div>\n'
                '<div class="source">{{Source}}</div>\n'
                '<div class="picture">{{Picture}}</div>\n',
            },
        ])
