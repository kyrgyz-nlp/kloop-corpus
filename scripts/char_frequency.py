from collections import Counter
import re

def read_and_analyze_text(filepath):
    # Dictionary to store character frequencies
    char_freq = Counter()
    
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into articles using the 'Title:' marker
    articles = content.split('Title:')[1:]  # Skip the first empty split
    
    for article in articles:
        # Find the text between 'Sentences:' and '----------------------------------------'
        match = re.search(r'Sentences:\n----------------------------------------\n(.*?)\n----------------------------------------', 
                         article, re.DOTALL)
        
        if match:
            # Get the news text and convert to lowercase
            news_text = match.group(1).lower()
            
            # Update character frequencies
            char_freq.update(news_text)
    
    return char_freq

def print_stats(char_freq):
    # Get total character count
    total_chars = sum(char_freq.values())
    
    print(f"Total characters: {total_chars}")
    print("\nCharacter frequencies:")
    print("Char | Count | Percentage")
    print("-" * 30)
    
    # Sort by frequency, highest first
    for char, count in sorted(char_freq.items(), key=lambda x: x[1], reverse=True):
        if char.isspace():
            char_display = "SPACE"
        elif char == '\n':
            char_display = "\\n"
        else:
            char_display = char
        percentage = (count / total_chars) * 100
        print(f"{char_display:5} | {count:5d} | {percentage:6.2f}%")

if __name__ == "__main__":
    filepath = "all_texts.txt"
    char_freq = read_and_analyze_text(filepath)
    print_stats(char_freq)
