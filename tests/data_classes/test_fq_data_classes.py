from src.data_classes.fq_data_classes import Book, Canto, Stanza, Line

# BOOK


def test_book_init(fq_book_root):
    book = Book(fq_book_root)
    assert book.root_node == fq_book_root


def test_book_repr(fq_book):
    assert repr(fq_book) == f"Book(number=1)"


def test_book_eq(make_fake_book, make_fake_canto, make_fake_stanza, make_fake_line):
    # case: equal
    lines = [make_fake_line(1, ""), make_fake_line(2, "")]
    stanzas = [make_fake_stanza(1, lines), make_fake_stanza(2, lines)]
    cantos = [make_fake_canto(1, stanzas), make_fake_canto(2, stanzas)]
    book1, book2 = make_fake_book(1, cantos), make_fake_book(1, cantos)
    assert book1 == book2

    # case: unequal, numbers differ
    book1, book2 = make_fake_book(1, cantos), make_fake_book(2, cantos)
    assert book1 != book2

    # case: unequal, cantos differ
    book1_cantos = [make_fake_canto(1, stanzas), make_fake_canto(2, stanzas)]
    book2_cantos = [make_fake_canto(3, stanzas), make_fake_canto(4, stanzas)]
    book1, book2 = make_fake_book(1, book1_cantos), make_fake_book(1, book2_cantos)
    assert book1 != book2


def test_book_number(fq_book):
    assert fq_book.number() == 1


# CANTO


def test_canto_init(fq_canto_root):
    canto = Canto(fq_canto_root)
    assert canto.root_node == fq_canto_root


def test_canto_repr(fq_canto):
    assert repr(fq_canto) == f"Canto(number=1)"


def test_canto_eq(make_fake_canto, make_fake_stanza, make_fake_line):
    # case: equal
    lines = [make_fake_line(1, ""), make_fake_line(2, "")]
    stanzas = [make_fake_stanza(1, lines), make_fake_stanza(2, lines)]
    canto1, canto2 = make_fake_canto(1, stanzas), make_fake_canto(1, stanzas)
    assert canto1 == canto2

    # case: unequal, numbers differ
    canto1, canto2 = make_fake_canto(1, stanzas), make_fake_canto(2, stanzas)
    assert canto1 != canto2

    # case: unequal, stanzas differ
    canto1_stanzas = [make_fake_stanza(1, lines), make_fake_stanza(2, lines)]
    canto2_stanzas = [make_fake_stanza(3, lines), make_fake_stanza(4, lines)]
    canto1, canto2 = make_fake_canto(1, canto1_stanzas), make_fake_canto(
        1, canto2_stanzas
    )
    assert canto1 != canto2


def test_canto_number(fq_canto):
    assert fq_canto.number() == 1


# STANZA


def test_stanza_init(fq_stanza_root):
    stanza = Stanza(fq_stanza_root)
    assert stanza.root_node == fq_stanza_root


def test_stanza_repr(fq_stanza):
    assert repr(fq_stanza) == f"Stanza(number=1)"


def test_stanza_eq(make_fake_stanza, make_fake_line):
    # case: equal
    lines = [make_fake_line(1, ""), make_fake_line(2, "")]
    stanza1, stanza2 = make_fake_stanza(1, lines), make_fake_stanza(1, lines)
    assert stanza1 == stanza2

    # case: unequal, numbers differ
    lines = [make_fake_line(1, ""), make_fake_line(2, "")]
    stanza1, stanza2 = make_fake_stanza(1, lines), make_fake_stanza(2, lines)
    assert stanza1 != stanza2

    # case: unequal, lines differ
    stanza1_lines, stanza2_lines = [make_fake_line(1, ""), make_fake_line(2, "")], [
        make_fake_line(3, "A"),
        make_fake_line(4, "A"),
    ]
    stanza1, stanza2 = make_fake_stanza(1, stanza1_lines), make_fake_stanza(
        1, stanza2_lines
    )
    assert stanza1 != stanza2


def test_stanza_number(fq_stanza):
    assert fq_stanza.number() == 1


# LINE


def test_line_init(fq_line_root):
    line = Line(fq_line_root)
    assert line.root_node == fq_line_root


def test_line_repr(fq_line):
    assert repr(fq_line) == f"Line(number=1)"


def test_line_eq(make_fake_line):
    # case: equal
    line1 = make_fake_line(number=1, text="A Gentle Knight was pricking on the plaine,")
    line2 = make_fake_line(number=1, text="A Gentle Knight was pricking on the plaine,")
    assert line1 == line2

    # case: unequal, numbers differ
    line1 = make_fake_line(number=1, text="A Gentle Knight was pricking on the plaine,")
    line2 = make_fake_line(number=2, text="A Gentle Knight was pricking on the plaine,")
    assert line1 != line2

    # case: unequal, text differs
    line1 = make_fake_line(number=1, text="A Gentle Knight was pricking on the plaine,")
    line2 = make_fake_line(number=2, text="No Knights, no plaines, no pricking")
    assert line1 != line2


def test_line_number(fq_line):
    assert fq_line.number() == 1


def test_line_text(fq_line):
    assert (
        fq_line.text(spelling="modern") == "A Gentle Knight was pricking on the plaine,"
    )
    assert (
        fq_line.text(spelling="oxford") == "A Gentle Knight was pricking on the plaine,"
    )


def test_line_text_spelling_variation(fq_line_spelling_variation):
    assert (
        fq_line_spelling_variation.text(spelling="modern")
        == "Ycladd in mightie armes and silver shielde,"
    )
    assert (
        fq_line_spelling_variation.text(spelling="oxford")
        == "Ycladd in mightie armes and siluer shielde,"
    )
