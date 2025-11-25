def reverseWords(s: str) -> str:
    p=(s.split())
    p.reverse()
    return (" ").join(p)
print(reverseWords("hi ra jai sai"))
