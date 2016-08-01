import random
card_type = ['D' , 'S' , 'H' , 'C']
value = ['A', 2 , 3, 4 , 5, 6, 7, 8 , 9, 10 , 'J' , 'Q' , 'K']
card_point = 0
player_point = 0
dealer_point = 0
player_card = 0
dealer_card = 0
bet = 1
pocket = 100
chance = 0
playing = True
def welcome():
  
        play = raw_input('Would you like to play , Y or N ? :')
        if play == 'Y':
            print "Good , come along"
            gender =raw_input('If Male press M , if Female press F : ')
            if gender == 'M':
                print 'Welcome to Casino Royale , Sir !'
            else:
                 print 'Welcome to Casino Royale , Madam !'

def make_bet():
    
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    bet = 0
    
    print ' What amount of chips would you like to bet? (Enter whole integer please) '
    while bet == 0:
        in_hand = raw_input() 
        in_hand= int(in_hand)
        if in_hand >= 1 and in_hand <= pocket:
            bet = in_hand
        else:
            print "Invalid bet, you only have " + str(pocket) + " remaining"
            
def random_cards():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    card_random =(random.choice(value)) 
    card_type_random =(random.choice(card_type))
    if card_random == 'J' or card_random == 'Q' or card_random == 'K':
        card_point = 10
    elif card_random == 'A':
        a_condition()
    else:
        card_point=card_random
    print card_random , card_type_random

def deal_cards():
    global player_point , dealer_point , random_cards , card_point , pocket , bet , chance
    print "Player First card  :"
    random_cards()
    player_point += card_point
    print "Player Point :%s" %player_point
    
    print 'Dealer Card'
    random_cards()
    dealer_point += card_point
    print "Dealer Point : %s" %dealer_point
    
    print "Player First card  :"
    random_cards()
    player_point += card_point
    print "Player Point :%s" %player_point
    

def second_play():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    chance = raw_input('Would you like to hit or stay sir , H for hit and S for stay')
    if chance == 'H':
        hit()
    else:
        stay()
    
    
def hit():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    while chance == 'H' and player_point <= 21: 
        print "One more card Sir :"
        random_cards()
        player_point += card_point
        
        print "Player point now is : %s" %player_point
        if player_point <= 21:
            chance = raw_input('Would you like to hit or stay sir , H for hit and S for stay : ' )     
    else:
       
        draw()
        print "You lose sir"
        pocket -=bet 
        print 'Player has : %s' %pocket
        player_point = 0
        dealer_point = 0
        restart()
        
def win ():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    if dealer_point > player_point and dealer_point <=21:
        print "Dealer Wins : %s" %dealer_point
        pocket -= bet
        print 'Player has : %s' %pocket
        restart()
    elif player_point > dealer_point and player_point <=21:
        print "Player Wins : %s" %player_point
        pocket += bet
        print 'Player has : %s' %pocket
        player_point = 0
        dealer_point = 0
        restart()
def stay():
        global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
        print "Ok Sir , Nice call"
        print "Dealer Card"
        random_cards()
        dealer_point += card_point
        print "Dealer point is :%s" %dealer_point
        while dealer_point <17:
            print "l will Hit sir"
            random_cards()
            dealer_point +=card_point
            print "Dealer point : %s" %dealer_point
            if dealer_point >=17 and dealer_point <= 21:
                draw()
                
        else:
            draw()
            print 'Dealer lost'
            pocket += bet
            print 'Player has : %s' %pocket 
            player_point = 0
            dealer_point = 0
            restart()

def draw():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    if player_point == dealer_point:
        print "Its a draw Sir , we both win"
        
def a_condition():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance
    bang = input('What value for A you want - 1 or 11 Sir : ')
    if bang == 1:
        card_point = 1
    else:
        card_point = 11
        
def restart():
    global player_point , dealer_point , random_cards , card_point , pocket , bet ,chance , playing
    res = raw_input("Press D to continue Q to quit :" )
    if res == 'D':
        playing = True
    else:
        print 'Thanks for playing sir'
        playing = False
        quit()
    player_point = 0
    dealer_point = 0
        
def quit():
    exit()

welcome()
while playing == True:
    make_bet()
    deal_cards()
    second_play()