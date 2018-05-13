import goslate
import win32com.client as wincl
from gtts import gTTS
import os
def trans(input,convert):
    gs = goslate.Goslate()
    lang1 = {
        'afrikaans': 'af',
        'albanian': 'sq',
        'arabic': 'ar',
        'armenian': 'hy',
        'bengali': 'bn',
        'catalan': 'ca',
        'chinese': 'zh',
        'chinese (mandarin/china)': 'zh-cn',
        'chinese (mandarin/taiwan)': 'zh-tw',
        'chinese (cantonese)': 'zh-yue',
        'croatian': 'hr',
        'czech': 'cs',
        'danish': 'da',
        'dutch': 'nl',
        'english': 'en',
        'english (australia)': 'en-au',
        'english (united kingdom)': 'en-uk',
        'english (united states)': 'en-us',
        'esperanto': 'eo',
        'finnish': 'fi',
        'french': 'fr',
        'german': 'de',
        'greek': 'el',
        'hindi': 'hi',
        'hungarian': 'hu',
        'icelandic': 'is',
        'indonesian': 'id',
        'italian': 'it',
        'japanese': 'ja',
        'khmer (cambodian)': 'km',
        'korean': 'ko',
        'latin': 'la',
        'latvian': 'lv',
        'macedonian': 'mk',
        'norwegian': 'no',
        'polish': 'pl',
        'portuguese': 'pt',
        'romanian': 'ro',
        'russian': 'ru',
        'serbian': 'sr',
        'sinhala': 'si',
        'slovak': 'sk',
        'spanish': 'es',
        'spanish (spain)': 'es-es',
        'spanish (united states)': 'es-us',
        'swahili': 'sw',
        'swedish': 'sv',
        'tamil': 'ta',
        'thai': 'th',
        'turkish': 'tr',
        'ukrainian': 'uk',
        'vietnamese': 'vi',
        'welsh': 'cy'
    }
    translatedText = gs.translate(convert, lang1[input])
    print(translatedText)
    tts = gTTS(text=translatedText, lang=lang1[input])
    tts.save("pcvoice.mp3")

    os.system("start pcvoice.mp3")