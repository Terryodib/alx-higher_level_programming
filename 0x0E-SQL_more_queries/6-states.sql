-- creates database
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
-- switch the database
USE hbtn_0d_usa;
-- creates a table with a column that has auto increment
-- and as a primary key
CREATE TABLE IF NOT EXISTS states (
	  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  name VARCHAR(256) NOT NULL,
	  UNIQUE(id)
	);
