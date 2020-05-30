def problem3_1(filename):
    infile=open(filename)
    infile = open(filename)
    sum = 0
    for line in infile:
        sum = sum + len(line)
        print(line, end="") 
    print("\n\nThere are", sum, "letters in the file.")
    infile.close()