def snail(A):
    L = len(A)
    E = []
    # for i in range(1, L-1):
    #     E.append(A[i][-1])
    # for i in reversed(A[-1]):
    #     E.append(i)
    # for i in range(L-2, 1,-1):
    #     E.append(A[i][0])
    # for i in range(L-2):
    #     E.append(A[1])
    # for i in A[1][:-1]:
    #     E.append(i)
    c, f = 0, 0

    for i in range(L):
        c = i
        E.append(A[f][c])
    for i in range(1, L):
        f = i
        E.append(A[f][c])
    for i in range(L-2,-1,-1):
        c = i
        E.append(A[f][c])
    for i in range(L - 2, 0, -1):
        f = i
        E.append(A[f][c])

    print(E)


    # top, bottom, right, left = L, L, L, L
    # x, y = 0, 0
    # if L % 2 == 0:
    #     finishx = L // 2
    # while 1:
    #     for i in range(top):
    #         E.append(A[x][y])
    #         x +=1
    #     for i in range(left):
    #         E.append(A[x][y])
    #         y += 1
    #     for i in range(bottom):
    #         E.append(A[x][y])
    #         x -= 1
    #     for i in range(right):
    #         E.append(A[x][y])
    #         y -= 1
