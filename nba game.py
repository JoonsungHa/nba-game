import random

#prints out the name in a string rather than a list
def show_name(lst):
    name = ""
    for i in lst:
        i += " "
        name += i

    return name


def different_options(current_ball_handler):
    print(current_ball_handler + "can either pass, drive, or shoot")
    action = input("What does " + current_ball_handler + "choose to do: ")

    return action



#chance_of_making will have the function of the shooting splits in it
def chance_of_making(player,type_of_shot):
    data = open("player_stats.txt","r")

    shooting_splits = []
    #print("THE PLAYER",player)
    for line in data:
        x = line.split()
        #print("XX",x)
        if x != [] and x[1:] == player:
            break
            
    #this is 3 right now because I only have three, midrange, and layup
    for i in range(3):
        line = data.readline()
        line = line.split()
        shooting_splits.append(line)
    #print("shooting_splits",shooting_splits)

    #three different shots
    if type_of_shot.lower() == "three":
        return making_three(shooting_splits)

    elif type_of_shot.lower() == "midrange":
        return making_midrange(shooting_splits)

    elif type_of_shot.lower() == "layup":
        return making_layup(shooting_splits)




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
    #tis is me making my own algorithim
    make_layup = layup_rating - 20

    chance = random.randint(1,100)
    print("chance",chance)
    print("make_layup",make_layup)

    score = 0
    if make_layup >= chance:
        return score + 2 
    else:
        return score
    

    



def play(current_ball_handler,action):

    while action.lower() == "pass":
        current_ball_handler = input("Who do you want pass it to:")
        #this makes it into a list
        current_ball_handler = current_ball_handler.split()
        print(show_name(current_ball_handler) + "can either pass, drive, or shoot")
        action = input("What does " + show_name(current_ball_handler) + "choose to do: ")

    if action.lower() == "drive":
        pass

    elif action.lower() == "shoot":
        type_of_shot = input("What type of shot do you want to shoot: ")
        return chance_of_making(current_ball_handler,type_of_shot)

       
    


def main():

    data = open("nba.txt","r")

    #Now I want the user to choose which team they want to play as
    desired_team_1 = "Golden State Warriors"
    #input("What team do you want to play as? ")
    desired_team_2 = "Phoenix Suns"
    #input("What team do you want to go against? ")

    desired_team_1 = desired_team_1.split()
    desired_team_2 = desired_team_2.split()
    print(desired_team_1)
    print(desired_team_2)
    #for now lets do this
    

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
            #this gets the players names
            #elif x[0] == "Pg:" or x[0] == "Sg:" or x[0] == "Sf:" or x[0] == "Pf:" or x[0] == "C:":
                #team_1_players.append(show_name(x[1:]))

    #this is showing the two different teams that are playing
    #team_1 = show_name(team_1_lst)
    #team_2 = show_name(team_2_lst)
    print("team_1",team_1_lst)
    print("team_2",team_2_lst)

    #this seperates the teams to their respective teams
    print("team_1_players",team_1_players)
    print("team_2_players",team_2_players)
    
    #this keeps track of the score
    team_1_points = 0
    team_2_points = 0



    #now I have to put this in a loop
    
    #shows the current status of the game
    current_ball_handler = team_1_players[0]
    current_team = show_name(team_1_lst[0])
    current_team_score = team_1_points

    
    print("The current team with the ball is the", current_team)
    print("The current ball handler is",current_ball_handler)


    
    #for now lets assume that the action is to shoot
    print(current_ball_handler + "can either pass, drive, or shoot")
    action = input("What does " + current_ball_handler + "choose to do: ")

    print(play(current_ball_handler,action))



    


main()
