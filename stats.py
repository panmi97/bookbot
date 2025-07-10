def get_num_words(words):
    
    
    num_words=len(words)

    return num_words


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_dict(diction):
    def sort_on(item):
        return item[1] 

    sorted_items = sorted(diction.items(), key=sort_on, reverse=True)
    return dict(sorted_items)


def printAll(ordered, num ,url):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")

    for char in ordered:
        if char.isalpha():
            print(f"{char}: {ordered[char]}")

    print("============= END ===============")
