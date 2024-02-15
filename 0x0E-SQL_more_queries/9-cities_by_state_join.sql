-- a script that lists all cities contained in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN hbtn_0d_usa.states ON states_id = cities.state_id ORDER BY cities.id;

