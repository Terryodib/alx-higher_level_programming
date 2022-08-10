-- creates a table
-- for each row, which is never empty when a value isn't give
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
);
