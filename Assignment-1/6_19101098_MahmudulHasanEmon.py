#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Task 1

horz=4
vert=5
p=[[0 for i in range(vert+1)]
    for j in range(horz+1)]
digit=0
result=0
height=0
m=[-1,-1,-1,0,0,1,1,1]
n=[-1,0,1,-1,1,-1,0,1]
def dfs(a, b, q, x, y):    
    global digit, height, result
    p[a][b] = id
    height += 1    
    if (height > result):
        x = a
        y = b
        ressult = height
    for j in range(8):
        cx = a + m[j]
        cy = b + n[j]
        if (cx < 0 or cy < 0 or 
            cx >= horz or cy >= vert or 
            q[cx][cy] == 'N' or p[cx][cy]):
            continue
        dfs(cx, cy, q, x, y)              
    p[a][b] = 0    
    height -= 1
    return x, y
def findMaximumHeight(q):
    global digit, height, result
    x = 0
    y = 0
    digit += 1    
    height = 0
    result = 0
    for i in range(horz):
        for j in range(vert):
            if (q[i][j] != 0):
                x, y = dfs(i, j, q, x, y)
                i = horz
                break
    digit += 1
    height = 0
    result = 0
    x, y = dfs(x, y, q, x, y)
    print(result)
    
if __name__=="__main__":
    grid= [['Y','Y','N','N','N'],
           ['N','Y','Y','N','N'],
           ['N','N','Y','N','N'],
           ['Y','N','N','N','N']]
    findMaximumHeight(grid)


# In[ ]:




