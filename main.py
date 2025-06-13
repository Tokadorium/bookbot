from stats import get_num_words
from stats import get_char_counts

def get_book_text(filepath):
  with open(filepath) as f:
    file_content = f.read()
  return file_content

def main():
  file_content = get_book_text("books/frankenstein.txt")
  words_in_file = get_num_words(file_content)
  char_counts = get_char_counts(file_content)

  print(f"{words_in_file} words found in the document")
  print(char_counts)

main()