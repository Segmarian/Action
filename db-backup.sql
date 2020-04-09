-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: Character.mysql.pythonanywhere-services.com    Database: Character$action
-- ------------------------------------------------------
-- Server version	5.6.40-log

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
-- Table structure for table `action_advancement`
--

DROP TABLE IF EXISTS `action_advancement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_advancement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `description` varchar(120) DEFAULT NULL,
  `schtick_id` int(11) NOT NULL,
  `req_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `action_advancement_schtick_id_4a9a80b6_fk_action_schtick_id` (`schtick_id`),
  KEY `action_advancement_req_id_83a53c53_fk_action_pr` (`req_id`),
  CONSTRAINT `action_advancement_req_id_83a53c53_fk_action_pr` FOREIGN KEY (`req_id`) REFERENCES `action_prereq` (`valuepair_ptr_id`),
  CONSTRAINT `action_advancement_schtick_id_4a9a80b6_fk_action_schtick_id` FOREIGN KEY (`schtick_id`) REFERENCES `action_schtick` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_advancement`
--

LOCK TABLES `action_advancement` WRITE;
/*!40000 ALTER TABLE `action_advancement` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_advancement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_attribute`
--

DROP TABLE IF EXISTS `action_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_attribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `short_name` varchar(10) DEFAULT NULL,
  `start` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_attribute`
--

LOCK TABLES `action_attribute` WRITE;
/*!40000 ALTER TABLE `action_attribute` DISABLE KEYS */;
INSERT INTO `action_attribute` VALUES (1,'Strength','Str',5),(2,'Agility','Agi',5),(3,'Toughness','Tou',5),(4,'Perception','Per',5),(5,'Intelligence','Int',5),(6,'Wits','Wits',5),(7,'Charisma','Cha',5),(8,'Manipulation','Man',5),(9,'Empathy','Emp',5),(10,'Focus','Foc',5),(11,'Power','Pow',5),(12,'Influence','Inf',5),(13,'Resources','Res',5),(14,'Status','Sta',5);
/*!40000 ALTER TABLE `action_attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_flaw`
--

DROP TABLE IF EXISTS `action_flaw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_flaw` (
  `valuepair_ptr_id` int(11) NOT NULL,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`valuepair_ptr_id`),
  CONSTRAINT `action_flaw_valuepair_ptr_id_c45c22a8_fk_action_valuepair_id` FOREIGN KEY (`valuepair_ptr_id`) REFERENCES `action_valuepair` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_flaw`
--

LOCK TABLES `action_flaw` WRITE;
/*!40000 ALTER TABLE `action_flaw` DISABLE KEYS */;
INSERT INTO `action_flaw` VALUES (1,'Arrogant');
/*!40000 ALTER TABLE `action_flaw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_modifier`
--

DROP TABLE IF EXISTS `action_modifier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_modifier` (
  `valuepair_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`valuepair_ptr_id`),
  CONSTRAINT `action_modifier_valuepair_ptr_id_7080de4d_fk_action_valuepair_id` FOREIGN KEY (`valuepair_ptr_id`) REFERENCES `action_valuepair` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_modifier`
--

LOCK TABLES `action_modifier` WRITE;
/*!40000 ALTER TABLE `action_modifier` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_modifier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_prereq`
--

DROP TABLE IF EXISTS `action_prereq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_prereq` (
  `valuepair_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`valuepair_ptr_id`),
  CONSTRAINT `action_prereq_valuepair_ptr_id_9fdff157_fk_action_valuepair_id` FOREIGN KEY (`valuepair_ptr_id`) REFERENCES `action_valuepair` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_prereq`
--

LOCK TABLES `action_prereq` WRITE;
/*!40000 ALTER TABLE `action_prereq` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_prereq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_proficiency`
--

DROP TABLE IF EXISTS `action_proficiency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_proficiency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `skill_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `action_proficiency_skill_id_0ace4c1a_fk_action_skill_id` (`skill_id`),
  CONSTRAINT `action_proficiency_skill_id_0ace4c1a_fk_action_skill_id` FOREIGN KEY (`skill_id`) REFERENCES `action_skill` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_proficiency`
--

LOCK TABLES `action_proficiency` WRITE;
/*!40000 ALTER TABLE `action_proficiency` DISABLE KEYS */;
INSERT INTO `action_proficiency` VALUES (1,'Dodge',1),(2,'Athletics',1),(3,'Stunt',1),(4,'Martial Arts',1),(5,'Thrown',1);
/*!40000 ALTER TABLE `action_proficiency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_schtick`
--

DROP TABLE IF EXISTS `action_schtick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_schtick` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `cost` varchar(120) DEFAULT NULL,
  `description` longtext,
  `tier` smallint(5) unsigned DEFAULT NULL,
  `type_id` int(11) NOT NULL,
  `req_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `action_schtick_type_id_fd8786aa_fk_action_schticktype_id` (`type_id`),
  KEY `action_schtick_req_id_c7709da0_fk_action_prereq_valuepair_ptr_id` (`req_id`),
  CONSTRAINT `action_schtick_req_id_c7709da0_fk_action_prereq_valuepair_ptr_id` FOREIGN KEY (`req_id`) REFERENCES `action_prereq` (`valuepair_ptr_id`),
  CONSTRAINT `action_schtick_type_id_fd8786aa_fk_action_schticktype_id` FOREIGN KEY (`type_id`) REFERENCES `action_schticktype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_schtick`
--

LOCK TABLES `action_schtick` WRITE;
/*!40000 ALTER TABLE `action_schtick` DISABLE KEYS */;
INSERT INTO `action_schtick` VALUES (1,'Veteran','2','Raises SchtickMax of a Skill by 1.',2,1,NULL),(2,'Elite','2','Raises SkillMax of a Skill by 1.',2,1,NULL);
/*!40000 ALTER TABLE `action_schtick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_schtickmod`
--

DROP TABLE IF EXISTS `action_schtickmod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_schtickmod` (
  `valuepair_ptr_id` int(11) NOT NULL,
  `linked_schtick_id` int(11) NOT NULL,
  PRIMARY KEY (`valuepair_ptr_id`),
  KEY `action_schtickmod_linked_schtick_id_b26b8426_fk_action_sc` (`linked_schtick_id`),
  CONSTRAINT `action_schtickmod_linked_schtick_id_b26b8426_fk_action_sc` FOREIGN KEY (`linked_schtick_id`) REFERENCES `action_schtick` (`id`),
  CONSTRAINT `action_schtickmod_valuepair_ptr_id_6b69114d_fk_action_va` FOREIGN KEY (`valuepair_ptr_id`) REFERENCES `action_valuepair` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_schtickmod`
--

LOCK TABLES `action_schtickmod` WRITE;
/*!40000 ALTER TABLE `action_schtickmod` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_schtickmod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_schticktype`
--

DROP TABLE IF EXISTS `action_schticktype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_schticktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_schticktype`
--

LOCK TABLES `action_schticktype` WRITE;
/*!40000 ALTER TABLE `action_schticktype` DISABLE KEYS */;
INSERT INTO `action_schticktype` VALUES (1,'Perks & Flaws'),(2,'Fu'),(3,'Creature Power');
/*!40000 ALTER TABLE `action_schticktype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_skill`
--

DROP TABLE IF EXISTS `action_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_skill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_skill`
--

LOCK TABLES `action_skill` WRITE;
/*!40000 ALTER TABLE `action_skill` DISABLE KEYS */;
INSERT INTO `action_skill` VALUES (1,'Action'),(2,'Deceit'),(3,'Ranged Weapons'),(4,'Interaction'),(5,'Medicine'),(6,'Observation'),(7,'Occult'),(8,'Pursuit'),(9,'Security'),(10,'Survival'),(11,'Tech'),(12,'Academics'),(13,'Profession'),(14,'Arts');
/*!40000 ALTER TABLE `action_skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_tag`
--

DROP TABLE IF EXISTS `action_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_tag`
--

LOCK TABLES `action_tag` WRITE;
/*!40000 ALTER TABLE `action_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `action_valuepair`
--

DROP TABLE IF EXISTS `action_valuepair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_valuepair` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` smallint(5) unsigned NOT NULL,
  `attribute_id` int(11) DEFAULT NULL,
  `calculated_attribute_id` int(11) DEFAULT NULL,
  `proficiency_id` int(11) DEFAULT NULL,
  `schtick_id` int(11) DEFAULT NULL,
  `skill_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `action_valuepair_attribute_id_da4d5a1d_fk_action_attribute_id` (`attribute_id`),
  KEY `action_valuepair_calculated_attribute_b5bf62ff_fk_action_at` (`calculated_attribute_id`),
  KEY `action_valuepair_proficiency_id_68cd99b7_fk_action_pr` (`proficiency_id`),
  KEY `action_valuepair_schtick_id_999f6e99_fk_action_schtick_id` (`schtick_id`),
  KEY `action_valuepair_skill_id_0aa8b69e_fk_action_skill_id` (`skill_id`),
  CONSTRAINT `action_valuepair_attribute_id_da4d5a1d_fk_action_attribute_id` FOREIGN KEY (`attribute_id`) REFERENCES `action_attribute` (`id`),
  CONSTRAINT `action_valuepair_calculated_attribute_b5bf62ff_fk_action_at` FOREIGN KEY (`calculated_attribute_id`) REFERENCES `action_attribute` (`id`),
  CONSTRAINT `action_valuepair_proficiency_id_68cd99b7_fk_action_pr` FOREIGN KEY (`proficiency_id`) REFERENCES `action_proficiency` (`id`),
  CONSTRAINT `action_valuepair_schtick_id_999f6e99_fk_action_schtick_id` FOREIGN KEY (`schtick_id`) REFERENCES `action_schtick` (`id`),
  CONSTRAINT `action_valuepair_skill_id_0aa8b69e_fk_action_skill_id` FOREIGN KEY (`skill_id`) REFERENCES `action_skill` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_valuepair`
--

LOCK TABLES `action_valuepair` WRITE;
/*!40000 ALTER TABLE `action_valuepair` DISABLE KEYS */;
INSERT INTO `action_valuepair` VALUES (1,1,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `action_valuepair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add attribute',7,'add_attribute'),(26,'Can change attribute',7,'change_attribute'),(27,'Can delete attribute',7,'delete_attribute'),(28,'Can view attribute',7,'view_attribute'),(29,'Can add proficiency',8,'add_proficiency'),(30,'Can change proficiency',8,'change_proficiency'),(31,'Can delete proficiency',8,'delete_proficiency'),(32,'Can view proficiency',8,'view_proficiency'),(33,'Can add schtick',9,'add_schtick'),(34,'Can change schtick',9,'change_schtick'),(35,'Can delete schtick',9,'delete_schtick'),(36,'Can view schtick',9,'view_schtick'),(37,'Can add schtick type',10,'add_schticktype'),(38,'Can change schtick type',10,'change_schticktype'),(39,'Can delete schtick type',10,'delete_schticktype'),(40,'Can view schtick type',10,'view_schticktype'),(41,'Can add skill',11,'add_skill'),(42,'Can change skill',11,'change_skill'),(43,'Can delete skill',11,'delete_skill'),(44,'Can view skill',11,'view_skill'),(45,'Can add tag',12,'add_tag'),(46,'Can change tag',12,'change_tag'),(47,'Can delete tag',12,'delete_tag'),(48,'Can view tag',12,'view_tag'),(49,'Can add value pair',13,'add_valuepair'),(50,'Can change value pair',13,'change_valuepair'),(51,'Can delete value pair',13,'delete_valuepair'),(52,'Can view value pair',13,'view_valuepair'),(53,'Can add flaw',14,'add_flaw'),(54,'Can change flaw',14,'change_flaw'),(55,'Can delete flaw',14,'delete_flaw'),(56,'Can view flaw',14,'view_flaw'),(57,'Can add modifier',15,'add_modifier'),(58,'Can change modifier',15,'change_modifier'),(59,'Can delete modifier',15,'delete_modifier'),(60,'Can view modifier',15,'view_modifier'),(61,'Can add prereq',16,'add_prereq'),(62,'Can change prereq',16,'change_prereq'),(63,'Can delete prereq',16,'delete_prereq'),(64,'Can view prereq',16,'view_prereq'),(65,'Can add schtick mod',17,'add_schtickmod'),(66,'Can change schtick mod',17,'change_schtickmod'),(67,'Can delete schtick mod',17,'delete_schtickmod'),(68,'Can view schtick mod',17,'view_schtickmod'),(69,'Can add advancement',18,'add_advancement'),(70,'Can change advancement',18,'change_advancement'),(71,'Can delete advancement',18,'delete_advancement'),(72,'Can view advancement',18,'view_advancement'),(73,'Can add character',19,'add_character'),(74,'Can change character',19,'change_character'),(75,'Can delete character',19,'delete_character'),(76,'Can view character',19,'view_character'),(77,'Can add character skill',20,'add_characterskill'),(78,'Can change character skill',20,'change_characterskill'),(79,'Can delete character skill',20,'delete_characterskill'),(80,'Can view character skill',20,'view_characterskill'),(81,'Can add character schtick',21,'add_characterschtick'),(82,'Can change character schtick',21,'change_characterschtick'),(83,'Can delete character schtick',21,'delete_characterschtick'),(84,'Can view character schtick',21,'view_characterschtick'),(85,'Can add character proficiency',22,'add_characterproficiency'),(86,'Can change character proficiency',22,'change_characterproficiency'),(87,'Can delete character proficiency',22,'delete_characterproficiency'),(88,'Can view character proficiency',22,'view_characterproficiency'),(89,'Can add character flaw',23,'add_characterflaw'),(90,'Can change character flaw',23,'change_characterflaw'),(91,'Can delete character flaw',23,'delete_characterflaw'),(92,'Can view character flaw',23,'view_characterflaw'),(93,'Can add character attribute',24,'add_characterattribute'),(94,'Can change character attribute',24,'change_characterattribute'),(95,'Can delete character attribute',24,'delete_characterattribute'),(96,'Can view character attribute',24,'view_characterattribute');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$PGmsYYRJs7SY$dR/XfoyJazLM3JvTe6alCe1C8hwFZ3BRHpstzvmGh7A=','2020-02-02 09:12:19.261889',1,'segmarian','','','segmarian@gmail.com',1,1,'2020-02-02 01:37:33.469006');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_character`
--

DROP TABLE IF EXISTS `character_character`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_character` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `points` int(10) unsigned DEFAULT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_character`
--

LOCK TABLES `character_character` WRITE;
/*!40000 ALTER TABLE `character_character` DISABLE KEYS */;
INSERT INTO `character_character` VALUES (1,'Friedrich Weisshall',33,'White Mage of Jagaan');
/*!40000 ALTER TABLE `character_character` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_characterattribute`
--

DROP TABLE IF EXISTS `character_characterattribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_characterattribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` smallint(6) NOT NULL,
  `attribute_id` int(11) NOT NULL,
  `character_id` int(11) NOT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_charactera_attribute_id_9f0428e6_fk_action_at` (`attribute_id`),
  KEY `character_charactera_character_id_8f275448_fk_character` (`character_id`),
  CONSTRAINT `character_charactera_attribute_id_9f0428e6_fk_action_at` FOREIGN KEY (`attribute_id`) REFERENCES `action_attribute` (`id`),
  CONSTRAINT `character_charactera_character_id_8f275448_fk_character` FOREIGN KEY (`character_id`) REFERENCES `character_character` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_characterattribute`
--

LOCK TABLES `character_characterattribute` WRITE;
/*!40000 ALTER TABLE `character_characterattribute` DISABLE KEYS */;
INSERT INTO `character_characterattribute` VALUES (12,5,1,1,NULL),(13,5,2,1,NULL),(14,5,3,1,NULL),(15,5,4,1,NULL),(16,8,5,1,NULL),(17,8,6,1,NULL),(18,6,7,1,NULL),(19,4,8,1,NULL),(20,8,9,1,NULL),(21,6,10,1,NULL),(22,13,11,1,NULL),(23,6,12,1,NULL),(24,6,13,1,NULL),(25,6,14,1,NULL);
/*!40000 ALTER TABLE `character_characterattribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_characterflaw`
--

DROP TABLE IF EXISTS `character_characterflaw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_characterflaw` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` smallint(6) NOT NULL,
  `character_id` int(11) NOT NULL,
  `flaw_id` int(11) NOT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_characterf_character_id_1041f2e7_fk_character` (`character_id`),
  KEY `character_characterf_flaw_id_830a1bd6_fk_action_fl` (`flaw_id`),
  CONSTRAINT `character_characterf_character_id_1041f2e7_fk_character` FOREIGN KEY (`character_id`) REFERENCES `character_character` (`id`),
  CONSTRAINT `character_characterf_flaw_id_830a1bd6_fk_action_fl` FOREIGN KEY (`flaw_id`) REFERENCES `action_flaw` (`valuepair_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_characterflaw`
--

LOCK TABLES `character_characterflaw` WRITE;
/*!40000 ALTER TABLE `character_characterflaw` DISABLE KEYS */;
INSERT INTO `character_characterflaw` VALUES (7,1,1,1,NULL);
/*!40000 ALTER TABLE `character_characterflaw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_characterproficiency`
--

DROP TABLE IF EXISTS `character_characterproficiency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_characterproficiency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `acquired` tinyint(1) NOT NULL,
  `character_id` int(11) NOT NULL,
  `proficiency_id` int(11) NOT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_characterp_character_id_ec916655_fk_character` (`character_id`),
  KEY `character_characterp_proficiency_id_dac04290_fk_action_pr` (`proficiency_id`),
  CONSTRAINT `character_characterp_character_id_ec916655_fk_character` FOREIGN KEY (`character_id`) REFERENCES `character_character` (`id`),
  CONSTRAINT `character_characterp_proficiency_id_dac04290_fk_action_pr` FOREIGN KEY (`proficiency_id`) REFERENCES `action_proficiency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_characterproficiency`
--

LOCK TABLES `character_characterproficiency` WRITE;
/*!40000 ALTER TABLE `character_characterproficiency` DISABLE KEYS */;
INSERT INTO `character_characterproficiency` VALUES (2,1,1,2,NULL);
/*!40000 ALTER TABLE `character_characterproficiency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_characterschtick`
--

DROP TABLE IF EXISTS `character_characterschtick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_characterschtick` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` smallint(6) NOT NULL,
  `character_id` int(11) NOT NULL,
  `schtick_id` int(11) NOT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_characters_character_id_872927da_fk_character` (`character_id`),
  KEY `character_characters_schtick_id_44d8f446_fk_action_sc` (`schtick_id`),
  CONSTRAINT `character_characters_character_id_872927da_fk_character` FOREIGN KEY (`character_id`) REFERENCES `character_character` (`id`),
  CONSTRAINT `character_characters_schtick_id_44d8f446_fk_action_sc` FOREIGN KEY (`schtick_id`) REFERENCES `action_schtick` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_characterschtick`
--

LOCK TABLES `character_characterschtick` WRITE;
/*!40000 ALTER TABLE `character_characterschtick` DISABLE KEYS */;
INSERT INTO `character_characterschtick` VALUES (5,2,1,1,NULL);
/*!40000 ALTER TABLE `character_characterschtick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_characterskill`
--

DROP TABLE IF EXISTS `character_characterskill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `character_characterskill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` smallint(6) NOT NULL,
  `character_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL,
  `notes` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_characters_character_id_2a9aca7f_fk_character` (`character_id`),
  KEY `character_characterskill_skill_id_c2a71938_fk_action_skill_id` (`skill_id`),
  CONSTRAINT `character_characters_character_id_2a9aca7f_fk_character` FOREIGN KEY (`character_id`) REFERENCES `character_character` (`id`),
  CONSTRAINT `character_characterskill_skill_id_c2a71938_fk_action_skill_id` FOREIGN KEY (`skill_id`) REFERENCES `action_skill` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_characterskill`
--

LOCK TABLES `character_characterskill` WRITE;
/*!40000 ALTER TABLE `character_characterskill` DISABLE KEYS */;
INSERT INTO `character_characterskill` VALUES (1,1,1,1,NULL),(2,1,1,2,NULL),(3,1,1,3,NULL),(4,4,1,4,NULL),(5,1,1,5,NULL),(6,1,1,6,NULL),(7,5,1,7,NULL),(8,1,1,8,NULL),(9,1,1,9,NULL),(10,1,1,12,NULL);
/*!40000 ALTER TABLE `character_characterskill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-02-02 01:38:16.273459','1','Action',1,'[{\"added\": {}}]',11,1),(2,'2020-02-02 01:39:48.835527','2','Deceit',1,'[{\"added\": {}}]',11,1),(3,'2020-02-02 01:39:54.870001','3','Ranged Weapons',1,'[{\"added\": {}}]',11,1),(4,'2020-02-02 01:40:06.007828','4','Interaction',1,'[{\"added\": {}}]',11,1),(5,'2020-02-02 01:40:10.572492','5','Medicine',1,'[{\"added\": {}}]',11,1),(6,'2020-02-02 01:40:20.933647','6','Observation',1,'[{\"added\": {}}]',11,1),(7,'2020-02-02 01:40:25.409180','7','Occult',1,'[{\"added\": {}}]',11,1),(8,'2020-02-02 01:40:33.709144','8','Pursuit',1,'[{\"added\": {}}]',11,1),(9,'2020-02-02 01:40:38.689609','9','Security',1,'[{\"added\": {}}]',11,1),(10,'2020-02-02 01:40:44.189159','10','Survival',1,'[{\"added\": {}}]',11,1),(11,'2020-02-02 01:40:49.698396','11','Tech',1,'[{\"added\": {}}]',11,1),(12,'2020-02-02 01:40:54.723218','12','Academics',1,'[{\"added\": {}}]',11,1),(13,'2020-02-02 01:41:03.010443','13','Profession',1,'[{\"added\": {}}]',11,1),(14,'2020-02-02 01:41:06.744789','14','Arts',1,'[{\"added\": {}}]',11,1),(15,'2020-02-02 01:41:52.492288','1','Perks & Flaws',1,'[{\"added\": {}}]',10,1),(16,'2020-02-02 01:41:57.084161','2','Fu',1,'[{\"added\": {}}]',10,1),(17,'2020-02-02 01:42:06.103247','3','Creature Power',1,'[{\"added\": {}}]',10,1),(18,'2020-02-02 01:42:32.715569','1','Strength (5)',1,'[{\"added\": {}}]',7,1),(19,'2020-02-02 01:42:43.621693','2','Agility (5)',1,'[{\"added\": {}}]',7,1),(20,'2020-02-02 01:42:57.609901','3','Toughness (5)',1,'[{\"added\": {}}]',7,1),(21,'2020-02-02 01:43:05.568012','4','Perception (5)',1,'[{\"added\": {}}]',7,1),(22,'2020-02-02 01:43:24.309475','5','Intelligence (5)',1,'[{\"added\": {}}]',7,1),(23,'2020-02-02 01:43:32.995449','6','Wits (5)',1,'[{\"added\": {}}]',7,1),(24,'2020-02-02 01:43:41.579935','7','Charisma (5)',1,'[{\"added\": {}}]',7,1),(25,'2020-02-02 01:43:51.501289','8','Manipulation (5)',1,'[{\"added\": {}}]',7,1),(26,'2020-02-02 01:43:59.143712','9','Empathy (5)',1,'[{\"added\": {}}]',7,1),(27,'2020-02-02 01:44:15.316904','10','Focus (5)',1,'[{\"added\": {}}]',7,1),(28,'2020-02-02 01:44:24.401152','11','Power (5)',1,'[{\"added\": {}}]',7,1),(29,'2020-02-02 01:44:33.994599','12','Influence (5)',1,'[{\"added\": {}}]',7,1),(30,'2020-02-02 01:44:42.534294','13','Resources (5)',1,'[{\"added\": {}}]',7,1),(31,'2020-02-02 01:44:55.216322','14','Status (5)',1,'[{\"added\": {}}]',7,1),(32,'2020-02-02 01:45:22.909968','1','Dodge',1,'[{\"added\": {}}]',8,1),(33,'2020-02-02 01:48:16.555060','2','Athletics',1,'[{\"added\": {}}]',8,1),(34,'2020-02-02 01:48:23.291418','3','Stunt',1,'[{\"added\": {}}]',8,1),(35,'2020-02-02 01:48:36.391742','4','Martial Arts',1,'[{\"added\": {}}]',8,1),(36,'2020-02-02 01:48:43.896915','5','Thrown',1,'[{\"added\": {}}]',8,1),(37,'2020-02-02 01:50:27.948120','1','Veteran(Tier 2)',1,'[{\"added\": {}}]',9,1),(38,'2020-02-02 01:51:04.673096','2','Elite(Tier 2)',1,'[{\"added\": {}}]',9,1),(39,'2020-02-02 01:53:22.541160','1','Friedrich Weisshall',1,'[{\"added\": {}}]',19,1),(40,'2020-02-02 10:11:51.057726','12','Strength 5',1,'[{\"added\": {}}]',24,1),(41,'2020-02-02 10:12:01.257513','13','Agility 5',1,'[{\"added\": {}}]',24,1),(42,'2020-02-02 10:12:07.714311','14','Toughness 5',1,'[{\"added\": {}}]',24,1),(43,'2020-02-02 10:12:36.766350','15','Perception 5',1,'[{\"added\": {}}]',24,1),(44,'2020-02-02 10:12:44.803523','16','Intelligence 8',1,'[{\"added\": {}}]',24,1),(45,'2020-02-02 10:12:52.916500','17','Wits 8',1,'[{\"added\": {}}]',24,1),(46,'2020-02-02 10:13:11.867091','18','Charisma 6',1,'[{\"added\": {}}]',24,1),(47,'2020-02-02 10:13:23.135520','19','Manipulation 4',1,'[{\"added\": {}}]',24,1),(48,'2020-02-02 10:13:31.028422','20','Empathy 8',1,'[{\"added\": {}}]',24,1),(49,'2020-02-02 10:13:41.275582','21','Focus 6',1,'[{\"added\": {}}]',24,1),(50,'2020-02-02 10:13:59.701849','22','Power 8',1,'[{\"added\": {}}]',24,1),(51,'2020-02-02 10:14:17.092658','22','Power 13',2,'[{\"changed\": {\"fields\": [\"Points\"]}}]',24,1),(52,'2020-02-02 10:14:30.931457','23','Influence 6',1,'[{\"added\": {}}]',24,1),(53,'2020-02-02 10:14:40.077443','24','Resources 6',1,'[{\"added\": {}}]',24,1),(54,'2020-02-02 10:14:46.773541','25','Status 6',1,'[{\"added\": {}}]',24,1),(55,'2020-02-02 10:15:33.226855','1','Arrogant 1',1,'[{\"added\": {}}]',14,1),(56,'2020-02-02 10:15:59.904479','1','Arrogant 1',2,'[]',14,1),(57,'2020-02-02 10:17:51.093031','7','Arrogant 1',1,'[{\"added\": {}}]',23,1),(58,'2020-02-02 10:21:37.569731','5','Veteran 2',1,'[{\"added\": {}}]',21,1),(59,'2020-02-02 10:22:47.652529','1','Action 10',1,'[{\"added\": {}}]',20,1),(60,'2020-02-02 10:22:58.395229','2','Deceit 1',1,'[{\"added\": {}}]',20,1),(61,'2020-02-02 10:23:35.681326','1','Action 1',2,'[{\"changed\": {\"fields\": [\"Points\"]}}]',20,1),(62,'2020-02-02 10:23:44.003452','3','Ranged Weapons 1',1,'[{\"added\": {}}]',20,1),(63,'2020-02-02 10:23:54.489259','4','Interaction 4',1,'[{\"added\": {}}]',20,1),(64,'2020-02-02 10:24:07.117875','5','Medicine 1',1,'[{\"added\": {}}]',20,1),(65,'2020-02-02 10:24:39.543281','6','Observation 1',1,'[{\"added\": {}}]',20,1),(66,'2020-02-02 10:25:00.323589','7','Occult 5',1,'[{\"added\": {}}]',20,1),(67,'2020-02-02 10:25:09.196539','8','Pursuit 1',1,'[{\"added\": {}}]',20,1),(68,'2020-02-02 10:25:21.560257','9','Security 1',1,'[{\"added\": {}}]',20,1),(69,'2020-02-02 10:25:50.894293','10','Academics 1',1,'[{\"added\": {}}]',20,1),(70,'2020-02-02 10:28:14.514455','2','Athletics True',1,'[{\"added\": {}}]',22,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (18,'action','advancement'),(7,'action','attribute'),(14,'action','flaw'),(15,'action','modifier'),(16,'action','prereq'),(8,'action','proficiency'),(9,'action','schtick'),(17,'action','schtickmod'),(10,'action','schticktype'),(11,'action','skill'),(12,'action','tag'),(13,'action','valuepair'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(19,'character','character'),(24,'character','characterattribute'),(23,'character','characterflaw'),(22,'character','characterproficiency'),(21,'character','characterschtick'),(20,'character','characterskill'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'action','0001_initial','2020-02-02 01:32:44.425461'),(2,'contenttypes','0001_initial','2020-02-02 01:32:54.835431'),(3,'auth','0001_initial','2020-02-02 01:33:59.904575'),(4,'admin','0001_initial','2020-02-02 01:34:24.565793'),(5,'admin','0002_logentry_remove_auto_add','2020-02-02 01:34:24.820397'),(6,'admin','0003_logentry_add_action_flag_choices','2020-02-02 01:34:24.845127'),(7,'contenttypes','0002_remove_content_type_name','2020-02-02 01:34:25.056313'),(8,'auth','0002_alter_permission_name_max_length','2020-02-02 01:34:25.179008'),(9,'auth','0003_alter_user_email_max_length','2020-02-02 01:34:25.252274'),(10,'auth','0004_alter_user_username_opts','2020-02-02 01:34:25.267411'),(11,'auth','0005_alter_user_last_login_null','2020-02-02 01:34:25.324188'),(12,'auth','0006_require_contenttypes_0002','2020-02-02 01:34:25.332187'),(13,'auth','0007_alter_validators_add_error_messages','2020-02-02 01:34:25.354769'),(14,'auth','0008_alter_user_username_max_length','2020-02-02 01:34:25.424680'),(15,'auth','0009_alter_user_last_name_max_length','2020-02-02 01:34:25.493328'),(16,'auth','0010_alter_group_name_max_length','2020-02-02 01:34:25.554357'),(17,'auth','0011_update_proxy_permissions','2020-02-02 01:34:25.575724'),(18,'character','0001_initial','2020-02-02 01:35:39.769892'),(19,'sessions','0001_initial','2020-02-02 01:35:51.186818'),(20,'action','0002_proficiency_skill','2020-02-02 01:47:09.307873'),(21,'character','0002_auto_20200202_0156','2020-02-02 01:56:41.990662'),(22,'character','0003_auto_20200202_1020','2020-02-02 10:20:38.357528');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('pn88n9wfk5h94dmd777e8t3bky69xz9b','NTFmMjgwZmY0MDY4ZjUzNjk2ZDRlZWE4NDk5NTc5ZDE3MGU0NGUyZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NzA2OGU3MWNmMzhmMjNiMGJiMmFiMWExZGMxYjVhMGRiYTllMTEyIn0=','2020-02-16 09:12:19.267786'),('xj1s7v56l0epibhj54sn0iah2bv0r02r','NTFmMjgwZmY0MDY4ZjUzNjk2ZDRlZWE4NDk5NTc5ZDE3MGU0NGUyZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NzA2OGU3MWNmMzhmMjNiMGJiMmFiMWExZGMxYjVhMGRiYTllMTEyIn0=','2020-02-16 01:37:46.458781');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-03 20:51:12
