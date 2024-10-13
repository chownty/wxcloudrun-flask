-- flask_demo.counters definition
CREATE DATABASE IF NOT EXISTS flask_demo;
USE flask_demo;

CREATE TABLE `Counters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `count` int NOT NULL DEFAULT '1',
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;