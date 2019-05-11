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