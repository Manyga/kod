text2process = 'Первый образец «нового стиля» граффити сохранился в древнегреческом городе Эфесе (на территории современной Турции). Местные гиды называют его рекламным сообщением проституции. Расположенное рядом с украшенной мозаикой и камнями дорогой граффити изображало отпечаток руки, отдалённо напоминающий сердце, отпечаток ноги и число. Это означало, что где-то поблизости находился публичный дом, отпечаток руки символизировал оплату[4].' 
print('DLINASTROKI', len(text2process)) 
# text2process = ' joja '

def upper_letters_from_str(sample_text):
    corrected_text = ''
    for i in range(len(sample_text)): 
        symbol = sample_text[i]
        print(i, symbol)
        if symbol.isalpha() or symbol == ' ':
            corrected_text += symbol.upper()
    return corrected_text
cor_text = upper_letters_from_str(text2process)
# print(upper_letters_from_str('pivo'))
# print(cor_text)
# exit()
def text_to_wordslist(text):
    return text.split(sep=' ') 
print(cor_text) 
text_list = text_to_wordslist(cor_text)
print(text_list)

words_dict = {}
for word in text_list:


exit()

words =sample_text.split(sep='.') 
print(type(words)) 
print(words) 
for i in range(len(words)): 
    word = words[i] 
    print(i, word)
    #if word == 'на':  #cтрогое равенство 
    if 'на' in word:   #наличие подстроки в строке
        print('+' * 20)
   
print('CHEESLOSLOV', len(words))