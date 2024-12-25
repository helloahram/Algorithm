str = input().strip()
sub_str = set()

for i in range(len(str)):
    for j in range(i+1, len(str)+1):
        sub_str.add(str[i:j])

print(len(sub_str))