def printFilePermutations(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            printPermutations(line)

def printPermutations(string):
    permute_list = []
    permute(string, "", permute_list)
    print(', '.join(sorted(permute_list)))

def permute(string, permutation, list):
    if len(string) == 0:
        list.append(permutation)
    else:
        for i in range(len(string)):
            char = string[i]
            permutation += char
            string = string[:i] + string[i+1:]

            permute(string, permutation, list)

            string = string[:i] + char + string[i:]
            permutation = permutation[:len(permutation) - 1]



printFilePermutations("testfile.txt")