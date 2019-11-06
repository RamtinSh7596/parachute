import re


class Cleaner:
    def __init__(self):
        self.pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    def clean(self, text):
        return re.sub(self.pattern, '', text)


if __name__ == '__main__':
    cleaner = Cleaner()
    print(cleaner.clean("<div style='color: red'>my test</div>"))
