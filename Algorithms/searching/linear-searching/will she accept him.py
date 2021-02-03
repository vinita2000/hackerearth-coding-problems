
# Write your code here
def findSubsequence(s1, s2):
    flag = 0
    ind = -1
    for i in range(len(s1)):
        flag = 0
        for j in range(ind+1, len(s2)):
            if ind+1<len(s2):
                if s1[i] == s2[j]:
                    ind = j
                    flag = 1
                    break
        if flag == 0:
            return False
    return True  
            

for t in range(int(input())):
    s1, s2 = [x for x in input().split(" ")]
    if (findSubsequence(s1, s2)):
        print("Love you too")
    else:
        print("We are only friends")
    print("\n")
