-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 13, 2022 at 05:59 PM
-- Server version: 8.0.28-0ubuntu0.20.04.3
-- PHP Version: 7.3.33-1+ubuntu20.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LMS`
--

-- --------------------------------------------------------

--
-- Table structure for table `Auth_group`
--

CREATE TABLE `Auth_group` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Auth_permission`
--

CREATE TABLE `Auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add profile', 7, 'add_profile'),
(26, 'Can change profile', 7, 'change_profile'),
(27, 'Can delete profile', 7, 'delete_profile'),
(28, 'Can view profile', 7, 'view_profile'),
(29, 'Can add book', 8, 'add_book'),
(30, 'Can change book', 8, 'change_book'),
(31, 'Can delete book', 8, 'delete_book'),
(32, 'Can view book', 8, 'view_book');

-- --------------------------------------------------------

--
-- Table structure for table `Auth_profile`
--

CREATE TABLE `Auth_profile` (
  `id` int NOT NULL,
  `bio` longtext NOT NULL,
  `phone_number` varchar(12) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Auth_user`
--

CREATE TABLE `Auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Auth_user`
--

INSERT INTO `Auth_user` (`id`, `password`, `last_login`, `email`, `first_name`, `last_name`, `date_joined`, `is_active`, `is_staff`, `is_superuser`, `status`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'pbkdf2_sha256$150000$J98NqpLRmmQt$ZDyk67O2dMwOXziPtBN1zf/nc/Z99sbhytLdjajcIAo=', '2022-04-13 17:23:31.941654', 'dev.sunil.shaw@gmail.com', 'Sunil Kumar', 'Shaw', '2022-04-13 17:22:46.129548', 1, 1, 1, 0, 0, '2022-04-13', '2022-04-13');

-- --------------------------------------------------------

--
-- Table structure for table `Auth_user_groups`
--

CREATE TABLE `Auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Auth_user_user_permissions`
--

CREATE TABLE `Auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Book_book`
--

CREATE TABLE `Book_book` (
  `id` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `summary` longtext NOT NULL,
  `author` longtext NOT NULL,
  `book_code` varchar(255) NOT NULL,
  `no_of_book` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Book_book`
--

INSERT INTO `Book_book` (`id`, `title`, `summary`, `author`, `book_code`, `no_of_book`, `status`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'dsfgrz', 'sfdgsfddrgy', 'Menu Kohliz', '120xcdgfdxzz', 2001, 1, 0, '2022-04-13', '2022-04-13');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'Auth', 'profile'),
(6, 'Auth', 'user'),
(8, 'Book', 'book'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-04-13 17:18:44.518205'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-04-13 17:18:48.015211'),
(3, 'auth', '0001_initial', '2022-04-13 17:18:50.750214'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-04-13 17:19:00.589975'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-04-13 17:19:00.773054'),
(6, 'auth', '0004_alter_user_username_opts', '2022-04-13 17:19:00.920379'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-04-13 17:19:01.059374'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-04-13 17:19:01.190582'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-04-13 17:19:01.364085'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-04-13 17:19:01.516073'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-04-13 17:19:01.687918'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-04-13 17:19:02.033999'),
(13, 'auth', '0011_update_proxy_permissions', '2022-04-13 17:19:02.211987'),
(14, 'Auth', '0001_initial', '2022-04-13 17:19:08.573974'),
(15, 'Book', '0001_initial', '2022-04-13 17:19:23.636370'),
(16, 'admin', '0001_initial', '2022-04-13 17:19:24.770283'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-04-13 17:19:30.144466'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-04-13 17:19:30.297229'),
(19, 'sessions', '0001_initial', '2022-04-13 17:19:31.260354'),
(20, 'Book', '0002_auto_20220413_1742', '2022-04-13 17:42:49.741000');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('q8fzwy2fqciv9imy952mzft0pbd1xwr8', 'ZTAxNDgzNGMyMmFkZDMzNjY2OGE2MjRiZjBkNDQxYzllZWVmNzc2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYzdhY2NiMTM3YTBmM2I4M2VlNjFiNjJiMTI0NDY4MGRkN2VjODI0In0=', '2022-04-27 17:23:32.056470');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Auth_group`
--
ALTER TABLE `Auth_group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `Auth_permission`
--
ALTER TABLE `Auth_permission`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `Auth_profile`
--
ALTER TABLE `Auth_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `Auth_user`
--
ALTER TABLE `Auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `Auth_user_groups`
--
ALTER TABLE `Auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Auth_user_groups_user_id_group_id_921b23aa_uniq` (`user_id`,`group_id`),
  ADD KEY `Auth_user_groups_group_id_7f08c832_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `Auth_user_user_permissions`
--
ALTER TABLE `Auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Auth_user_user_permissions_user_id_permission_id_26a4eb17_uniq` (`user_id`,`permission_id`),
  ADD KEY `Auth_user_user_permi_permission_id_1375db89_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `Book_book`
--
ALTER TABLE `Book_book`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Book_code` (`book_code`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_Auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Auth_group`
--
ALTER TABLE `Auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Auth_permission`
--
ALTER TABLE `Auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `Auth_profile`
--
ALTER TABLE `Auth_profile`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Auth_user`
--
ALTER TABLE `Auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Auth_user_groups`
--
ALTER TABLE `Auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Auth_user_user_permissions`
--
ALTER TABLE `Auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Book_book`
--
ALTER TABLE `Book_book`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `Auth_profile`
--
ALTER TABLE `Auth_profile`
  ADD CONSTRAINT `Auth_profile_user_id_2ad0f394_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `Auth_user` (`id`);

--
-- Constraints for table `Auth_user_groups`
--
ALTER TABLE `Auth_user_groups`
  ADD CONSTRAINT `Auth_user_groups_group_id_7f08c832_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `Auth_user_groups_user_id_851066aa_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `Auth_user` (`id`);

--
-- Constraints for table `Auth_user_user_permissions`
--
ALTER TABLE `Auth_user_user_permissions`
  ADD CONSTRAINT `Auth_user_user_permi_permission_id_1375db89_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `Auth_user_user_permissions_user_id_36d68527_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `Auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `Auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
