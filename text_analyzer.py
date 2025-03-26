import re

def count_words(text):
    """Count words in text using regular expressions"""
    if not text.strip():
        return 0
    words = re.split(r'[,;:\s\t]+', text)
    return len([w for w in words if w.strip()])

def count_sentences(text):
    """Count sentences in text using regular expressions"""
    if not text.strip():
        return 0
    sentences = re.split(r'[.!?…]+', text)
    return len([s for s in sentences if s.strip()])

def analyze_text_file(file_path):
    """
    Analyze text file and return word and sentence counts.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        tuple: (word_count, sentence_count)
    
    Raises:
        FileNotFoundError: If file doesn't exist
        Exception: For other errors
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return count_words(text), count_sentences(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")