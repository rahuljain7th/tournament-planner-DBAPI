from tournament import *
import random

def create_random_matches():
    conn = connect();
    db_cursor = conn.cursor()
    query = "select * from players"
    db_cursor.execute(query)
    list_players = db_cursor.fetchall()
    player_id_list = [j[0] for j in list_players]
    for i in range(10):
        player_matches = random.sample(player_id_list, 2)
        print player_matches
        winner = player_matches[0]
        loser = player_matches[1]
        matchquery = "INSERT into matches (winner,loser) VALUES (%s,%s)"
        db_cursor.execute(matchquery,(winner,loser))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    deletePlayers()
    registerPlayer("Rahul")
    registerPlayer("Adarsh")
    registerPlayer("Vijay")
    registerPlayer("Shinoy")
    registerPlayer("Pranjal")
    registerPlayer("Sunil")
    create_random_matches()
    print "Success!  All tests pass!"
