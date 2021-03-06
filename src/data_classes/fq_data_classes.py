class Book:
    def __init__(self, book_root_node):
        self.root_node = book_root_node

    def __repr__(self):
        return f"{self.__class__.__name__}(number={self.number()})"

    def __eq__(self, other):
        numbers_equal = self.number() is not None and (self.number() == other.number())
        cantos_equal = self.cantos() is not None and (self.cantos() == other.cantos())
        return numbers_equal and cantos_equal

    def number(self):
        return None

    def cantos(self):
        return None


class Canto:
    def __init__(self, canto_root_node):
        self.root_node = canto_root_node

    def __repr__(self):
        return f"{self.__class__.__name__}(number={self.number()})"

    def __eq__(self, other):
        numbers_equal = self.number() is not None and (self.number() == other.number())
        stanzas_equal = self.stanzas() is not None and (
            self.stanzas() == other.stanzas()
        )
        return numbers_equal and stanzas_equal

    def number(self):
        return None

    def stanzas(self):
        return None


class Stanza:
    def __init__(self, stanza_root_node):
        self.root_node = stanza_root_node

    def __repr__(self):
        return f"{self.__class__.__name__}(number={self.number()})"

    def __eq__(self, other):
        numbers_equal = self.number() is not None and (self.number() == other.number())
        lines_equal = self.lines() is not None and (self.lines() == other.lines())
        return numbers_equal and lines_equal

    def number(self):
        return None

    def lines(self):
        return None


class Line:
    def __init__(self, line_root_node):
        self.root_node = line_root_node

    def __repr__(self):
        return f"{self.__class__.__name__}(number={self.number()})"

    def __eq__(self, other):
        numbers_equal = self.number() is not None and (self.number() == other.number())
        modern_texts_equal = self.text(spelling="modern") is not None and (
            self.text(spelling="modern") == other.text(spelling="modern")
        )
        oxford_texts_equal = self.text(spelling="oxford") is not None and (
            self.text(spelling="oxford") == other.text(spelling="oxford")
        )
        return numbers_equal and modern_texts_equal and oxford_texts_equal

    def number(self):
        return None

    def text(self, spelling="modern"):
        return None
