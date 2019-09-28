

-- phpMyAdmin SQL Dump

-- version 4.8.3

-- https://www.phpmyadmin.net/

--

-- Servidor: 127.0.0.1

-- Tiempo de generación: 28-09-2019 a las 22:30:45

-- Versión del servidor: 10.1.36-MariaDB

-- Versión de PHP: 7.2.11

​

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

SET AUTOCOMMIT = 0;

START TRANSACTION;

SET time_zone = "+00:00";

​

​

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;

/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;

/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;

/*!40101 SET NAMES utf8mb4 */;

​

--

-- Base de datos: `ieps`

--

​

-- --------------------------------------------------------

​

--

-- Estructura de tabla para la tabla `eps`

--

​

CREATE TABLE `eps` (

  `id` int(4) NOT NULL,

  `name` varchar(100) NOT NULL,

  `phone` varchar(30) NOT NULL,

  `free_line` varchar(30) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

​

​

-- --------------------------------------------------------

​

--

-- Estructura de tabla para la tabla `eps_hospital`

--

​

CREATE TABLE `eps_hospital` (

  `eps_id` int(4) NOT NULL,

  `hospital_id` int(4) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

​

-- --------------------------------------------------------

​

--

-- Estructura de tabla para la tabla `hospital`

--

​

CREATE TABLE `hospital` (

  `id` int(4) NOT NULL,

  `name` varchar(255) NOT NULL,

  `latitude` float NOT NULL,

  `longitude` float NOT NULL,

  `address` varchar(255) NOT NULL,

  `general_em` tinyint(1) NOT NULL,

  `odonto_em` tinyint(1) NOT NULL,

  `contact` varchar(255) NOT NULL,

  `phone_number` varchar(50) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

​




--

-- Índices para tablas volcadas

--

​

--

-- Indices de la tabla `eps`

--

ALTER TABLE `eps`

  ADD PRIMARY KEY (`id`);

​

--

-- Indices de la tabla `hospital`

--

ALTER TABLE `hospital`

  ADD PRIMARY KEY (`id`);

​

--

-- AUTO_INCREMENT de las tablas volcadas

--

​

--

-- AUTO_INCREMENT de la tabla `eps`

--

ALTER TABLE `eps`

  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

​

--

-- AUTO_INCREMENT de la tabla `hospital`

--

ALTER TABLE `hospital`

  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

COMMIT;

​

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


