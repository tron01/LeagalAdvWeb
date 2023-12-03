-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2023 at 07:23 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `law`
--

-- --------------------------------------------------------

--
-- Table structure for table `advocate`
--

CREATE TABLE `advocate` (
  `adv_id` int(100) NOT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `adv_img` varchar(100) DEFAULT NULL,
  `adv_name` varchar(100) DEFAULT NULL,
  `adv_enroll_no` varchar(100) DEFAULT NULL,
  `adv_qual` varchar(100) DEFAULT NULL,
  `adv_age` varchar(100) DEFAULT NULL,
  `adv_gender` varchar(100) DEFAULT NULL,
  `adv_email` varchar(100) DEFAULT NULL,
  `adv_phone` varchar(100) DEFAULT NULL,
  `adv_address` varchar(100) DEFAULT NULL,
  `adv_category` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `advocate`
--

INSERT INTO `advocate` (`adv_id`, `user_id`, `adv_img`, `adv_name`, `adv_enroll_no`, `adv_qual`, `adv_age`, `adv_gender`, `adv_email`, `adv_phone`, `adv_address`, `adv_category`) VALUES
(1, '3', '/Media/team5_77dr4IM.jpg', 'Raj', '#442422424', 'llb', '54', 'male', 'raj123@gmail.com', '4324242424', 'kochi', 'Criminal lawyer');

-- --------------------------------------------------------

--
-- Table structure for table `case_request`
--

CREATE TABLE `case_request` (
  `case_id` int(100) NOT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `case_title` varchar(100) DEFAULT NULL,
  `case_desc` varchar(100) DEFAULT NULL,
  `case_file` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `ipc_sections` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `case_request`
--

INSERT INTO `case_request` (`case_id`, `adv_id`, `user_id`, `case_title`, `case_desc`, `case_file`, `status`, `ipc_sections`, `posted_date`) VALUES
(1, '3', '2', 'test 1', 'test111', '/Media/case.txt', 'Proceeding', 'Section 463 to 489 -E', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cat_id` int(100) NOT NULL,
  `cat_name` varchar(100) NOT NULL,
  `cat_description` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cat_id`, `cat_name`, `cat_description`) VALUES
(2, 'Family lawyer', ' family lawyer is the type of lawyer who’ll be best equipped to guide you through the process which lies before you'),
(3, 'Intellectual Property  Lawyer', 'Intellectual property (IP) lawyers protect and enforce the rights and creations of inventors, authors, artists, and businesses.'),
(4, 'Tax lawyer', ' A tax attorney specializes in the many intricacies of federal, state, and local tax laws and should be able to provide advice on the particular tax issue you face.'),
(5, 'Personal injury lawyer', 'Personal injury lawyers work primarily in civil litigations, representing clients who have sustained an injury. '),
(6, 'Bankruptcy lawyer', 'If you’re having financial difficulties and are contemplating bankruptcy proceedings, you’ll want to consult with a bankruptcy attorney.'),
(7, 'Corporate lawyer', 'Corporate lawyers handle legal matters for corporations and ensure that all business transactions are in compliance with the law. '),
(8, 'Immigration lawyer', 'Immigration lawyers play a pivotal role in providing guidance to individuals and families navigating the necessary requirements to live, work, or study in the U.S.');

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `doc_id` int(100) NOT NULL,
  `case_id` varchar(100) DEFAULT NULL,
  `u_id` varchar(100) DEFAULT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `doc_name` varchar(100) DEFAULT NULL,
  `document` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `documents`
--

INSERT INTO `documents` (`doc_id`, `case_id`, `u_id`, `adv_id`, `doc_name`, `document`, `posted_date`) VALUES
(1, '1', '2', NULL, 'doctest1', '/Media/case2.txt', '2023-11-08'),
(4, '1', NULL, '3', 'advTestDoc3', '/Media/adv_doc_AdqN3TP.txt', '2023-11-16');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feed_id` int(100) NOT NULL,
  `user_id` int(100) NOT NULL,
  `feed_subject` varchar(100) DEFAULT NULL,
  `feed_description` varchar(500) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ipc`
--

CREATE TABLE `ipc` (
  `ipc_id` int(100) NOT NULL,
  `ipc_section` varchar(100) DEFAULT NULL,
  `ipc_description` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ipc`
--

INSERT INTO `ipc` (`ipc_id`, `ipc_section`, `ipc_description`) VALUES
(1, 'Sections 120A to 120B.', 'criminal conspiracy.'),
(2, 'Sections 121 to 130', 'Offences against the State'),
(3, 'Sections 141 to 160', 'Offences against the Public Tranquillity'),
(4, 'Sections 171A to 171I', 'Offences Relating to Elections'),
(5, 'Sections 172 to 190', 'Offences relating to coin and Government Stamps'),
(6, 'Sections 264 to 267', 'Offences relating to Weight and Measures'),
(7, 'Sections 268 to 294', 'Offences affecting the Public Health, Safety, Convenience, Decency and Morals.'),
(8, 'Sections 295 to 298', 'Offences relating to Religion'),
(9, 'Sections 299 to 377', 'Offences affecting the Human Body.'),
(10, 'Sections 378 to 462', 'Offences Against Property'),
(11, 'Section 463 to 489 -E', 'Offences relating to Documents and Property Marks'),
(12, 'Sections 493 to 498', 'Offences related to marriage'),
(13, 'Sections 499 to 502', 'Offences related to Defamation');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `user_id` int(100) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user_id`, `username`, `password`, `type`, `status`) VALUES
(1, 'admin', '123', 'admin', '1'),
(2, 'aju123@gmail.com', '123', 'user', '1'),
(3, 'raj123@gmail.com', '1234', 'advocate', '1');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pay_id` int(100) NOT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `case_id` varchar(100) DEFAULT NULL,
  `posted_date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `paid_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_id`, `user_id`, `adv_id`, `case_id`, `posted_date`, `amount`, `paid_date`, `status`) VALUES
(1, '2', '3', '1', '2023-11-16', '2000', '2023-12-03', 'Not Paid');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `rate_id` int(100) NOT NULL,
  `case_id` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `adv_id` varchar(100) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `rate_desc` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `u_id` int(100) NOT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `u_img` varchar(100) DEFAULT NULL,
  `u_name` varchar(100) DEFAULT NULL,
  `u_age` varchar(100) DEFAULT NULL,
  `u_gender` varchar(100) DEFAULT NULL,
  `u_email` varchar(100) DEFAULT NULL,
  `u_phone` varchar(100) DEFAULT NULL,
  `u_aadhar` varchar(50) NOT NULL,
  `u_address` varchar(100) DEFAULT NULL,
  `u_account` varchar(100) DEFAULT NULL,
  `u_cvv` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `user_id`, `u_img`, `u_name`, `u_age`, `u_gender`, `u_email`, `u_phone`, `u_aadhar`, `u_address`, `u_account`, `u_cvv`) VALUES
(1, '2', '/Media/team7_g6zZjcY.jpg', 'Aju', '20', 'male', 'aju123@gmail.com', '1231313131', '313131233131', 'nnn', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advocate`
--
ALTER TABLE `advocate`
  ADD PRIMARY KEY (`adv_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `case_request`
--
ALTER TABLE `case_request`
  ADD PRIMARY KEY (`case_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cat_id`);

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`doc_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feed_id`),
  ADD KEY `feedback_ibfk_1` (`user_id`);

--
-- Indexes for table `ipc`
--
ALTER TABLE `ipc`
  ADD PRIMARY KEY (`ipc_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pay_id`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`rate_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`u_id`),
  ADD KEY `user_ibfk_1` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `advocate`
--
ALTER TABLE `advocate`
  MODIFY `adv_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `case_request`
--
ALTER TABLE `case_request`
  MODIFY `case_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cat_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `doc_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feed_id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ipc`
--
ALTER TABLE `ipc`
  MODIFY `ipc_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `user_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pay_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `rate_id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `u_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
