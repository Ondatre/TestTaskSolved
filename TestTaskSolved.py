size = int(input('Сколько слов хотите ввести: \n'))
index = 1 
LessThreeLetters = []
MoreThreeLetters = []
while (index <= size):
    Word = input('Введите слово:\n')
    if len(Word) <= 3:
        LessThreeLetters.append(Word)
    else:
        MoreThreeLetters.append(Word)
    index += 1
print(LessThreeLetters)