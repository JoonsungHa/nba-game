import random

#prints out the name in a string rather than a list
def show_name(lst):
    name = ""
    for i in lst:
        i += " "
        name += i

    return name




#this function gets all the stats of the player choosen
def stats(player):
    data = open("player_stats.txt","r")

    #if this is a string I have to do this
    #Stephen curry is not in a list
    if type(player) != list:
        player = player.split()
    

    shooting_splits = []
    for line in data:
        x = line.split()
        #print("XX",x)
        #I have to do x[1:] because it does Player: Anthony Davis
        if x != [] and x[1:] == player:
            break
            
    #this is 3 right now because I only have three, midrange, layup, and steal
    for i in range(4):
        line = data.readline()
        line = line.split()
        shooting_splits.append(line)

    return shooting_splits




#chance_of_making will have the function of the shooting splits in it
def chance_of_making(player,type_of_shot):
    
    shooting_splits = stats(player)

    #three different shots
    if type_of_shot.lower() == "three":
        #I manually have the three rating in the making_three function
        #shooting splits has all the ratings
        return making_three(shooting_splits)

    elif type_of_shot.lower() == "midrange":
        return making_midrange(shooting_splits)

    elif type_of_shot.lower() == "layup":
        return making_layup(shooting_splits)





#chance of getting a steal
#calculates the steal rate of a player
#player_1 is the player with the ball
#I am going to give the function a list with all the players
#team_1_players ['Stephen Curry ', "D'Angelo Russell ", 'Klay Thompson ', 'Draymond Green ', 'Kevon Looney ']
#team_2_players ['Ricky Rubio ', 'Devin Booker ', 'Mikal Bridges ', 'Kelly Oubre Jr. ', 'Deandre Ayton ']
#Turnover gives the right player
######## THIS makes sure I can pass it to the right player
def turnover(player_1,team_1_players,team_2_players):

    #use .index(name of the player)
    print("player_1",player_1)
    player_1 += " "
    print("team_1_players",team_1_players)


    if player_1 in team_1_players:
        x = team_1_players.index(player_1)
        current_ball_defender = team_2_players[x]
        shooting_splits = stats(current_ball_defender)
        return making_steal(shooting_splits)

        
    elif player_1 in team_2_players:
        x = team_2_players.index(player_1)
        current_ball_defender = team_1_players[x]
        shooting_splits = stats(current_ball_defender)
        return making_steal(shooting_splits)






def making_three(stats):
    #this correctly gets the three pointer rating
    three_rating = stats[0][2]
    #convert the string into an integer
    three_rating = int(three_rating)
    #now I have the make the algorithim to decide how likely it is to make a three pointer
    make_three = three_rating/2

    #this is generating the random value
    chance = random.randint(1,100)
    print("chance",chance)
    print("make_three",make_three)

    score = 0

    if make_three >= chance:
        return score + 3
    else:
        return score

    


def making_midrange(stats):
    midrange_rating = stats[1][2]
    #convert the string into an integer
    midrange_rating = int(midrange_rating)
    #this one has a +25 because the midrange is overall easier to make than a three
    make_midrange = midrange_rating/2 + 25

    chance = random.randint(1,100)
    print("chance",chance)
    print("make_midrange",make_midrange)

    score = 0
    if make_midrange >= chance:
        return  score + 2
    else:
        return score



def making_layup(stats):
    layup_rating = stats[2][2]
    #convert the string into an integer
    layup_rating = int(layup_rating)
    #this is me making my own algorithim
    make_layup = layup_rating - 20

    chance = random.randint(1,100)
    print("chance",chance)
    print("make_layup",make_layup)

    score = 0
    if make_layup >= chance:
        return score + 2 
    else:
        return score
    


#I have to get the steal rating of the defender and not the current ball handler
def making_steal(stats):
    #its [3][1] because there are only two items in that list
    #print("stats",stats)
    steal_rating = stats[3][1]
    print("steal_rating",steal_rating)
    #convert the string into an integer
    steal_rating = int(steal_rating)
    #this is me making my own algorithim
    make_steal = steal_rating/10

    chance = random.randint(1,100)
    print("chance",chance)
    print("make_steal",make_steal)

    #I have to figure out what value to return
    #have to return the player who now has the ball
    #I will assume the player with the deflection will have control of the ball
    if make_steal >= chance:
        return False

    else:
        return True




#this function will give the likelihood of a rebound after a player misses a shot
#how should i decide on how rebounding works????
#defensive and offensive rebounding might have to be in two different functions
def getting_defensive_rebound(stats,opposing_team):

    opposing_team_pg = opposing_team[0]
    opposing_team_sg = opposing_team[1]
    opposing_team_sf = opposing_team[2]
    opposing_team_pf = opposing_team[3]
    opposing_team_c = opposing_team[4]


    shooting_splits_pg = stats(opposing_team_pg)
    shooting_splits_sg = stats(opposing_team_sg)
    shooting_splits_sf = stats(opposing_team_sf)
    shooting_splits_pf = stats(opposing_team_pf)
    shooting_splits_c = stats(opposing_team_c)


    pass




def getting_offensive_rebound(stats,current_team):

    current_team_pg = current_team[0]
    current_team_sg = current_team[1]
    current_team_sf = current_team[2]
    current_team_pf = current_team[3]
    current_team_c = current_team[4]


    shooting_splits_pg = stats(current_team_pg)
    shooting_splits_sg = stats(current_team_sg)
    shooting_splits_sf = stats(current_team_sf)
    shooting_splits_pf = stats(current_team_pf)
    shooting_splits_c = stats(current_team_c)


    pass





#team_1_players ['Stephen Curry ', "D'Angelo Russell ", 'Klay Thompson ', 'Draymond Green ', 'Kevon Looney ']
#team_2_players ['Ricky Rubio ', 'Devin Booker ', 'Mikal Bridges ', 'Kelly Oubre Jr. ', 'Deandre Ayton ']
def play(current_ball_handler,action,team_1_players,team_2_players):

    stays = True

    while action.lower() == "pass" and stays == True:
        #I have to make sure you can only pass to your team
        current_ball_handler = input("Who do you want pass it to:")
        #current_ball_handler = current_ball_handler.split()



        #run the turnover function here to see if the pass was successful 
        stays = turnover(current_ball_handler,team_1_players,team_2_players)



        if stays == True:
            #this makes it into a list
            current_ball_handler = current_ball_handler.split()
            print(show_name(current_ball_handler) + "can either pass or shoot")
            action = input("What does " + show_name(current_ball_handler) + "choose to do: ")


    if stays == False:
        #the ball has to go to the other team
        return 0


    
    elif action.lower() == "drive":
        pass

        #my number one priority
        #I have to work on the drive option!!!



    elif action.lower() == "shoot":
        print("You can shoot a layup, midrange, or three")
        type_of_shot = input("What type of shot do you want to shoot: ")

        return chance_of_making(current_ball_handler,type_of_shot)

        #I have to put the rebounding function here





def winner(team_1_points,team_2_points,team_1_lst,team_2_lst):

    if team_1_points > team_2_points:
        print(show_name(team_1_lst),"has won")

    elif team_1_points < team_2_points:
        print(show_name(team_2_lst), "has won")

    else:
        print(show_name(team_1_lst),"and", show_name(team_2_lst), "have tied")
       




def main():

    data = open("nba.txt","r")

    #Now I want the user to choose which team they want to play as
    desired_team_1 = input("What team do you want to play as? ")
    desired_team_2 = input("What team do you want to go against? ")

    desired_team_1 = desired_team_1.split()
    desired_team_2 = desired_team_2.split()


    team_1_lst = []
    team_2_lst = []
    team_1_players = []
    team_2_players = []

    for line in data:
        x = line.split()
        if x != []:
            #this gets the team names
            if x[0] == "Team:" and x[1:] == desired_team_1:
                team_1_lst.append(x[1:])
                x = data.readline()
                x = x.split()
                while x != []:
                    team_1_players.append(show_name(x[1:]))
                    x = data.readline()
                    x = x.split()

            elif x[0] == "Team:" and x[1:] == desired_team_2:
                team_2_lst.append(x[1:]) 
                x = data.readline()
                x = x.split()
                while x != []:
                    team_2_players.append(show_name(x[1:]))
                    x = data.readline()
                    x = x.split()


    #to make this into a 1D list
    team_1_lst = team_1_lst[0]
    team_2_lst = team_2_lst[0]
    #print("TEAM",team_1_players)
    print("team_1",show_name(team_1_lst))
    print("team_2",show_name(team_2_lst))

    #this seperates the teams to their respective teams
    #I can make this neater later
    print("team_1_players",show_name(team_1_players))
    print("team_2_players",show_name(team_2_players))
    
    #this keeps track of the score
    team_1_points = 0
    team_2_points = 0
    

    
    #in this scenario team 1 starts with the ball
    #shows the current status of the game
    #need to keep track of the time left in the game
    for i in range(5):
        current_ball_handler = team_1_players[0]
        current_team = show_name(team_1_lst)
        current_team_score = team_1_points

        
        print("The current team with the ball is the", current_team)
        print("The current ball handler is",current_ball_handler)


        
        #for now lets assume that the action is to shoot
        print(current_ball_handler + "can either pass or shoot")
        action = input("What does " + current_ball_handler + "choose to do: ")


        #going to make it tell if the player missed the shot or not
        before_the_shot = team_1_points


        team_1_points += play(current_ball_handler,action,team_1_players,team_2_players)


        #going to make it tell if the player missed the shot or not
        ##########DOES NOT DIFFERENTIATE BETWEEN TURNOVER AND MISSED SHOTS
        if before_the_shot < team_1_points:
            print(current_ball_handler + "made the shot")
        else:
            print(current_ball_handler + "missed the shot")


        print(show_name(team_1_lst) + "has", team_1_points, "points")



        ########################
        ########################



        print("Now the other team has the ball")
        current_ball_handler = team_2_players[0]
        current_team = show_name(team_2_lst)
        current_team_score = team_2_points

        
        print("The current team with the ball is the", current_team)
        print("The current ball handler is",current_ball_handler)


        
        #for now lets assume that the action is to shoot
        print(current_ball_handler + "can either pass or shoot")
        action = input("What does " + current_ball_handler + "choose to do: ")


        #going to make it tell if the player missed the shot or not
        before_the_shot = team_2_points


        team_2_points += play(current_ball_handler,action,team_1_players,team_2_players)


        #going to make it tell if the player missed the shot or not
        if before_the_shot < team_1_points:
            print(current_ball_handler + "made the shot")
        else:
            print(current_ball_handler + "missed the shot")



        print(show_name(team_2_lst) + "has", team_2_points, "points")
    


    #What do I have to do next?
    #Show the box score and who won the game
    winner(team_1_points,team_2_points,team_1_lst,team_2_lst)




    #Later I want to work on rebouding
    #find the probability of rebounding offensive and defensive 
    


main()