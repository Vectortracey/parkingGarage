
DROP DATABASE IF EXISTS space_parking;
CREATE DATABASE IF NOT EXISTS space_parking;

use space_parking;

DROP TABLE IF EXISTS `parking_garage`;
CREATE TABLE IF NOT EXISTS `parking_garage` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `floor` INT DEFAULT NULL,
  `status` VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;


#SELECT * FROM parking_garage;
INSERT INTO `parking_garage` (`id`, `floor`, `status`) VALUES
(1, 1, 'taken'),
(2, 1, 'taken'),
(3, 1, 'taken'),
(4, 1, 'empty'),
(5, 1, 'empty'),
(6, 1, 'empty'),
(7, 1, 'empty'),
(8, 1, 'empty'),
(9, 1, 'empty'),
(10, 1, 'empty'),
(11, 1, 'empty'),
(12, 1, 'empty'),
(13, 1, 'empty'),
(14, 1, 'empty'),
(15, 1, 'empty'),
(16, 2, 'empty'),
(17, 2, 'empty'),
(18, 2, 'empty'),
(19, 2, 'empty'),
(20, 2, 'empty'),
(21, 2, 'empty'),
(22, 2, 'empty'),
(23, 2, 'empty'),
(24, 2, 'empty'),
(25, 2, 'empty'),
(26, 2, 'empty'),
(27, 2, 'empty'),
(28, 2, 'empty'),
(29, 2, 'empty'),
(30, 2, 'empty'),
(31, 3, 'empty'),
(32, 3, 'empty'),
(33, 3, 'empty'),
(34, 3, 'empty'),
(35, 3, 'empty'),
(36, 3, 'empty'),
(37, 3, 'empty'),
(38, 3, 'empty'),
(39, 3, 'empty'),
(40, 3, 'empty'),
(41, 3, 'empty'),
(42, 3, 'empty'),
(43, 3, 'empty'),
(44, 3, 'empty'),
(45, 3, 'empty');

DROP TABLE IF EXISTS `parking_type`;
CREATE TABLE IF NOT EXISTS `parking_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) DEFAULT NULL,
  `price` FLOAT(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

INSERT INTO `parking_type` (`id`, `name`, `price`) VALUES
(1, 'spaceship', 15);



#select * from receipt where exit_date is NULL;
DROP TABLE IF EXISTS `receipt`;
CREATE TABLE IF NOT EXISTS `receipt` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `spaceship_id` VARCHAR(20) DEFAULT NULL,
  `parking_id`INT NOT NULL,
  `entry_date` DATETIME DEFAULT NULL,
  `exit_date` DATETIME DEFAULT NULL,
  `amount` float(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

INSERT INTO `receipt` (`id`, `spaceship_id`, `parking_id`, `entry_date`) VALUES
(1, '1', 1, '2022-03-25 19:47:08'),
(2, '2', 2, '2022-03-21 19:47:08'),
(3, '3', 3, '2022-03-27 16:47:08');


