# MA1008-Introduction-to-Computational-Thinking
**Project Title: A Badminton Ladder**

This is a data management project with graphical display. You are to write a program for managing a badminton ladder, which is a form of badminton competition where the players are placed in an ordered list and challenge players higher in the order. Here are the rules in operating the ladder:

i. A player on the ladder may challenge another player up to three places above. A challenge to players beyond three places above is forbidden.

ii. If the challenger wins, then s/he moves into the position of the challenged. The challenged and the players in between each moves down the ladder by one place. Other players are not affected.

iii. If the challenger loses, the ladder remains unchanged.

iv. A new player joins the ladder at the bottom.

v. When a player leaves, everyone below moves up by one place to occupy the vacated spot.

**The program must:**

i. Provide means for a player to take one of these actions:

a. Issue a challenge (stating opponent and play-by date)

b. Record the result of a challenge

c. Join the ladder

d. Withdraw from the ladder

e. Make a query

ii. Provide means of recording and displaying the result of a challenge.

iii. Adjust the ladder according to the result.

iv. Register a new player and place him/her on the ladder.

v. Accept the withdrawal of a player from the ladder and update the ladder accordingly.

**Your program must produce a graphical display with these elements** (imagine this is a web page where players go for their information and conduct ladder business):

i. The ladder, with the first player on top and the last player at the bottom.

ii. Facilities for a player to take an action as stated above.

iii. A display showing the yet-to-play challenges.

iv. A means for making queries and displaying the answers. Your program should include these queries:

  a. The order of the ladder on a specific date
  
  b. The data of a specific challenge based on the names of the players
  
  c. The data of a specific challenge based on the date
  
  d. The list of matches a player has played, with all the associated data
  
  e. The most active player, i.e. the player with the most matches
  
  f. The least active player, i.e. the player with the least matches
  
  g. The list of matches played in a specific date range
  
  h. You may add more queries as you see fit
  
v. The data of the ladder are stored in the two data files specified below, and they must be updated as events take place.

vi. When the program runs, the display should show the current ladder order as well as the results of the latest n challenges (you may choose n, n >= 2).

**The Data Files**
The data of the ladder are in two files which are to be updated every time an action is taken. One file, **ladder.txt**, contains the current order of the ladder, which is an ordered list of the names of the players. The second file, **data.txt**, contains data on every challenge and the coming and going of players. The data are in chronological order, with the latest data inserted at the end of the file. Specifically, each line of this second file contains one of these three items:

i. The data on a challenge. The syntax of the line is:

Name of challenger p1 / Name of challenged p2/ date / scores

The “/” separates the different fields. The names are strings. p1 and p2 after the names are integers showing the current positions of the players on the ladder. The date format is DD-MM-YYYY, and the scores format is xx-yy, where xx and yy represent the numerical scores of the challenger and the challenged respectively. A match may have two or three of such scores. Example: CW Lee 5/M Frost 3/20-07-2000/20-22 18-21

If a score is missing from such a line, it means that the challenge has been issued but the match has not been played, and the date in the line is the play-by date. If this date is in the past, it means that the challenged has not taken up the challenge and therefore forfeits the match; the challenger is automatically the winner.
(Note: Badminton matches are played to the best of three games. The player reaching 21 points first in a game wins the game. If a game reaches 20-20, then the player leading by two points subsequently wins the game.)

ii. The name of a new player who joins and the date of joining, with a + sign before the name. Example: +NEW Player/18-05-2020

iii. The name of a player who leaves and his/her position on the ladder, and the date of leaving, with a – sign before the name. Example: -EX Player 12/18-05-2020

The existing data in ladder.txt contains the current order of the list of players in there. The data in data.txt contains the chronological record of the challenges, new players joining and existing players leaving to date. As your program runs, the data in these files will change.
