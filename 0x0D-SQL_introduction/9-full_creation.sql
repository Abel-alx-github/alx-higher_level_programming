-- creates a table second_table

CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT)
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10), (1, "Alex", 3), (2, "Bob", 14), (3, "George", 8);
