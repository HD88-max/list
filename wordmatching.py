#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
def wordmatch(word):
    counts = 0
    list = []
    for i in word:
        if len(i)>1 and i[0] == i[-1]:
                counts = counts + 1
                list.append(i)
    print(list)
    return counts
count = wordmatch(["ab","abe","abp","aba","aba","1221"])
print(count)