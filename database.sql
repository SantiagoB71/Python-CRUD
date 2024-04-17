CREATE DATABASE IF NOT EXISTS notebook
use notebook


Create TABLE users(
    id int(25) auto_increment NOT NULL, 
    name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    password VARCHAR(150) NOT NULL,
    date DATE NOT NULL,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
 )ENGINE=InnoDB;


 CREATE TABLE notes(
    id int(25) auto_increment NOT NULL,
    user_id int(25) NOT NULL,
    title VARCHAR(100) NOT NULL,
    description MEDIUMTEXT,
    date DATE NOT NULL,
    CONSTRAINT PK_NOTES PRIMARY KEY(id),
    CONSTRAINT fk_user_note FOREIGN KEY(user_id) REFERENCES users (id)
 )ENGINE=InnoDB;