#считает процент слова с запятой в этом файле по отношению к общему числу слов

number_of_words=0
number_of_commas=0
fp = open("m5-line-by-line.txt", encoding="utf-8")
line = fp.readline()
while len(line) != 0:
    line=line.split(' ')
    for word in line:
        number_of_words+=1
        if ',' in word:
            number_of_commas+=1
    line = fp.readline()
fp.close()
print(number_of_commas)
print(number_of_words)
print(int(number_of_commas/number_of_words*100))