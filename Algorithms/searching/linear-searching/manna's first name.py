# Write your code here
for t in range(int(input())):
    st = input()
    cnt1 = st.count('SUVO')
    cnt2 = st.count('SUVOJIT')
    output = "SUVO = " + str(abs(cnt1-cnt2)) + ", " + "SUVOJIT = " + str(cnt2)
    print(output) 
    
