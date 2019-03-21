#считает процент слова с точкой в этом файле по отношению к общему числу слов

number_of_words=0
number_of_commas=0
with open("m5-line-by-line.txt", encoding="utf-8") as fp:
    for line in fp:
        line=line.strip().split(' ')
        for word in line:
            number_of_words+=1
            if '.' in word:
                number_of_commas+=1     
print(number_of_words)
print(number_of_commas)
print(int(number_of_commas/number_of_words*100))