-- a script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, state.name
FROM cities
JOIN states ON cities.states_id = cities.state_id ORDER BY cities.id;
