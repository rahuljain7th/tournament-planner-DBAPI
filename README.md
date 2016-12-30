#Project - Tournament Planner DATABASE API
================================
UNIX BOX SET UP VAGRANT 
1. Install vagrant and virtual box
2. Change directory to the vagrant directory in git bash for windows
3. Run Vagrant up command.
4. Run Vagrant ssh to log in to your newly installed Linux VM!

#DATABASE SETUP
1. open new git bash Window (This Terminal will be used for databased queries)
2. Run Vagrant ssh command
3. Run PSQL Command to enter sql terminal
4. Run \i tournament.sql . This will run the queries present in sql.It will create tournament Database,Will create matches and Players table,will create players_standings view.

#Shortcuts:
psql: to enter into database
\q : To Quit From Database
\l : List All Database
\c tournament: connect to tournament database
\dt : List All Table in Databases.
\i tournament.sql :  executes the sql commands within the sql file from psql
\? : get Help with psql commands

#Tournament.py File Methods:
1.connect --> will connect to database tournament
2.deleteMatches --> Remove all the match records from the database.
3.deletePlayers -->Remove all the player records from the database.
4.countPlayers ---> Returns the number of players currently registered.
5.registerPlayer --> Add players to database.
6.playerStandings --> Returns a list of the players and their win records, sorted by wins
7.reportMatch ---> Records the outcome of a single match between two players
8.swissPairings ---> Returns a list of pairs of players for the next round of a match

#UNIT TEST FILE: 
tournament_test containes a unit test method to test tournament.py method.
