a = 0
b = 0
p = 1
print 'Lets play Tic tac Toe'
l = ['-','-','-','-','-','-','-','-','-']
print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8] 

def p1():
    global a,p,b
    b += 1
    x = input('Player one plays : ')
    while p == 1:
        if x == 1 and l[0]== '-':
            l[0] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 2 and l[1]== '-':
            l[1] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 3 and l[2]== '-':
            l[2] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 4 and l[3]== '-':
            l[3] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 5 and l[4]== '-':
            l[4] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 6 and l[5]== '-':
            l[5] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 7 and l[6]== '-':
            l[6] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 8 and l[7]== '-':
            l[7] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 9 and l[8]== '-':
            l[8] = 'X'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        else:
            print 'Error'
            p =1
            break
        p = 2
        
        
def p2():
    global a,p
    x = input('Player 2 plays : ')
    while p == 2:
        if x == 1 and l[0]== '-':
            l[0] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 2 and l[1]== '-':
            l[1] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 3 and l[2]== '-':
            l[2] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 4 and l[3]== '-':
            l[3] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 5 and l[4]== '-':
            l[4] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 6 and l[5]== '-':
            l[5] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 7 and l[6]== '-':
            l[6] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 8 and l[7]== '-':
            l[7] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        elif x == 9 and l[8]== '-':
            l[8] = '0'
            print l[0] , l[1] ,l[2] ,'\n', l[3] , l[4] , l[5] ,'\n' , l[6], l[7] , l[8]
        else:
            print 'Error'
            p = 2
            break
        p = 1
    
def win():
    global a
    if l[0] == ('X') and l[1] == ('X') and l[2] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[0] == ('0') and l[1] == ('0') and l[2] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[0] == ('X') and l[3] == ('X') and l[6] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[0] == ('0') and l[3] == ('0') and l[6] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[2] == ('X') and l[5] == ('X') and l[8] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[2] == ('0') and l[5] == ('0') and l[8] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[2] == ('X') and l[4] == ('X') and l[6] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[2] == ('0') and l[4] == ('0') and l[6] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[0] == ('X') and l[4] == ('X') and l[8] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[0] == ('0') and l[4] == ('0') and l[8] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[3] == ('X') and l[4] == ('X') and l[5] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[3] == ('0') and l[4] == ('0') and l[5] == ('0'):
        a = 1
        print 'Player 2 wins'
    elif l[6] == ('X') and l[7] == ('X') and l[8] == ('X'):
        a = 1
        print 'Player 1 wins'
    elif l[6] == ('0') and l[7] == ('0') and l[8] == ('0'):
        a = 1
        print 'Player 2 wins'

        
        
def draw():
    print 'Match is Draw'
       
while a==0 and b !=5:
    while p == 1:
        p1()
    win()
    while p == 2:
        if a == 0 and b !=5:
            p2()
        win()
    if b == 5 and a != 1:
        draw()