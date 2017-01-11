intermediaries = ["", "+", "-", "*", "^"]
results = {}

def pattern(string, digit):
    if digit == 10:
        res = eval(string)
        if 1 <= res <= 11111 and res not in results:
            global results
            results[res] = string
            print("(" + str(len(results)) + ")", string, "=", res)

        return

    global intermediaries

    for i in intermediaries:
        pattern(string + i + str(digit), digit + 1)

pattern("1", 2)

print("found", len(results), "results")
with open("output", "w") as f:
    for i in range(1, 11111):
        if i in results:
            print(i, "=", results[i], file=f)
