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
                'qfmt': """
                <div class="header">
                <span class="word">{{Word}}</span>
                </div>
                
                <div class="header">
                <span class="transcription">{{Transcription}}</span>
                <span class="part-of-speech">{{Part of Speech}}</span>
                </div>
                <span class="audio">{{Audio}}</span>""",

                'afmt': """
                {{FrontSide}}
                
                <hr id="answer">
                
                <div class="sub-header">
                <span class="definition">{{Definition}}</span>
                </div>
                
                {{#Synonym}}
                <div class="sub-header">
                <span class="synonym"><b>Synonym</b> {{Synonym}}</span>
                </div>
                {{/Synonym}}
                {{#Antonym}}
                <div class="sub-header">
                <span class="antonym"><b>Antonym:</b> {{Antonym}}</span>
                </div>
                
                {{/Antonym}}
                <div class="sentence">{{Sentence}}</div>
                <div class='source'>{{Source}}</div>
                <div class="picture">{{Picture}}</div>""",
            },
        ])
