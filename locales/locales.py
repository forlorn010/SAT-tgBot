import json

def load_languages():
    global languages
    for lang in ['en', 'ru']:
        with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
            languages[lang] = json.load(f)


# get translated text
def t(lang: str, key: str):
    return languages.get(lang, "en").get(key, key) #en is default language
