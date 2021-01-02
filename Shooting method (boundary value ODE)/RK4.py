def RK4(N,x0,xN,y10,y20,f1,f2):

    y1 = [None for _ in range(N)]
    y2 = [None for _ in range(N)]
    x = [None for _ in range(N)]
    
    h = (xN-x0) / (N-1)
    y1[0] = y10
    y2[0] = y20
    x[0] = x0

    for n in range(1,N):
            
        k11 = h * f1(x[n-1], y1[n-1], y2[n-1])
        k21 = h * f2(x[n-1], y1[n-1], y2[n-1])
        
        k12 = h * f1(x[n-1] + h/2, y1[n-1] + k11/2, y2[n-1] + k21/2)
        k22 = h * f2(x[n-1] + h/2, y1[n-1] + k11/2, y2[n-1] + k21/2)
        
        k13 = h * f1(x[n-1] + h/2, y1[n-1] + k12/2, y2[n-1] + k22/2)
        k23 = h * f2(x[n-1] + h/2, y1[n-1] + k12/2, y2[n-1] + k22/2)
    
        k14 = h * f1(x[n-1] + h, y1[n-1] + k13, y2[n-1] + k23)
        k24 = h * f2(x[n-1] + h, y1[n-1] + k13, y2[n-1] + k23)
    
        y1[n] = y1[n-1] + (k11 + 2*k12 + 2*k13 + k14)/6
        y2[n] = y2[n-1] + (k21 + 2*k22 + 2*k23 + k24)/6
        x[n] = x[n-1] + h

    return x, y1, y2