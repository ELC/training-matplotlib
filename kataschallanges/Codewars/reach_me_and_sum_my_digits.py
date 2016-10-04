def sumDig_nthTerm(initVal, patternL, nthTerm):
    term = initVal
    mod = len(patternL)
    for i in range(nthTerm-1):
        term = patternL[i % mod] + term
    return sum(int(i) for i in str(term))
