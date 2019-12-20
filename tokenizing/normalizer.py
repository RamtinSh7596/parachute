import re


class Normalizer:
    def __init__(self, affix_spacing=True):
        self._affix_spacing = affix_spacing
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

    def affix_spacing(self, text):
        for pattern, repl in self.affix_spacing_patterns:
            text = re.compile(pattern).sub(repl, text)
        return text

    def normalize(self, text):
        if self._affix_spacing:
            text = self.affix_spacing(text)
        return text


if __name__ == '__main__':
    normalizer = Normalizer()
    normal = normalizer.normalize('فاصله ی میان پیشوند ها و پسوند ها را اصلاح می کند')
    print(normal)
