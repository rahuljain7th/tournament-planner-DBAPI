-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament
CREATE TABLE players (id SERIAL primary key,player_name TEXT);

CREATE TABLE matches (id SERIAL primary key,winner INTEGER REFERENCES players(id),loser INTEGER REFERENCES players(id));

CREATE view players_standings as
select players.id,player_name,count(case when matches.winner=players.id then 1 end) as wintotal ,count(case when matches.winner=players.id or matches.loser=players.id then 1 end) as totalgames
from matches  right outer join players on matches.winner=players.id or matches.loser=players.id group by players.id order by wintotal desc;