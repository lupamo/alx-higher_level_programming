-- a script that creates the database hbtn_0d_usa and the table state
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
