import string
def count_letters(strh):
    #убираю знаки препинания и разбиваю строку на список слов
    words = strh.translate(str.maketrans('', '',string.punctuation ),).split()
    # считаю количество в каждом слове
    letter_counts = [len(word) for word in words]
    letter_counts = []
  #  for word in words: 
  #      letter_counts.append(len(word))
    for i in range(len(words)):
        word = words[i]
        letter_counts.append(len(word))
    return letter_counts
strh = "извини , но ты лох"
letter_counts = count_letters(strh)
print(strh , letter_counts)