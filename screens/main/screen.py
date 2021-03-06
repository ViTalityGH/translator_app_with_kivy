from kivy.lang import Builder

from core.translator_engine import TranslatorEngine
from screens.base.screen import BaseScreen


Builder.load_file('screens/main/main.kv')


class MainScreen(BaseScreen):
    original_lang = ['eng', 'Английский']
    expected_transl = ['rus', 'Русский']
    tr_engine = None

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__()
        self.update_translation_direction()
        self.tr_engine = TranslatorEngine()

    def update_translation_direction(self):
        self.original_lang, self.expected_transl = self.expected_transl, self.original_lang
        self.title = '{} [font=FontAwesome]\uf07e[/font] {}'.format(self.original_lang[1], self.expected_transl[1])
        self.ids.input.text = ''
        self.ids.output_view.text = ''

    def on_title_press(self, *args):
        self.update_translation_direction()

    def translate_text(self):
        text = self.ids.input.text
        translation = self.tr_engine.translate_text(text, self.original_lang[0], self.expected_transl[0])
        output_view = self.ids.output_view
        output_view.text = translation
