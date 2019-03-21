import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

generated_prophecies = []

def rand(s):
    return random.randrange(0, len(s))
c = 0
while c < 5:
    j = 0
    oracle=""
    while j < 3:
        buff=""
        buff=times[rand(times)]+" "+advices[rand(advices)]+" "+promises[rand(promises)]+"."
        oracle=oracle+buff.capitalize()
        j = j + 1
    generated_prophecies.append(oracle)
    c = c + 1
# всё что выше этого комментария вставьте на сайте в блок проверки

i = 0
print("Вот что получилось")
while i < 5:
    print(i + 1, generated_prophecies[i])
    i = i + 1
