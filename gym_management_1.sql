-- Create Database
-- CREATE DATABASE sakshi_project_db;

-- Use database
 USE sakshi_project_db;

-- =========================
-- TABLE 1: USERS (for login)
-- =========================
-- CREATE TABLE users (
  --   user_id INT PRIMARY KEY AUTO_INCREMENT,
 --    username VARCHAR(50) UNIQUE NOT NULL,
 --    password VARCHAR(100) NOT NULL
-- );

-- =========================
-- TABLE 2: MEMBERS / STUDENTS
-- =========================
-- CREATE TABLE members (
 --    member_id INT PRIMARY KEY AUTO_INCREMENT,
 --    name VARCHAR(100),
 --    age INT,
 --    phone VARCHAR(15),
  --   email VARCHAR(100)- 
-- );

-- =========================
-- TABLE 3: PLANS (gym plan / course plan)
-- =========================
-- CREATE TABLE plans (
   --  plan_id INT PRIMARY KEY AUTO_INCREMENT,
   --  plan_name VARCHAR(50),
   --  duration_months INT,
   --  fees INT
-- );

-- =========================
-- TABLE 4: MEMBER_PLAN (mapping)
-- =========================
-- CREATE TABLE member_plan (
  --   id INT PRIMARY KEY AUTO_INCREMENT,
  --   member_id INT,
   --  plan_id INT,
   --  start_date DATE,
   --  end_date DATE,
    
   --  FOREIGN KEY (member_id) REFERENCES members(member_id),
   --  FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
-- );

-- =========================
-- INSERT SAMPLE DATA
-- =========================

-- INSERT INTO users (username, password)
-- VALUES ('admin', 'admin123');

-- INSERT INTO plans (plan_name, duration_months, fees)
-- VALUES 
-- ('Basic', 1, 1000),
-- ('Standard', 3, 2500),
-- ('Premium', 6, 4500);


-- CREATE TABLE attendance (
  --   attendance_id INT PRIMARY KEY AUTO_INCREMENT,
  --   member_id INT,
  --   visit_date DATE,
  --   FOREIGN KEY (member_id) REFERENCES members(member_id)
-- );
 SHOW TABLES;