import itertools
import os

# Leet speak mapping
LEET_MAPPING = {
    'a': ['@', '4'],
    'b': ['8'],
    'e': ['3'],
    'g': ['6', '9'],
    'i': ['1', '!'],
    'l': ['1', '|'],
    'o': ['0'],
    's': ['5', '$'],
    't': ['7'],
    'z': ['2']
}

COMMON_SUFFIXES = ['123', '!', '@', '#', '1', '2023', '2024']
COMMON_PREFIXES = ['!', '@', '#', '1', '2023', '2024']

def generate_leet_variations(word):
    """
    Generate all possible leet speak variations of a word.
    """
    if not word:
        return [word]
    
    variations = ['']
    for char in word:
        new_variations = []
        for variation in variations:
            # Add the original character
            new_variations.append(variation + char)
            # Add leet replacements if available
            if char.lower() in LEET_MAPPING:
                for leet_char in LEET_MAPPING[char.lower()]:
                    new_variations.append(variation + leet_char)
        variations = new_variations
    return variations

def generate_wordlist(details):
    """
    Generate a wordlist based on input details with variations.
    """
    wordlist = set()
    
    # Generate basic permutations of details
    for r in range(1, len(details) + 1):
        for combo in itertools.permutations(details, r):
            base_word = ''.join(combo)
            wordlist.add(base_word)
            # Generate leet variations for each permutation
            for leet_word in generate_leet_variations(base_word):
                wordlist.add(leet_word)
    
    # Add common prefixes and suffixes
    enhanced_wordlist = set()
    for word in wordlist:
        for suffix in COMMON_SUFFIXES:
            enhanced_wordlist.add(word + suffix)
        for prefix in COMMON_PREFIXES:
            enhanced_wordlist.add(prefix + word)
        # Capitalized version
        enhanced_wordlist.add(word.capitalize())
    
    # Merge enhanced wordlist with original
    wordlist.update(enhanced_wordlist)
    
    return wordlist

def save_wordlist(wordlist, filename='wordlist.txt'):
    """
    Save the generated wordlist to a file.
    """
    try:
        with open(filename, 'w') as f:
            for word in sorted(wordlist):  # Sort alphabetically for better readability
                f.write(word + '\n')
        print(f"Wordlist successfully saved to '{filename}' with {len(wordlist)} entries.")
    except IOError as e:
        print(f"Error saving wordlist: {e}")

def main():
    """
    Main function to handle user input and generate the wordlist.
    """
    print("Advanced Wordlist Generator")
    print("-" * 30)
    user_input = input("Enter details separated by commas (e.g., name,birthdate,hobby): ")
    details = [detail.strip() for detail in user_input.split(',') if detail.strip()]
    
    if not details:
        print("Error: No valid details provided. Please try again.")
        return

    wordlist = generate_wordlist(details)
    save_wordlist(wordlist)
    print("Wordlist generation completed.")

if __name__ == "__main__":
    main()

