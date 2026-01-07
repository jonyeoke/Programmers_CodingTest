def solution(line):
    answer = []
    save=[]
    min_x =min_y= int(1e15)
    max_x = max_y = int(-1e15)
    for i in range(len(line)):
        a,b,e=line[i]
        for j in range(len(line)):
            c,d,f=line[j]
            
            if a*d == b*c: continue
            x = (b * f - e * d)/(a*d-b*c)
            y = (e * c - a * f)/(a*d-b*c)
            if x == int(x) and y == int(y):
                save.append([int(x),int(y)])
                if min_x>x:min_x=x
                if min_y>y:min_y=y
                if max_x<x:max_x=x
                if max_y<y:max_y=y
    x_len = int(max_x-min_x+1)
    y_len = int(max_y-min_y+1)
    coord = [['.']*x_len for i in range(y_len)]
    
    for x, y in save:
        nx = int(x - min_x)
        ny = int(max_y - y)
        coord[ny][nx] = '*'
    
    return ["".join(row) for row in coord]