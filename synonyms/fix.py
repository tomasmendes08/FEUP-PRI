lines = [x.split(",") for x in open("synonyms.txt").readlines()]

file = open("synonyms_fix.txt", "w")

# file.write("\n".join(lines))

for l in list(lines):
    if l[-1] == "\n":
        lines.remove(l)
        continue
    else:
        l[-1] = l[-1].strip()
        file.write(",".join(l) + "\n")
    