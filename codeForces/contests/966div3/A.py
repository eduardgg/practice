
for _ in range(int(input())):
    s = input()
    print("NO" if len(s) <= 2 or s[0:2] != "10" or s[2] == '0' or (len(s) == 3 and s[2] == '1') else "YES")