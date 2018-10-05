import argparse
from google.cloud import translate
import six


def translate_text(target, text):
    print('traduciendo: ', text)
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)
    resultTranslated = result['translatedText']

    return resultTranslated