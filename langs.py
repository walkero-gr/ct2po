#!python
# coding=utf-8
import sys

class langsHandler:
    def __init__(self):
        self.langs = {
            'bs': { # bosnian
                'name': 'bosanski',
                'encoding': 'iso-8859-2'
            },
            'ca': { # catalan
                'name': 'català',
                'encoding': 'iso-8859-15'
            },
            'hr': { # croatian
                'name': 'hrvatski',
                'encoding': 'iso-8859-16'
            },
            'cs': { # czech
                'name': 'czech',
                'encoding': 'iso-8859-2'
            },
            'da': { # danish
                'name': 'dansk',
                'encoding': 'iso-8859-15'
            },
            'nl': { # dutch
                'name': 'nederlands',
                'encoding': 'iso-8859-15'
            },
            'en_GB': { # english-british
                'name': 'english-british',
                # 'encoding': 'iso-8859-1'
            },
            'fi': { # finnish
                'name': 'suomi',
                'encoding': 'iso-8859-15'
            },
            'fr': { # french
                'name': 'français',
                'encoding': 'iso-8859-15'
            },
            'de': { # german
                'name': 'deutsch',
                'encoding': 'iso-8859-15'
            },
            'el': { # greek
                'name': 'greek',
                'encoding': 'iso-8859-7'
            },
            'hu': { # hungarian
                'name': 'magyar',
                'encoding': 'iso-8859-16'
            },
            'it': { # italian
                'name': 'italiano',
                'encoding': 'iso-8859-15'
            },
            'ja': { # japanese
                'name': 'nihongo',
                'encoding': 'euc-jp'
            },
            'ko': { # korean
                'name': 'hangul',
                'encoding': 'euc-kr'
            },
            'no': { # norwegian
                'name': 'norsk',
                'encoding': 'iso-8859-15'
            },
            'fa': { # persian
                'name': 'farsi',
                'encoding': 'utf-8'
            },
            'pl': { # polish
                'name': 'polski',
                'encoding': 'iso-8859-2'
            },
            'pt': { # portuguese
                'name': 'português',
                # 'encoding': 'iso-8859-15'
            },
            'pt_BR': { # portuguese-brazil
                'name': 'português-brasil',
                # 'encoding': 'iso-8859-15'
            },
            'ru': { # russian
                'name': 'russian',
                'encoding': 'windows-1251'
            },
            'sr': { # serbian
                'name': 'srpski',
                'encoding': 'iso-8859-16'
            },
            'sk': { # slovakian
                'name': 'slovak',
                'encoding': 'iso-8859-2'
            },
            'sl': { # slovenian
                'name': 'slovensko',
                'encoding': 'iso-8859-2'
            },
            'es': { # spanish
                'name': 'español',
                'encoding': 'iso-8859-15'
            },
            'sv': { # swedish
                'name': 'svenska',
                'encoding': 'iso-8859-15'
            },
            'tr': { # turkish
                'name': 'türkçe',
                'encoding': 'iso-8859-9'
            }
        }

        return None

    def getEncoding(self, lang):
        try:
            return self.langs[lang]['encoding']
        except KeyError:
            return 'iso-8859-1'
