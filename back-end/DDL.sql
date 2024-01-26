-- MariaDB dump 10.19-11.1.2-MariaDB, for osx10.18 (arm64)
--
-- Host: localhost    Database: ntuaflix
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ListForWtachingLater`
--

DROP TABLE IF EXISTS `ListForWtachingLater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ListForWtachingLater` (
  `usersid` int(10) NOT NULL,
  `title_basicstconst` int(10) NOT NULL,
  PRIMARY KEY (`usersid`,`title_basicstconst`),
  KEY `FKListForWta487630` (`title_basicstconst`),
  CONSTRAINT `FKListForWta155105` FOREIGN KEY (`usersid`) REFERENCES `users` (`id`),
  CONSTRAINT `FKListForWta487630` FOREIGN KEY (`title_basicstconst`) REFERENCES `title_basics` (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ListForWtachingLater`
--

LOCK TABLES `ListForWtachingLater` WRITE;
/*!40000 ALTER TABLE `ListForWtachingLater` DISABLE KEYS */;
/*!40000 ALTER TABLE `ListForWtachingLater` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `director`
--

DROP TABLE IF EXISTS `director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `director` (
  `name_basicsnconst` int(10) NOT NULL,
  `title_basicstconst` int(10) NOT NULL,
  PRIMARY KEY (`name_basicsnconst`,`title_basicstconst`),
  KEY `FKdirector154772` (`title_basicstconst`),
  CONSTRAINT `FKdirector154772` FOREIGN KEY (`title_basicstconst`) REFERENCES `title_basics` (`tconst`),
  CONSTRAINT `FKdirector47392` FOREIGN KEY (`name_basicsnconst`) REFERENCES `name_basics` (`nconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `director`
--

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;
/*!40000 ALTER TABLE `director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knownForTitles`
--

DROP TABLE IF EXISTS `knownForTitles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `knownForTitles` (
  `name_basicsnconst` int(10) NOT NULL,
  `title_basicstconst` int(10) NOT NULL,
  PRIMARY KEY (`name_basicsnconst`,`title_basicstconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knownForTitles`
--

LOCK TABLES `knownForTitles` WRITE;
/*!40000 ALTER TABLE `knownForTitles` DISABLE KEYS */;
/*!40000 ALTER TABLE `knownForTitles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `usersid` int(10) NOT NULL,
  `title_basicstconst` int(10) NOT NULL,
  PRIMARY KEY (`usersid`,`title_basicstconst`),
  KEY `FKlikes85493` (`title_basicstconst`),
  CONSTRAINT `FKlikes442757` FOREIGN KEY (`usersid`) REFERENCES `users` (`id`),
  CONSTRAINT `FKlikes85493` FOREIGN KEY (`title_basicstconst`) REFERENCES `title_basics` (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `name_basics`
--

DROP TABLE IF EXISTS `name_basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `name_basics` (
  `nconst` int(10) NOT NULL AUTO_INCREMENT,
  `PrimaryName` varchar(100) NOT NULL,
  `birthYear` int(4) NOT NULL,
  `deathYear` int(4) DEFAULT NULL,
  `primaryProfession` varchar(200) NOT NULL,
  `img_url_asset` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`nconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `name_basics`
--

LOCK TABLES `name_basics` WRITE;
/*!40000 ALTER TABLE `name_basics` DISABLE KEYS */;
/*!40000 ALTER TABLE `name_basics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_akas`
--

DROP TABLE IF EXISTS `title_akas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_akas` (
  `titleId` int(10) NOT NULL,
  `ordering` int(2) NOT NULL,
  `title` varchar(100) NOT NULL,
  `region` varchar(5) DEFAULT NULL,
  `language` varchar(10) DEFAULT NULL,
  `types` varchar(50) DEFAULT NULL,
  `attributes` varchar(100) DEFAULT NULL,
  `isOriginalTitle` int(1) NOT NULL,
  PRIMARY KEY (`titleId`,`ordering`),
  CONSTRAINT `FKtitle_akas925023` FOREIGN KEY (`titleId`, `ordering`) REFERENCES `title_principals` (`tconst`, `ordering`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_akas`
--

LOCK TABLES `title_akas` WRITE;
/*!40000 ALTER TABLE `title_akas` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_akas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_basics`
--

DROP TABLE IF EXISTS `title_basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_basics` (
  `tconst` int(10) NOT NULL AUTO_INCREMENT,
  `titleType` varchar(20) NOT NULL,
  `primaryTitle` varchar(200) NOT NULL,
  `originalTitle` varchar(200) NOT NULL,
  `isAdult` int(1) NOT NULL,
  `startYear` int(4) NOT NULL,
  `endYear` int(4) DEFAULT NULL,
  `runtimeMinutes` int(4) DEFAULT NULL,
  `genres` varchar(100) DEFAULT NULL,
  `Column` int(10) DEFAULT NULL,
  PRIMARY KEY (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_basics`
--

LOCK TABLES `title_basics` WRITE;
/*!40000 ALTER TABLE `title_basics` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_basics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_episode`
--

DROP TABLE IF EXISTS `title_episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_episode` (
  `tconst` int(10) NOT NULL AUTO_INCREMENT,
  `parentTconst` int(10) NOT NULL,
  `seasonNumber` int(3) DEFAULT NULL,
  `episodeNumber` int(3) DEFAULT NULL,
  PRIMARY KEY (`tconst`),
  KEY `FKtitle_epis595858` (`parentTconst`),
  CONSTRAINT `FKtitle_epis595858` FOREIGN KEY (`parentTconst`) REFERENCES `title_basics` (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_episode`
--

LOCK TABLES `title_episode` WRITE;
/*!40000 ALTER TABLE `title_episode` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_episode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_principals`
--

DROP TABLE IF EXISTS `title_principals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_principals` (
  `tconst` int(10) NOT NULL,
  `ordering` int(2) NOT NULL,
  `name_basicsnconst` int(10) NOT NULL,
  `category` varchar(100) NOT NULL,
  `job` varchar(100) DEFAULT NULL,
  `characters` varchar(100) DEFAULT NULL,
  `img_url_asset` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`tconst`,`ordering`),
  KEY `FKtitle_prin203074` (`name_basicsnconst`),
  CONSTRAINT `FKtitle_prin203074` FOREIGN KEY (`name_basicsnconst`) REFERENCES `name_basics` (`nconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_principals`
--

LOCK TABLES `title_principals` WRITE;
/*!40000 ALTER TABLE `title_principals` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_principals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title_ratings`
--

DROP TABLE IF EXISTS `title_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title_ratings` (
  `tconst` int(10) NOT NULL,
  `averageRating` double NOT NULL,
  `numVotes` int(7) NOT NULL,
  PRIMARY KEY (`tconst`),
  CONSTRAINT `FKtitle_rati976740` FOREIGN KEY (`tconst`) REFERENCES `title_basics` (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title_ratings`
--

LOCK TABLES `title_ratings` WRITE;
/*!40000 ALTER TABLE `title_ratings` DISABLE KEYS */;
/*!40000 ALTER TABLE `title_ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `is_admin` int(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `writer`
--

DROP TABLE IF EXISTS `writer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `writer` (
  `name_basicsnconst` int(10) NOT NULL,
  `title_basicstconst` int(10) NOT NULL,
  PRIMARY KEY (`name_basicsnconst`,`title_basicstconst`),
  KEY `FKwriter536057` (`title_basicstconst`),
  CONSTRAINT `FKwriter428677` FOREIGN KEY (`name_basicsnconst`) REFERENCES `name_basics` (`nconst`),
  CONSTRAINT `FKwriter536057` FOREIGN KEY (`title_basicstconst`) REFERENCES `title_basics` (`tconst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `writer`
--

LOCK TABLES `writer` WRITE;
/*!40000 ALTER TABLE `writer` DISABLE KEYS */;
/*!40000 ALTER TABLE `writer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-26 14:46:25
