CREATE DATABASE Maitri_S026;

USE Maitri_S026;

CREATE TABLE Student (
    s_id INT PRIMARY KEY,
    s_name VARCHAR(30) NOT NULL,
    s_gender CHAR(1) CHECK (s_gender = 'M' OR s_gender = 'F'),
    s_contact VARCHAR(10) DEFAULT '0000000000',
    m_id INT,
    s_age INT
);

CREATE TABLE Mentor (
    m_id INT PRIMARY KEY,
    m_firstName VARCHAR(15) NOT NULL,
    m_middleName VARCHAR(15) NOT NULL,
    m_lastName VARCHAR(15) NOT NULL,
    m_contact VARCHAR(10) DEFAULT '0000000000',
    m_exp INT
);

CREATE TABLE Subject (
    sub_id INT PRIMARY KEY,
    sub_name VARCHAR(20),
    sub_credit FLOAT,
    s_id INT
);

CREATE TABLE StudyPattern (
    sp_no INT PRIMARY KEY,
    sp_methadology VARCHAR(20),
    sp_hours INT,
    s_id INT,
    m_id INT
);

CREATE TABLE Resources (
    r_no INT PRIMARY KEY,
    r_type VARCHAR(20),
    sub_id INT,
    s_id INT,
    m_id INT
);

CREATE TABLE Grades (
    g_id INT PRIMARY KEY,
    g_CGPA FLOAT,
    g_percentage FLOAT,
    g_grade VARCHAR(2),
    s_id INT,
    t_id INT
);

CREATE TABLE Test (
    t_id INT PRIMARY KEY,
    t_marks FLOAT,
    t_type VARCHAR(20),
    sub_id INT,
    s_id INT,
    m_id INT
);

CREATE TABLE Skills (
    skill_id INT PRIMARY KEY,
    skill_name VARCHAR(20),
    skill_type VARCHAR(20),
    skill_profeciency VARCHAR(20),
    s_id INT
);

CREATE TABLE hardSkills (
    skill_id INT,
    techDomain VARCHAR(20)
);

CREATE TABLE softSkills (
    skill_id INT,
    softDomain VARCHAR(20)
);

ALTER TABLE Student
    ADD FOREIGN KEY (m_id) REFERENCES Mentor(m_id);

ALTER TABLE StudyPattern
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE StudyPattern
    ADD FOREIGN KEY (m_id) REFERENCES Mentor(m_id);

ALTER TABLE Subject
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE Test
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE Test
    ADD FOREIGN KEY (m_id) REFERENCES Mentor(m_id);

ALTER TABLE Test
    ADD FOREIGN KEY (sub_id) REFERENCES Subject(sub_id);

ALTER TABLE Skills
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE Resources
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE Resources
    ADD FOREIGN KEY (m_id) REFERENCES Mentor(m_id);

ALTER TABLE Resources
    ADD FOREIGN KEY (sub_id) REFERENCES Subject(sub_id);

ALTER TABLE Grades
    ADD FOREIGN KEY (s_id) REFERENCES Student(s_id);

ALTER TABLE Grades
    ADD FOREIGN KEY (t_id) REFERENCES Test(t_id);
