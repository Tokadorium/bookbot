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