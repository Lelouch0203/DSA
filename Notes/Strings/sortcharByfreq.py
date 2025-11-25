from collections import Counter

def frequencySort(s):
    cnt = Counter(s)
    ans = []
    for freq, ch in cnt.most_common():
        ans.append(ch*freq)
    print(cnt.most_common())
    return "".join(ans)
print(frequencySort("aAbb"))