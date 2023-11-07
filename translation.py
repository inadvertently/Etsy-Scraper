from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='en',
    target_language='es',
    timeout=10
)

def translation(text):
    translator.translate(text)