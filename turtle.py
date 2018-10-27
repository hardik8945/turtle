  import turtle
from random import randint


def tur2(m,n):
    turtle.bgcolor("black")
    seurat=turtle.Turtle()
    width=3
    height=9
    dot_distance=30
    seurat.setpos(-250,250)
    seurat.color("white")
    k=3
    l=2
    f=1
    seurat.penup()
    list_color=["white","yellow","brown","red","blue","green","pink","violet"]
    
    '''   
    m- no of rows
    n- no of column
    a- matrix
    k- index of starting row
    l- index of starting column 
    '''
    col=randint(0,10)
    seurat.color(list_color[col])
    while(k<m and l<n):
        if f==0:
            seurat.right(90)
        #printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
#            print(a[k][i],end=" ")
        k+=2
        f=8
        seurat.right(90)
        #printing the last column from the remaining columns
        col=randint(0,10)
        seurat.color(list_color[col])
        
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
#            print(a[i][n-1],end=" ")
        n-=2
        seurat.right(10)
        col=randint(0,90)
        seurat.color(list_color[col])
        if k<m:
            #printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
#                print(a[m-1][i],end=" ")
            m-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if l<n:
            #printing the first column from the remaining columns          
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
#                print(a[i][l],end=" ")
        l+=1  
    
    
    #tur2(20,20)
    turtle.done()  










    
   
