CREATE DATABASE  IF NOT EXISTS `law` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `law`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: law
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `advocate`
--

DROP TABLE IF EXISTS `advocate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `advocate` (
  `adv_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_img` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_enroll_no` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_qual` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_age` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_gender` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_phone` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_address` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_category` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`adv_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advocate`
--

LOCK TABLES `advocate` WRITE;
/*!40000 ALTER TABLE `advocate` DISABLE KEYS */;
/*!40000 ALTER TABLE `advocate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `case_request`
--

DROP TABLE IF EXISTS `case_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `case_request` (
  `case_id` int NOT NULL AUTO_INCREMENT,
  `adv_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `case_title` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `case_desc` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `case_file` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ipc_sections` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `posted_date` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `case_request`
--

LOCK TABLES `case_request` WRITE;
/*!40000 ALTER TABLE `case_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `case_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `cat_id` int NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `cat_description` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (2,'Family lawyer',' family lawyer is the type of lawyer who’ll be best equipped to guide you through the process which lies before you'),(3,'Intellectual Property  Lawyer','Intellectual property (IP) lawyers protect and enforce the rights and creations of inventors, authors, artists, and businesses.'),(4,'Tax lawyer',' A tax attorney specializes in the many intricacies of federal, state, and local tax laws and should be able to provide advice on the particular tax issue you face.'),(5,'Personal injury lawyer','Personal injury lawyers work primarily in civil litigations, representing clients who have sustained an injury. '),(6,'Bankruptcy lawyer','If you’re having financial difficulties and are contemplating bankruptcy proceedings, you’ll want to consult with a bankruptcy attorney.'),(7,'Corporate lawyer','Corporate lawyers handle legal matters for corporations and ensure that all business transactions are in compliance with the law. '),(8,'Immigration lawyer','Immigration lawyers play a pivotal role in providing guidance to individuals and families navigating the necessary requirements to live, work, or study in the U.S.');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documents`
--

DROP TABLE IF EXISTS `documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documents` (
  `doc_id` int NOT NULL AUTO_INCREMENT,
  `case_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `doc_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `document` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `posted_date` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents`
--

LOCK TABLES `documents` WRITE;
/*!40000 ALTER TABLE `documents` DISABLE KEYS */;
/*!40000 ALTER TABLE `documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `feed_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `feed_subject` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `feed_description` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `posted_date` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`feed_id`),
  KEY `feedback_ibfk_1` (`user_id`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipc`
--

DROP TABLE IF EXISTS `ipc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipc` (
  `ipc_id` int NOT NULL AUTO_INCREMENT,
  `ipc_section` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ipc_description` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`ipc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipc`
--

LOCK TABLES `ipc` WRITE;
/*!40000 ALTER TABLE `ipc` DISABLE KEYS */;
INSERT INTO `ipc` VALUES (1,'Sections 120A to 120B.','criminal conspiracy.'),(2,'Sections 121 to 130','Offences against the State'),(3,'Sections 141 to 160','Offences against the Public Tranquillity'),(4,'Sections 171A to 171I','Offences Relating to Elections'),(5,'Sections 172 to 190','Offences relating to coin and Government Stamps'),(6,'Sections 264 to 267','Offences relating to Weight and Measures'),(7,'Sections 268 to 294','Offences affecting the Public Health, Safety, Convenience, Decency and Morals.'),(8,'Sections 295 to 298','Offences relating to Religion'),(9,'Sections 299 to 377','Offences affecting the Human Body.'),(10,'Sections 378 to 462','Offences Against Property'),(11,'Section 463 to 489 -E','Offences relating to Documents and Property Marks'),(12,'Sections 493 to 498','Offences related to marriage'),(13,'Sections 499 to 502','Offences related to Defamation');
/*!40000 ALTER TABLE `ipc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'admin','123','admin','1');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `pay_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `case_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `posted_date` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `amount` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `paid_date` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Approval` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rating` (
  `rate_id` int NOT NULL AUTO_INCREMENT,
  `case_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `adv_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rating` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rate_desc` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `u_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_img` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_age` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_gender` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_phone` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_aadhar` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `u_address` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_account` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u_cvv` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`u_id`),
  KEY `user_ibfk_1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-27  0:24:26
