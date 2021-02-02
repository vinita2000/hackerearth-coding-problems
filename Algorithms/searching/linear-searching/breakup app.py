
# Write your code here
date = no_date = 0
n = int(input())
for _ in range(n):
    chat = input().split(" ")
    #print(chat)

    for msg in chat:
        if msg.isdigit():
            if msg=='19' or msg=='20' and msg[0][0]=='G':
                date += 2
            else:
                no_date += 1
    
print('Date') if date>no_date else print('No Date')
    

