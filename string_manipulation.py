# Function to find the most frequently occurring word in a sentence
def most_frequent_word(sentence):
  
    import re
    from collections import Counter

    # To remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', sentence.lower())

    # Count word frequencies
    word_count = Counter(words)

    # Get the most frequent words
    max_count = max(word_count.values(), default=0)
    frequent_words = [word for word, count in word_count.items() if count == max_count]

    # Return the first occurring word 
    for word in words:
        if word in frequent_words:
            return word

    return None

# Example usage
sentence = "This is a test. This test is only a test."
print(most_frequent_word(sentence))
