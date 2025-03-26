import re

def count_words_and_sentences(file_path):
    """
    Count the number of words and sentences in a text file.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        tuple: (word_count, sentence_count)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Count sentences (ending with .!?...)
            sentence_pattern = r'[.!?…]+'
            sentences = re.split(sentence_pattern, text)
            sentence_count = len([s for s in sentences if s.strip()])
            
            # Count words (split by ,;: space or tab)
            word_pattern = r'[,;:\s\t]+'
            words = re.split(word_pattern, text)
            word_count = len([w for w in words if w.strip()])
            
            return word_count, sentence_count
            
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")