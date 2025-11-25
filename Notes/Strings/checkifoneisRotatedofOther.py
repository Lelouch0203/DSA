def cheks(s,goal):
    # for i in range(len(s)):
    #     if s[i:]+s[:i]== goal:
    #         return True
    # return False
    doubled=s+s
    return goal in doubled
    

