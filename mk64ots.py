# Project: 		Mario Kart 64: One Try Simulator
# Author:		Daniel "TheMadNad" Wynham
# Date:			November 12th, 2021
# Version:		0.1.2b
#
# Find source code updates at https://github.com/themadnad/mk64ots

# To be added in future versions:
#
# - Jokers
# - NTSC/PAL conversion and preference
# - More visible debug/time mode
# - Windows/Linux cross platform functionality
# - Fun "unlockables" for winning match for higher ranks
# - Improved time calculations

# About:
# 
# This is a project to assist with practicing Mario Kart 64  1-try matches. 
# Feel free to use this source code and have fun practicing 1-tries.
# I  will continue to update this code (It's fun to make things and  tinker with Python). 
# If you have any suggestions or updates, please let me know. I hope together we can 
# make this a useful tool for anyone who wants to practice MK64.



# Many thanks and credit to:
#
# The MK64 speedrun community discord
# MarioKart64.com for the great resources and times
# Nintendo



# importing stuff
import os
import random


# Define variables
version = '0.1.2b'			# next version 0.1.3



# Toggle debug mode. This can be used to test generating times quickly without racing.
debug = False
debug_message = ''


# Basetimes
# This is a double array of all the lowest times per standard. 
# Columns are ranks from God to Newbie, and rows are tracks from LR to RRd. Time is measured in 1/100s of a second in NTSC
basetimes = [[9879, 9897, 9989, 10087, 10209, 10265, 10345, 10427, 10519, 10639, 10859, 11179, 11599],
[7389, 7411, 7534, 7687, 7747, 7788, 7839, 7919, 8039, 8259, 8559, 8859, 9179],
[8095, 8116, 8229, 8399, 8614, 8691, 8775, 8883, 9039, 9259, 9599, 10139, 10859],
[10539, 10561, 10672, 10811, 11019, 11124, 11255, 11405, 11579, 11859, 12159, 12479, 12859],
[14999,	15035, 15213, 15387, 15551, 15616, 15707, 15839, 16059, 16399, 16899, 17419, 18019],
[10099,	10147, 10361, 10489, 10664, 10745, 10859, 11039, 11259,	11579, 11979, 12399, 12939],
[9799, 9829, 9964, 10053, 10185, 10269,	10379, 10539, 10759, 11079,	11479, 11899, 12439],
[7449, 7461, 7522, 7645, 7782, 7847, 7919, 8039, 8239, 8439, 8659, 8999, 9519],
[22099,	22159, 22454, 22776, 23203,	23316, 23479, 23719, 24099,	24619, 25279, 26199, 27199],
[9849, 9875, 10001,	10141, 10369, 10474, 10605,	10773, 11019, 11399, 11939,	12639, 13279 ],
[14499,	14533, 14695, 14879, 15215,	15303, 15434, 15619, 15859,	16179, 16599, 17139, 17779],
[11199,	11227, 11359, 11491, 11719,	11829, 11999, 12259, 12579,	12979, 13419, 14099, 15119],
[11399,	11459, 11732, 11913, 12127,	12229, 12399, 12659, 12979,	13399, 13939, 14639, 15279],
[8749, 8789, 8979, 9159, 9419, 9539, 9759, 10079, 10499, 11019,	11639, 12359, 13199],
[10549, 10573, 10693, 10871, 11209,	11274, 11339, 11439, 11659,	11979, 12399, 12939, 13699],
[29899,	29927, 30259, 30739, 31119,	31239, 31439, 31659, 31979,	32439, 33199, 34199, 35199]]


# Track short names
tracks = 'LR','MM','KB','KD','TT','FS','CM','MR','WS','SL','RRy','BC','DK','YV','BB','RRd'

# Track variance in 1/100s of a second per track. (250 means 2.5 seconds)
trackvariance = [250,550,1050,350,550,1250,350,250,1250,950,450,1750,1750,3050,750,250]

# Chance out of 100 that opponent hits a track variant.
trackvariancechance = [15, 40, 25, 20, 25, 35, 20, 20, 20, 35, 25, 40, 40, 50, 30, 15]

# Base variance based on rank. (1.5 seconds for God, 10 seconds for Newbie)
rank_basetime = [150,250,250,250,350,350,350,450,450,550,700,850,1000]

default_rank = 8
opponent_rank = default_rank


# Function to generate time based on rank and track
def generate_time(opponent_rank, track_choice):
    debug_message = ''
    opponent_time = basetimes[int(track_choice)][int(opponent_rank)]                # Pull the base time
    random_base = int(random.uniform(0,1) * rank_basetime[opponent_rank])           # Generate additional time from 0 to the maximum base time for that track
    random_variance = int(random.uniform(0,1) * trackvariance[int(track_choice)])   # Generate variance time from 0 to maximum variance time for that track
    random_variance_chance = int(random.uniform(0,1) * 100)                         # Get random number from 0-100 for variance check.
    # debug stuff
    if(debug): 
        debug_message += '\nTrack Choice:'
        debug_message += str(track_choice)
        debug_message += '\nRank: '
        debug_message += str(opponent_rank)
        debug_message += '\nOpponent Time: '
        debug_message += str(opponent_time)
        debug_message += '\nBase Time: '
        debug_message += str(random_base)
        debug_message += '\nRandom Variance Chance: '
        debug_message += str(random_variance_chance)
        debug_message += '\nRandom Variance: '
        debug_message += str(random_variance)
    opponent_time += random_base
    if(trackvariancechance[int(track_choice)] > random_variance_chance):            # Check if variance hits
        opponent_time += random_variance
        if(debug): debug_message += '\n Variance Accepted'
    if(debug): print(debug_message)
    return opponent_time
    
    









def standard(rank):
    if(rank == 1): return 'God'
    if(rank == 2): return 'Legend'
    if(rank == 3): return 'King'
    if(rank == 4): return 'Elite'
    if(rank == 5): return 'Master'
    if(rank == 6): return 'Pro'
    if(rank == 7): return 'Semi-Pro'
    if(rank == 8): return 'Expert'
    if(rank == 9): return 'Advanced'
    if(rank == 10): return 'Intermediate'
    if(rank == 11): return 'Apprentice'
    if(rank == 12): return 'Beginner'
    if(rank == 13): return 'Newbie'

    



# Main Loop
def main():
    
    global opponent_rank
    global tracks
    global trackpool
    global your_tracks_completed
    global opp_tracks_completed
    global your_sets_completed
    global opp_sets_completed
    global debug_message
    running = True
    settings = False
    game = False
    race = False
    debug_menu = False
    your_choice = True      # By default, players track choice
    while(running):
        # clear screen
        os.system('clear')   # Note, if on Windows, change this to cls instead of clear. (Will add cross platform functionality later)
        print('Mario Kart 64: One Try Simulator!')
        print('Version:', version)
        print('\nOpponent rank is ', standard(opponent_rank))
        print('\n\n1) Begin One Try')
        print('2) Opponent Settings')
        if(debug):
            print('3) Debug Mode')
        print('q) Exit')
        menu_answer = input('\nChoice: ')
        os.system('clear')
        if(menu_answer == '1'): 
            game = True
            your_sets_completed = 0
            your_tracks_completed = 0
            opp_sets_completed = 0
            opp_tracks_completed = 0
            yourFLAP = True
            yourSC = True
            oppFLAP = True
            oppSC = True
            trackpool = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True] # This says if track is available or not 
        if(menu_answer == '2'): settings = True
        if(menu_answer == '3' and debug): debug_menu = True
        if(menu_answer == 'q' or menu_answer == 'Q'):running = False

        
        
        # Debug Menu
        while(debug_menu):
            print('~~~~~~~Debug Menu~~~~~~~~~\n\n')
            print('\nTracks available:')
            count = 0
            debug_message = ''
            for x in tracks:
                track_name = x
                if(count < 9):
                    print('', count + 1, ': ', track_name)
                else:
                    print(count + 1, ': ', track_name)
                count+=1
            print('Choose a track to generate a time. Press q to quit')
            track_choice = input('\nTrack: ')
            try:
                your_choice_value = int(track_choice)
                choice_valid = True
            except ValueError:
                choice_valid = False
            if(track_choice == 'q'): debug_menu = False
            if(choice_valid):
                count = 0
                for x in tracks:
                    if(int(track_choice) == (count + 1)): 
                        current_track = x
                        debug_time = generate_time(opponent_rank - 1, int(track_choice) - 1)
                        debug_seconds = int((debug_time/100)%60)
                        debug_minutes = int((debug_time/(100*60))%60)
                        debug_miliseconds = debug_time - (debug_seconds*100) - (debug_minutes * 6000)
                        debug_message += '\n Debug Time:   '
                        debug_message += str(debug_minutes)
                        debug_message += 'm '
                        debug_message += str(debug_seconds)
                        debug_message += 's '
                        debug_message += str(debug_miliseconds)
                        debug_message += 'ms \n'
                    count += 1
                print(debug_message)
                wait = input('\nPress ENTER to Continue ')
            os.system('clear')
        
        # Settings
        while(settings):
            #settings here
            print('How strong is your opponent?\n\n')
            print(' 1: ', standard(1))
            print(' 2: ', standard(2))
            print(' 3: ', standard(3))
            print(' 4: ', standard(4))
            print(' 5: ', standard(5))
            print(' 6: ', standard(6))
            print(' 7: ', standard(7))
            print(' 8: ', standard(8))
            print(' 9: ', standard(9))
            print('10: ', standard(10))
            print('11: ', standard(11))
            print('12: ', standard(12))
            print('13: ', standard(13))
            print('\n')
            settings_answer = input('\nChoice: ')
            os.system('clear')
            for x in range(1, 14):
                #print(x)
                if(settings_answer == str(x)): 
                    opponent_rank = x
                    settings = False
        
        
        
        
        
        # Main Game Loop
        while(game):
           #game loop here
            print('@----------- Mario Kart One Try in Progress! -----------@')
            print('|                                                       |')
            print('|                 You          Opponent                 |')
            print('|                                                       |')
            print('|                                                       |')
            print('| Sets:          ', your_sets_completed, '               ', opp_sets_completed, '                  |')
            print('| Tracks:        ', your_tracks_completed, '               ', opp_tracks_completed, '                  |')
            print('|                                                       |')
            print('|                                                       |')
            print('@-------------------------------------------------------@')
            print('Opponent Rank: ', standard(opponent_rank))
            
            # If a track has been chosen and the race has been started
            if(race):
                print('\nCurrent Track:', current_track)
                print('\n\n\nWhen finished, enter you time in this format: MMSSms\n')
                time_input = input('Track Time: ')
                # Check if time is valid
                try:
                    time_value = int(time_input)
                    a,b,c,d,e,f = time_input
                    if(int(c) < 6): time_valid = True
                except ValueError:
                    time_valid = False
                
                if(time_valid):
                    a,b,c,d,e,f = time_input
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    d = int(d)
                    e = int(e)
                    f = int(f)
                    your_minutes = (a*10) + b
                    your_seconds = (c*10) + d
                    your_miliseconds = (e*10) + f
                    your_time = your_miliseconds + (your_seconds * 100) + (your_minutes * 60 * 100)
                    # This runs the function from earlier
                    opp_time = generate_time(opponent_rank - 1, int(track_choice) - 1)
                    opp_seconds = int((opp_time/100)%60)
                    opp_minutes = int((opp_time/(100*60))%60)
                    opp_miliseconds = opp_time - (opp_seconds*100) - (opp_minutes * 6000)
                    print('\n Your Time:        ', your_minutes, 'm ', your_seconds, 's ', your_miliseconds, 'ms')
                    print(' Opponents Time:   ', opp_minutes, 'm ', opp_seconds, 's ', opp_miliseconds, 'ms \n')
                    if(your_choice): your_choice = False
                    else: your_choice = True
                    if(your_time < opp_time):
                        your_tracks_completed += 1
                        if(your_tracks_completed > 3):
                            print('You win!! You also take the set!')
                            your_sets_completed += 1
                            your_tracks_completed = 0
                            opp_tracks_completed = 0
                            total_sets = opp_sets_completed + your_sets_completed
                            if(total_sets == 2 or total_sets == 4):
                                for x in range(0,16):
                                    trackpool[x] = True
                            your_choice = False
                        else: print('You Win!')
                        
                    else:
                        opp_tracks_completed += 1
                        if(opp_tracks_completed > 3):
                            print('Your Opponent wins and also takes the set.')
                            opp_sets_completed += 1
                            opp_tracks_completed = 0
                            your_tracks_completed = 0
                            total_sets = opp_sets_completed + your_sets_completed
                            if(total_sets == 2 or total_sets == 4):
                                for x in range(0,16):
                                    trackpool[x] = True
                            your_choice = True
                        else: print('Opponent Wins.')
                    wait= input('\n\nPress Enter to Continue ')
                    race = False
                os.system('clear') # or cls
                
            else:
                print('\nTracks available:')
                count = 0
                for x in tracks:
                    if(trackpool[count]):
                        track_name = x
                    else:
                        track_name = '--'
                    if(count < 9):
                        print('', count + 1, ': ', track_name)
                    else:
                        print(count + 1, ': ', track_name)
                    count+=1
                if(your_choice):
                    print('\nYour pick! Which track do you choose?')
                    track_choice = input('\nTrack: ')
                    os.system('clear')
                    try:
                        your_choice_value = int(track_choice)
                        choice_valid = True
                    except ValueError:
                        choice_valid = False
                    if(choice_valid):
                        count = 0
                        for x in tracks:
                            if(int(track_choice) == (count + 1) and trackpool[count] == True): 
                                trackpool[count] = False
                                current_track = x
                                race = True
                            count += 1
                else:
                    track_choice = 0
                    while(track_choice == 0):
                        opp_pick = int(random.uniform(0,16))
                        if(trackpool[opp_pick]): 
                            track_choice = opp_pick + 1
                            trackpool[opp_pick] = False
                            current_track = tracks[opp_pick]
                            race = True
                    print('\nOpponent choice!\nYour opponent has chosen next track:', current_track, '\n\n')
                    wait = input('\nPress Enter to Continue ')
                    os.system('clear')
            if(opp_sets_completed == 3):
                game = False
                print('\n\nYour opponent has won the match. Winning', opp_sets_completed, 'sets versus your', your_sets_completed,'. Better luck next time!')
                wait = input('\nPress Enter to Continue ')
                os.system('clear')
            if(your_sets_completed == 3):
                game = False
                print('\n\nYou win the match! You took', your_sets_completed,'sets versus your opponent who took', opp_sets_completed,'. Awesome job, and nice racing!')
                wait = input('\nPress Enter to Continue ')
        

main()