import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERS = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERS,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text=''):
    """Function translating english text to french."""
    if english_text != '':
        response = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = response['translations'][0]['translation']
        print(french_text)
        return french_text
    else:
        return 'Text should not be empty'


def frenchToEnglish(french_text=''):
    """Function translating french text to ensglish."""
    if french_text != '':
        response = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = response['translations'][0]['translation']
        print(english_text)
        return english_text
    else:
        return 'Text should not be empty'
