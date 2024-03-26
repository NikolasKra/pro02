n=3
m=3
matrix= []
for i in range(n):
   matrix.append([" "]*3)
 
def pole():
   print(f"  0 1 2")
   print(f"0 {matrix [0][0]} {matrix [0][1]} {matrix [0][2]} ")
   print(f"1 {matrix [1][0]} {matrix [1][1]} {matrix [1][2]} ")
   print(f"2 {matrix [2][0]} {matrix [2][1]} {matrix [2][2]} ")
pole()

def pro_ver():
   vvod = input("   Ваш ход: ")
   x,y = map(int,vvod.split())
   rez = False
   if 0 <= x <=2 and 0<= y <=2:
      if matrix[x][y] == " ":
         rez = True
    
      else:
         print( " занято введите другое поле")
   
   else:
      print(" за пределами поля")
   return x,y,rez


def dubl ():
   num = 0 
   while True:
      num+=1
      pole()
      po_b = "x"  
      if num % 2!=0: 
         print("ходит крест")
      else:
         po_b = "0"
         print("ходит ноль")

      x, y,rez = pro_ver()
      while not rez:
         x, y,rez = pro_ver() 
    
      a_dig = True   
      b_dig = True
      matrix[x][y] = po_b
      for i in range(n):
         row = True
         cols = True 
         for j in range(m):
            if j == i and matrix[j][i] != po_b:
               a_dig = False
            if j == i and matrix[j][m-i-1] != po_b:
               b_dig = False
            if matrix[j][i] != po_b:
               cols = False
            if matrix[i][j] != po_b:
               row = False
         if row ==True or cols == True:
            print('выиграл игрок:' ,po_b)
            return


      if a_dig == True or b_dig == True:
         
         print('выиграл игрок:' ,po_b)
         return
         
      if num == 9:
         print("Ничья")
         return
dubl()
            
      
      

         
        
      