

class Bolder:
    def __init__(self):
        self._format = '<span style="font-weight: bold; color: red">{0}</span>'

    def bold(self, text, words):
        for word in words:
            text = text.replace(word, self._format.format(word))
        return text
