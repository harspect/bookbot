from stats import *
import sys

def main():
    if sys.argv.__len__() != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        # sys.exit(1)
    fileName = sys.argv[1]
    text = get_book_text(fileName)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print(f"--------- Character Count -------")
    ans = create_res(get_num_characters(text))
    print("\n".join(f"{one['char']}: {one['num']}" for one in ans if one['char'].isalpha()))
    print("============= END ===============")

main()