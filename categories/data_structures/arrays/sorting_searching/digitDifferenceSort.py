def digitDifferenceSort(a):
    def getDiff(n):
        s = list(map(int, list(str(n))))
        return max(s) - min(s)        
    
    return sorted(reversed(a), key=getDiff)
    
