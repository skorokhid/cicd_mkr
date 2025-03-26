import pytest
import os
from text_analyzer import count_words_and_sentences

@pytest.fixture
def sample_text_file(tmp_path):
    """Fixture to create a sample text file for testing."""
    content = """This is a sample text. It contains multiple sentences!
    Some sentences end with question marks? Others might end with ellipsis...
    Let's test different separators: comma, semicolon; colon: and others."""
    
    file_path = tmp_path / "sample.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

@pytest.fixture
def empty_file(tmp_path):
    """Fixture to create an empty text file."""
    file_path = tmp_path / "empty.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        pass
    return file_path

@pytest.mark.parametrize("content,expected_words,expected_sentences", [
    ("One word.", 2, 1),
    ("Hello, world! How are you?", 4, 2),
    ("This;is:a:test.", 4, 1),
    ("Multiple    spaces   between     words.", 4, 1),
    ("", 0, 0),
    ("No punctuation but words", 4, 1),
])
def test_count_words_and_sentences_parametrized(tmp_path, content, expected_words, expected_sentences):
    """Parametrized test for various text cases."""
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    word_count, sentence_count = count_words_and_sentences(file_path)
    assert word_count == expected_words
    assert sentence_count == expected_sentences

def test_count_words_and_sentences(sample_text_file):
    """Test with the sample text file fixture."""
    word_count, sentence_count = count_words_and_sentences(sample_text_file)
    assert word_count == 28
    assert sentence_count == 5

def test_empty_file(empty_file):
    """Test with an empty file."""
    word_count, sentence_count = count_words_and_sentences(empty_file)
    assert word_count == 0
    assert sentence_count == 0

def test_file_not_found():
    """Test for non-existent file."""
    with pytest.raises(FileNotFoundError):
        count_words_and_sentences("nonexistent_file.txt")