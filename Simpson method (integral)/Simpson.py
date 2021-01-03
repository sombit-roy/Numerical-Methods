def Simpson(F,x1,xN,N):
    
    h = (xN-x1) / (N-1)
    I = (F(x1) + F(xN)) * h/3
    x = [None for _ in range(N)]
    x[0] = x1
    
    for j in range(1,N):
        x[j] = x[j-1] + h

    for i in range(1,N-1):
        if (i%2 == 0):
            I = I + 4*h*F(x[i])/3
        else:
            I = I + 2*h*F(x[i])/3

    return I