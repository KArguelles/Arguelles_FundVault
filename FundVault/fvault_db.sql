-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2024 at 01:58 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fvault_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `goals`
--

CREATE TABLE `goals` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `target_amount` decimal(10,2) NOT NULL,
  `current_amount` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `savings_goals`
--

CREATE TABLE `savings_goals` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `goal_name` varchar(100) DEFAULT NULL,
  `target_amount` decimal(10,2) DEFAULT NULL,
  `current_balance` decimal(10,2) DEFAULT 0.00,
  `due_date` date DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `goal_id` int(11) DEFAULT NULL,
  `transaction_type` varchar(50) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `phone_number` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pin` varchar(4) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone_number`, `email`, `pin`, `balance`) VALUES
(1, 'dfaefe', 'efewf', '12345678910', 'gregre', '1234', 0.00),
(2, 'Kriskyla', 'Arguelles', '09567531103', 'krsikylaarguelles24@gmail.com', '0103', 0.00),
(6, 'afffs', 'ffafa', '12398192091', 'fgdgfg', '1234', 0.00),
(7, 'John', 'Doe', '12345678901', 'john.doe@example.com', '1234', 0.00),
(9, 'Mikha', 'Lim', '09876546556', 'mikha24@gmail.com', '0192', 0.00),
(10, 'Maloi', 'Ricalde', '08948586877', 'maloi01@gmail.com', '1245', 0.00),
(11, 'Colet', 'Vergara', '09673673674', 'colet53@gmail.com', '1234', 0.00),
(12, 'Aiah', 'Arceta', '09667657567', 'aiah34@gmail.com', '3465', 0.00),
(13, 'Jhoanna', 'Robles', '09723672362', 'jhoana34@gmail.com', '8765', 0.00),
(14, 'Sheena', 'Catacutan', '43656676767', 'sheena09@gmail.com', '5665', 0.00),
(15, 'Stacey', 'Sevilleja', '09786554677', 'stacey43@gmail.com', '7665', 0.00),
(16, 'Gwen', 'Apuli', '09784758353', 'gwen67@gmail.com', '3443', 0.00),
(17, 'Edward', 'Alcantara', '09876543211', 'dfdsvsd', '1234', 0.00),
(18, 'Kriskyla', 'Arguelles', '12345678765', 'kriskyla24@gmail.com', '1234', 0.00),
(19, 'wqdqw', 'qdwq', '09875671892', 'svsdvsdv', '1234', 0.00),
(20, 'Jhoanna', 'Robles', '09634682832', 'jhoanna23@gmail.com', '1234', 0.00),
(23, 'Kriskyla', 'Arguelles', '09643753453', 'esre24@gmail.com', '1234', 0.00),
(24, 'Kyla', 'Arguelles', '09534678943', 'dsfsfs', '1234', 0.00),
(25, 'Kriskyla', 'Arguelles', '09546789340', 'gdrf', '1234', 0.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `goals`
--
ALTER TABLE `goals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `savings_goals`
--
ALTER TABLE `savings_goals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `goal_id` (`goal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone_number` (`phone_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `goals`
--
ALTER TABLE `goals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `savings_goals`
--
ALTER TABLE `savings_goals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `goals`
--
ALTER TABLE `goals`
  ADD CONSTRAINT `goals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `savings_goals`
--
ALTER TABLE `savings_goals`
  ADD CONSTRAINT `savings_goals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goals` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
