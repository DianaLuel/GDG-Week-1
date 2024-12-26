def input_accepter():
    paragraph = input("Enter a paragraph:\n")
    return paragraph

def menu():
    menu_list = """
    Welcome to "Word Frequency Analyzer"!!!
    ----------------------------------
    |    1. Display Word Frequency   |
    |    2. Display Top N words      |
    |    3. Word search              | 
    |    4. Exit                     |
    ----------------------------------
    """
    print(menu_list)
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Enter a valid number.")

def word_tokenization(para):
    words = para.split()  # Split text into individual words
    return words

def freq_calc(tokens):
    counts = dict()
    for token in tokens:
        token = token.lower()  # Make the words case-insensitive
        if token not in counts:
            counts[token] = 1
        else:
            counts[token] += 1
    return counts

def display_freq(word_lists):
    sorted_words = sorted(word_lists.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

def display_top_n(word_lists):
    try:
        number = int(input("Top N words; Enter the value of N you want to be displayed: "))
        sorted_words = sorted(word_lists.items(), key=lambda item: item[1], reverse=True)
        if number > len(sorted_words):
            print("Enter a valid range.")
        else:
            for word, count in sorted_words[:number]:
                print(f"{word}: {count}")
    except ValueError:
        print("Enter a valid input.")

def word_search(word_lists):
    search_word = input("Enter the word you want to find: ").lower()
    if search_word in word_lists:
        print(f"The word '{search_word}' appears {word_lists[search_word]} times.")
    else:
        print(f"The word '{search_word}' is not found in the text.")

def main():
    print("Welcome to *Word Frequency Analyzer* !!!")
    para = input_accepter()
    tokens = word_tokenization(para)
    word_lists = freq_calc(tokens)
    
    while True:
        choice = menu()
        match choice:
            case 1:
                display_freq(word_lists)
            case 2:
                display_top_n(word_lists)
            case 3:
                word_search(word_lists)
            case 4:
                print("Bye bye :)\n")
                exit()
            case _:
                print("Enter numbers only from the above menu.")

if __name__ == "__main__":
    main()
