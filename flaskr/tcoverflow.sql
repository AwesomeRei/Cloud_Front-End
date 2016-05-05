/*
SQLyog Ultimate v9.02 
MySQL - 5.5.5-10.0.17-MariaDB : Database - tcoverflow
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tcoverflow` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tcoverflow`;

/*Table structure for table `jawaban` */

DROP TABLE IF EXISTS `jawaban`;

CREATE TABLE `jawaban` (
  `id_jawaban` int(11) NOT NULL AUTO_INCREMENT,
  `id_soal` int(11) NOT NULL,
  `rating_jawaban` int(11) NOT NULL DEFAULT '0',
  `isi_jawaban` text NOT NULL,
  `id_user` int(11) NOT NULL,
  `tgl_jawaban` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_jawaban`),
  KEY `id_soal` (`id_soal`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `jawaban_ibfk_1` FOREIGN KEY (`id_soal`) REFERENCES `question` (`id_question`),
  CONSTRAINT `jawaban_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `jawaban` */

/*Table structure for table `picture` */

DROP TABLE IF EXISTS `picture`;

CREATE TABLE `picture` (
  `id_picture` int(11) NOT NULL AUTO_INCREMENT,
  `isi_picture` longblob NOT NULL,
  `id_question` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_picture`),
  KEY `FK_picture` (`id_question`),
  CONSTRAINT `FK_picture` FOREIGN KEY (`id_question`) REFERENCES `question` (`id_question`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `picture` */

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `id_question` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL,
  `pertanyaan` text NOT NULL,
  `judul` varchar(50) NOT NULL,
  `tgl_question` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_question`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `question` */

/*Table structure for table `tags` */

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
  `id_tags` int(11) NOT NULL AUTO_INCREMENT,
  `C_tags` int(11) NOT NULL DEFAULT '0',
  `C++_tags` int(11) NOT NULL DEFAULT '0',
  `C#_tags` int(11) NOT NULL DEFAULT '0',
  `HTML_tags` int(11) NOT NULL DEFAULT '0',
  `PHP_tags` int(11) NOT NULL DEFAULT '0',
  `JS_tags` int(11) NOT NULL DEFAULT '0',
  `Py_tags` int(11) NOT NULL DEFAULT '0',
  `VB_tags` int(11) NOT NULL DEFAULT '0',
  `Bash_tags` int(11) NOT NULL DEFAULT '0',
  `Java_tags` int(11) NOT NULL DEFAULT '0',
  `Android_tags` int(11) NOT NULL DEFAULT '0',
  `Unity_tags` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_tags`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tags` */

/*Table structure for table `tagstoquestion` */

DROP TABLE IF EXISTS `tagstoquestion`;

CREATE TABLE `tagstoquestion` (
  `id_tagstoquestion` int(11) NOT NULL AUTO_INCREMENT,
  `id_tags` int(11) NOT NULL,
  `id_question` int(11) NOT NULL,
  PRIMARY KEY (`id_tagstoquestion`),
  KEY `id_tags` (`id_tags`),
  KEY `id_question` (`id_question`),
  CONSTRAINT `tagstoquestion_ibfk_1` FOREIGN KEY (`id_tags`) REFERENCES `tags` (`id_tags`),
  CONSTRAINT `tagstoquestion_ibfk_2` FOREIGN KEY (`id_question`) REFERENCES `question` (`id_question`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tagstoquestion` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `status` int(11) NOT NULL,
  `foto_user` longblob,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
