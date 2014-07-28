f = open("file.txt")
for i in range(int(f.readline())):
    params = [int(x) for x in f.readline().split(" ")]
    rows = params[0]
    cols = params[1]
    mines = params[2]
    sweep = []
    for row in range(rows):
        sweep.append(["." for col in range(cols)])
    sweep[0][0] = "c"
    row = rows - 1
    col = cols - 1
    while (mines > 0):
        sweep[row][col] = "*"
        mines -= 1
        col -= 1
        if (col < 0):
            col = cols - 1
            row -= 1
    caseOut = "Case #%i:\n" % (i + 1)
    try:
        if (sweep[0][1] == "*"): sweep = []
    except IndexError:
        pass
    try :
        if(sweep[1][0] == "*") : sweep = []
    except IndexError:
        pass
    try:
        if(sweep[1][1] == "*"): sweep = []
    except IndexError:
        pass
    if (sweep == []): caseOut += "Impossible\n"
    else: caseOut += "".join([("".join(line) + "\n") for line in sweep])
    a = open("out.txt", 'a')
    a.write(caseOut)
    a.close()
f.close()
