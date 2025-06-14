from stats import get_num_words, get_char_counts, get_sorted_list, pretty_print

def get_book_text(filepath):
  with open(filepath) as f:
    file_content = f.read()
  return file_content

def main():
  filename = "books/frankenstein.txt"
  file_content = get_book_text(filename)
  words_in_file = get_num_words(file_content)
  char_counts = get_char_counts(file_content)
  sorted_chars_list = get_sorted_list(char_counts)

  # print(f"{words_in_file} words found in the document")
  # print(char_counts)

  pretty_print(filename, words_in_file, sorted_chars_list)

main()