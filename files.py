def reading(filepath):
    f = open(filepath, "r")
    line_num = 1
    for line in f:
        print(f"{line_num} : {line}")
        line_num += 1
    f.close()

def dataProcessing(filepath):
    f = open(filepath, "r")
    names = []
    heights = []
    for line in f:
        name, height = line.strip().split(" ")
        names.append(name)
        heights.append(float(height))
    f.close()
    print("data for", names)
    print("avg height id {0:.2f}".format(sum(heights)/len(heights)))

def writing(filepath):
    #use with so dont have to close file manually
    with open(filepath, "w") as f:
        for i in range(0, 100, 3):
            f.write(str(i))
            f.write("\n")

