-- MySQL dump 10.13  Distrib 5.7.16, for osx10.11 (x86_64)
--
-- Host: localhost    Database: eplApi
-- ------------------------------------------------------
-- Server version	5.7.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Defenders`
--

DROP TABLE IF EXISTS `Defenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Defenders` (
  `id_defender` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `clean_sheets` varchar(45) DEFAULT NULL,
  `goals_conceded` varchar(45) DEFAULT NULL,
  `tackles` varchar(45) DEFAULT NULL,
  `tackle_success` float DEFAULT NULL,
  `player_id_def` int(11) DEFAULT NULL,
  `last_man_tackles` varchar(45) DEFAULT NULL,
  `blocked_shots` varchar(45) DEFAULT NULL,
  `interceptions` varchar(45) DEFAULT NULL,
  `clearances` varchar(45) DEFAULT NULL,
  `recoveries` varchar(45) DEFAULT NULL,
  `duels_won` varchar(45) DEFAULT NULL,
  `duels_lost` varchar(45) DEFAULT NULL,
  `successful_50_50` varchar(45) DEFAULT NULL,
  `own_goals` varchar(45) DEFAULT NULL,
  `err_leading_to_goal` varchar(45) DEFAULT NULL,
  `assists` varchar(45) DEFAULT NULL,
  `passes` varchar(45) DEFAULT NULL,
  `passes_per_match` float DEFAULT NULL,
  `big_chances_created` varchar(45) DEFAULT NULL,
  `crosses` varchar(45) DEFAULT NULL,
  `cross_accuracy` float DEFAULT NULL,
  `through_balls` varchar(45) DEFAULT NULL,
  `accurate_long_balls` varchar(45) DEFAULT NULL,
  `goals` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_defender`),
  UNIQUE KEY `id_defender_UNIQUE` (`id_defender`),
  KEY `player_id_idx` (`player_id_def`)
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Forwards`
--

DROP TABLE IF EXISTS `Forwards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Forwards` (
  `id_forward` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `appearances` varchar(45) DEFAULT NULL,
  `goals` varchar(45) DEFAULT NULL,
  `goals_per_match` varchar(45) DEFAULT NULL,
  `shots` varchar(45) DEFAULT NULL,
  `shots_on_target` varchar(45) DEFAULT NULL,
  `assists` varchar(45) DEFAULT NULL,
  `passes` varchar(45) DEFAULT NULL,
  `passes_per_match` float DEFAULT NULL,
  `crosses` varchar(45) DEFAULT NULL,
  `player_id_for` int(11) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_forward`),
  UNIQUE KEY `idForward_UNIQUE` (`id_forward`),
  KEY `player_id_idx` (`player_id_for`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Goalkeepers`
--

DROP TABLE IF EXISTS `Goalkeepers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Goalkeepers` (
  `id_goalkeeper` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `saves` varchar(45) DEFAULT NULL,
  `player_id_goal` int(11) DEFAULT NULL,
  `penalties_saved` varchar(45) DEFAULT NULL,
  `punches` varchar(45) DEFAULT NULL,
  `high_claims` varchar(45) DEFAULT NULL,
  `catches` varchar(45) DEFAULT NULL,
  `sweeper_clearances` varchar(45) DEFAULT NULL,
  `throw_outs` varchar(45) DEFAULT NULL,
  `goal_kicks` varchar(45) DEFAULT NULL,
  `clean_sheets` varchar(45) DEFAULT NULL,
  `goals_conceded` varchar(45) DEFAULT NULL,
  `err_leading_to_goal` varchar(45) DEFAULT NULL,
  `own_goals` varchar(45) DEFAULT NULL,
  `assists` varchar(45) DEFAULT NULL,
  `passes` varchar(45) DEFAULT NULL,
  `passes_per_match` float DEFAULT NULL,
  `accurate_long_balls` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_goalkeeper`),
  UNIQUE KEY `name_UNIQUE` (`id_goalkeeper`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Midfielders`
--

DROP TABLE IF EXISTS `Midfielders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Midfielders` (
  `id_midfielder` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `goals` varchar(45) DEFAULT NULL,
  `shots` varchar(45) DEFAULT NULL,
  `shots_on_target` varchar(45) DEFAULT NULL,
  `player_id_mid` int(11) DEFAULT NULL,
  `shooting_accuracy` float DEFAULT NULL,
  `assists` varchar(45) DEFAULT NULL,
  `passes` varchar(45) DEFAULT NULL,
  `passes_per_match` varchar(45) DEFAULT NULL,
  `big_chances_created` varchar(45) DEFAULT NULL,
  `crosses` varchar(45) DEFAULT NULL,
  `cross_accuracy` float DEFAULT NULL,
  `through_balls` varchar(45) DEFAULT NULL,
  `accurate_long_balls` varchar(45) DEFAULT NULL,
  `tackles` varchar(45) DEFAULT NULL,
  `tackle_success` float DEFAULT NULL,
  `blocked_shots` varchar(45) DEFAULT NULL,
  `interceptions` varchar(45) DEFAULT NULL,
  `clearances` varchar(45) DEFAULT NULL,
  `recoveries` varchar(45) DEFAULT NULL,
  `duels_won` varchar(45) DEFAULT NULL,
  `duels_lost` varchar(45) DEFAULT NULL,
  `successful_50_50` varchar(45) DEFAULT NULL,
  `aerial_battles_won` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_midfielder`),
  UNIQUE KEY `id_midfielder_UNIQUE` (`id_midfielder`),
  KEY `player_id_idx` (`player_id_mid`),
  CONSTRAINT `player_id` FOREIGN KEY (`player_id_mid`) REFERENCES `Players` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=317 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Players`
--

DROP TABLE IF EXISTS `Players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Players` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20000) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `player_link` varchar(200) DEFAULT NULL,
  `team` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=850 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-12 22:07:17
