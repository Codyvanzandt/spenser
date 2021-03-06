import pytest
from lxml import etree
from src.data_classes.fq_data_classes import Book, Canto, Stanza, Line
from src.constants import NAMESPACES

# File paths
@pytest.fixture(scope="session")
def fq_book1_xml_path():
    return "./data/primary_text_xml/fq1590.bk1.xml"


# XML root nodes
@pytest.fixture(scope="session")
def fq_book_root(fq_book1_xml_path):
    return (
        etree.parse(fq_book1_xml_path)
        .getroot()
        .xpath('.//tei:div[@n="1" and @type="book"]', namespaces=NAMESPACES)[0]
    )


@pytest.fixture(scope="session")
def fq_canto_root(fq_book_root):
    return fq_book_root.xpath(
        './/tei:div[@n="1" and @type="canto"]', namespaces=NAMESPACES
    )[0]


@pytest.fixture(scope="session")
def fq_stanza_root(fq_canto_root):
    return fq_canto_root.xpath('.//tei:lg[@n="1"]', namespaces=NAMESPACES)[0]


@pytest.fixture
def fq_line_root(fq_stanza_root):
    return fq_stanza_root.xpath(".//tei:l", namespaces=NAMESPACES)[0]


@pytest.fixture
def fq_line_spelling_variation_root(fq_stanza_root):
    return fq_stanza_root.xpath(".//tei:l", namespaces=NAMESPACES)[1]


# Data classes
@pytest.fixture
def fq_book(fq_book_root):
    return Book(fq_book_root)


@pytest.fixture
def fq_canto(fq_canto_root):
    return Canto(fq_canto_root)


@pytest.fixture
def fq_stanza(fq_stanza_root):
    return Stanza(fq_stanza_root)


@pytest.fixture
def fq_line(fq_line_root):
    return Line(fq_line_root)


@pytest.fixture
def fq_line_spelling_variation(fq_line_spelling_variation_root):
    return Line(fq_line_spelling_variation_root)


# Data class factories
@pytest.fixture
def make_fake_line():
    def _make_fake_line(number, text):
        line = Line(None)

        def _fake_text_fn(spelling="modern"):
            return text

        line.text = _fake_text_fn
        line.number = lambda: number
        return line

    return _make_fake_line


@pytest.fixture
def make_fake_stanza():
    def _make_fake_stanza(number, lines):
        stanza = Stanza(None)
        stanza.number = lambda: number
        stanza.lines = lambda: lines
        return stanza

    return _make_fake_stanza


@pytest.fixture
def make_fake_canto():
    def _make_fake_canto(number, stanzas):
        canto = Canto(None)
        canto.number = lambda: number
        canto.stanzas = lambda: stanzas
        return canto

    return _make_fake_canto


@pytest.fixture
def make_fake_book():
    def _make_fake_book(number, cantos):
        book = Book(None)
        book.number = lambda: number
        book.cantos = lambda: cantos
        return book

    return _make_fake_book
