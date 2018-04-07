CREATE DATABASE IF NOT EXISTS `vmail`;
USE `vmail`;

--
-- Table structure for table `aliases`
--

CREATE TABLE `aliases` (
  `mail` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  PRIMARY KEY (`mail`)
) DEFAULT CHARSET=utf8;

--
-- Table structure for table `senders`
--

CREATE TABLE `senders` (
  `sender` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  PRIMARY KEY (`sender`)
) DEFAULT CHARSET=utf8;

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `active` tinyint(4) NOT NULL,
  PRIMARY KEY (`username`)
) DEFAULT CHARSET=utf8;
