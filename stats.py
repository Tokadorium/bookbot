def get_num_words(str):
  words_array = str.split()
  return len(words_array)

def get_char_counts(str):
  str = str.lower()
  char_counts = {}
  for char in str:
    if char_counts.get(char) == None:
      char_counts[char] = 1
    else:
      char_counts[char] += 1
  return char_counts

def sort_on(dict):
  return dict["num"]

def get_sorted_list(char_dictionary):
  char_list = []
  for key in char_dictionary:
    new_dict = {}
    new_dict["char"] = key
    new_dict["num"] = char_dictionary[key]
    char_list.append(new_dict)
  char_list.sort(reverse=True, key=sort_on)
  return char_list

def word_deco(str_to_embed, decoration_str = "-", line_length = 0):
  deco_count = line_length - len(str_to_embed)
  if deco_count <= 0:
    return str_to_embed
  final_str = ""
  for i in range(0, deco_count // 2):
    final_str += decoration_str
  final_str += str_to_embed
  for i in range(deco_count // 2 + 1, deco_count):
    final_str += decoration_str
  return final_str

def pretty_print(filename = "", word_count = 0, char_count = 0):
  if (word_count == 0 or char_count == 0):
    print("Nothing to display")
    return None
  print(word_deco(" BOOKBOT ", "=", 24))
  if (filename == ""):
    print("Analyzing book...")
  else:
    print(f"Analyzing book found at {filename}...")
  if (word_count == 0):
    pass
  else:
    print(word_deco(" Word Count ", "-", 24))
    print(f"Found {word_count} total words")
  if (char_count == 0):
    pass
  else:
    print(word_deco(" Character Count ", "-", 24))
    for char_dict in char_count:
      char, char_num = char_dict.values()
      if (char.isalpha()):
        print(f"{char}: {char_num}")
  print(word_deco(" END ", "=", 24))