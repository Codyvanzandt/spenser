import pytest
from lxml import etree
from src.data_classes.fq_data_classes import FQBook

# File paths
@pytest.fixture(scope="session")
def fq_example_path():
    return "./data/examples/fq1590_book1_canto1_stanza1_2.xml"

# XML etree roots

@pytest.fixture(scope="session")
def fq_example_root(fq_example_path):
    """
    Returns:
        An etree root of data/examples/fq1590_book1_canto1_stanza1_2.xml
        This xml file contains the metadata, proem, and first two stanzas of FQ Book 1 Canto 1
    """
    return etree.parse(fq_example_path).getroot()


@pytest.fixture
def fq_example_book(fq_example_path):
    return FQBook(fq_example_path)
