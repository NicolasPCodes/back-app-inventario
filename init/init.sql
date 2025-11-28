-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: recepcion_dbs
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Create dump of database 'recepcion_dbs'
--

CREATE DATABASE IF NOT EXISTS recepcion_dbs;
USE recepcion_dbs;

--
-- Table structure for table `discrepancias`
--

DROP TABLE IF EXISTS `discrepancias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discrepancias` (
  `id_discrepancia` int NOT NULL AUTO_INCREMENT,
  `id_recepcion` int DEFAULT NULL,
  `diferencia` int DEFAULT NULL,
  `estado` enum('pendiente','resuelto') DEFAULT 'pendiente',
  `fecha_discrepancia` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `comentario` text,
  PRIMARY KEY (`id_discrepancia`),
  KEY `id_recepcion` (`id_recepcion`),
  CONSTRAINT `discrepancias_ibfk_1` FOREIGN KEY (`id_recepcion`) REFERENCES `recepcion` (`id_recepcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orden_compra`
--

DROP TABLE IF EXISTS `orden_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_compra` (
  `id_oc` int NOT NULL AUTO_INCREMENT,
  `numero_oc` varchar(50) DEFAULT NULL,
  `sku` varchar(20) DEFAULT NULL,
  `tienda` varchar(50) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`id_oc`),
  KEY `sku` (`sku`),
  CONSTRAINT `orden_compra_ibfk_1` FOREIGN KEY (`sku`) REFERENCES `productos` (`sku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `sku` varchar(20) NOT NULL,
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `categoria` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sku`),
  UNIQUE KEY `id_producto` (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `recepcion`
--

DROP TABLE IF EXISTS `recepcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recepcion` (
  `id_recepcion` int NOT NULL AUTO_INCREMENT,
  `id_oc` int DEFAULT NULL,
  `usuario` int DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `cantidad_recibida` int DEFAULT NULL,
  `estado_recepcion` enum('pendiente','completa','incompleta') DEFAULT 'pendiente',
  `comentario` text,
  PRIMARY KEY (`id_recepcion`),
  KEY `id_oc` (`id_oc`),
  KEY `usuario` (`usuario`),
  CONSTRAINT `recepcion_ibfk_1` FOREIGN KEY (`id_oc`) REFERENCES `orden_compra` (`id_oc`),
  CONSTRAINT `recepcion_ibfk_2` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `estado_usuario` enum('activo','inactivo','suspendido') DEFAULT 'activo',
  `rol` enum('encargado','jefe_tienda','auditor','admin') NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-23 16:53:12

--- INSERT VALORES
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12310',6,'Bloqueador en barra','Cuidado facial.','Cara');
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12345',1,'Labial blush','Tinte rojo para labios.','Labios');
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12346',2,'Labial brillo','Brillo para labios.','Labios');
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12347',3,'Sombras','Sombras para ojos.','Ojos');
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12349',5,'Skincare facial','Cuidado facial.','Cara');
INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12385',4,'Encrespador','Especial para pestañas.','Ojos');

INSERT INTO `usuarios` (`nombre`, `apellido`, `fecha_creacion`, `estado_usuario`, `rol`, `password_hash`)VALUES("Nicolas", "Paredes", "2025-11-02 12:00:00", 'activo', 'encargado', "abc12354");

INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (1,'OC-67890','SKU12345','COS',100);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (3,'OC-67890','SKU12310','COS',10);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (4,'OC-67892','SKU12346','COS',100);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (5,'OC-67892','SKU12347','COS',120);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (6,'OC-67892','SKU12385','COS',200);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (7,'OC-67893','SKU12346','MAI',200);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (8,'OC-67893','SKU12347','MAI',20);
INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (9,'OC-67894','SKU12385','MAI',200);