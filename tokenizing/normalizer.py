import re

compile_patterns = lambda patterns: [(re.compile(pattern), repl) for pattern, repl in patterns]


class Normalizer:
    def __init__(self, affix_spacing=True, persian_numbers=True, remove_diacritics=True, remove_extra_spaces=True):
        NUMBERS = '۰۱۲۳۴۵۶۷۸۹'
        maketrans = lambda A, B: dict((ord(a), b) for a, b in zip(A, B))
        self._affix_spacing = affix_spacing
        translation_src, translation_dst = ' ىكي“”', ' یکی""'
        if persian_numbers:
            translation_src += '0123456789%'
            translation_dst += '۰۱۲۳۴۵۶۷۸۹٪'
        self.translations = maketrans(translation_src, translation_dst)
        self.character_refinement_patterns = []

        if remove_extra_spaces:
            self.character_refinement_patterns.extend([
                (r'\n\n+', '\n\n'),  # remove extra newlines
                (r'[ـ\r]', ' '),  # remove keshide, carriage returns
                (r' ?\.', ' '),
                (r' ?\<', ' '),
                (r' ?\>', ' '),
                (r' ?\؟', ' '),
                (r' ?\!', ' '),
                (r' ?\،', ' '),
                (r' ?\D\:', ' '),
                (r'^', ' '),
                (r' ?\)', ' '),
                (r' ?\(', ' '),
                (r'\u200C', ' '),
                (r' ?\-', ' '),
                (r' ?\_', ' '),
                (r' +', ' '),
            ])

        if remove_diacritics:
            self.character_refinement_patterns.append(
                ('[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u2022]', ''),
                # remove FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA, SHADDA, SUKUN
            )

        punc_after, punc_before = r'\.:!،؛؟»\]\)\}', r'«\[\(\{'
        if affix_spacing:
            self.affix_spacing_patterns = [
                (r'([^ ]ه) ی ', r'\1‌ی '),  # fix ی space
                (r'(^| )(ن?می) ', r'\1\2‌'),  # put zwnj after می, نمی
                (
                    r'(?<=[^\n\d ' + punc_after + punc_before + ']{2}) (تر(ین?)?|گری?|های?)(?=[ \n' + punc_after + punc_before + ']|$)',
                    r'‌\1'),  # put zwnj before تر, تری, ترین, گر, گری, ها, های
                (r'([^ ]ه) (ا(م|یم|ش|ند|ی|ید|ت))(?=[ \n' + punc_after + ']|$)', r'\1‌\2'),
                # join ام, ایم, اش, اند, ای, اید, ات
            ]

    def character_refinement(self, text):
        text = text.translate(self.translations)
        for pattern, repl in self.character_refinement_patterns:
            text = re.compile(pattern).sub(repl, text)
        return text

    def affix_spacing(self, text):
        for pattern, repl in self.affix_spacing_patterns:
            text = re.compile(pattern).sub(repl, text)
        return text

    def normalize(self, text):
        text = self.character_refinement(text)
        if self._affix_spacing:
            text = self.affix_spacing(text)
        return text


if __name__ == '__main__':
    normalizer = Normalizer()
    normal = normalizer.normalize(
        'كریمي :() بُشقابِ مَن،را بِگیر- و فاصله ی میان .. - . _ پیشوند ها >>؟و پسوند ها. .. را اصلاح<. می کند!؟')
    print(normal)
