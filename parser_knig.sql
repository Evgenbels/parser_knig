-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Ноя 07 2021 г., 21:18
-- Версия сервера: 8.0.27-0ubuntu0.20.04.1
-- Версия PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `parser_knig`
--

-- --------------------------------------------------------

--
-- Структура таблицы `knigi`
--

CREATE TABLE `knigi` (
  `avtor` varchar(50) NOT NULL,
  `cikl` varchar(50) NOT NULL,
  `kol` int DEFAULT NULL,
  `flag` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `knigi`
--

INSERT INTO `knigi` (`avtor`, `cikl`, `kol`, `flag`) VALUES
('belyev', 'home', 2, 0),
('den', 'user', 3, 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `knigi`
--
ALTER TABLE `knigi`
  ADD PRIMARY KEY (`avtor`,`cikl`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
