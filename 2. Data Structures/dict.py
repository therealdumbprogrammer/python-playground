str = input("Enter a string: ")
freq = {}

for c in str.lower():
    if c != ' ':
        freq[c] = freq.get(c, 0) + 1

print(f"Frequencies: {freq}")

rev_freq = {}
for k,v in freq.items():
    if v in rev_freq:
        rev_freq[v].append(k)
    else:
        rev_freq[v] = [k]    

print(f"Reversed frequencies: {rev_freq}")