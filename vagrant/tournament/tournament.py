#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2



def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect();
    db_cursor = conn.cursor()
    db_cursor.execute("DELETE from matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect();
    db_cursor = conn.cursor()
    db_cursor.execute("DELETE from players;")
    conn.commit()
    conn.close()



def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect();
    db_cursor = conn.cursor()
    db_cursor.execute("select count(*) from players;")
    count = db_cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect();
    db_cursor = conn.cursor()
    query = "INSERT into players (player_name) VALUES (%s)"
    db_cursor.execute(query,(name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect();
    db_cursor = conn.cursor()
    db_cursor.execute("select players.id,player_name,count(case when matches.winner=players.id then 1 end) as wintotal ,count(case when matches.winner=players.id or matches.loser=players.id then 1 end) as totalgames"
+" from matches  right outer join players on matches.winner=players.id or matches.loser=players.id group by players.id order by wintotal desc;")
    list_players = db_cursor.fetchall()
    conn.commit()
    conn.close()
    return list_players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect();
    db_cursor = conn.cursor()
    matchquery = "INSERT into matches (winner,loser) VALUES (%s,%s)"
    db_cursor.execute(matchquery,(winner,loser))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    db_cursor = conn.cursor();
    db_cursor.execute("select * from players_standings")
    list_players = db_cursor.fetchall()
    swiss_pairList = []
    conn.commit()
    conn.close()
    iterate_players = iter(list_players)
    for player in iterate_players:
        pairedPlayer = next(iterate_players)
        swiss_pairList.append((player[0],player[1],pairedPlayer[0],pairedPlayer[1]))
    return swiss_pairList

