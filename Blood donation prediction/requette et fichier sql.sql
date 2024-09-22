create database projet;
USE projet;

CREATE TABLE Donateur(
Id_donateur VARCHAR(50) PRIMARY KEY NOT NULL,
 Name_donateur VARCHAR(100),
 age_donateur INT,
 email_donateur INT,
 GS_donateur VARCHAR(5) );
 
CREATE TABLE Sang (
 GS_sang VARCHAR (5),
 VS_Sang INT,
 idpoche_sang INT PRIMARY KEY,
 Quantity INT NOT null);
 
CREATE TABLE CDP (
Reserve_CDP INT PRIMARY KEY,
 BD_CDP Varchar(1000) );
 
CREATE TABLE Fichemedicale( 
Frequency_fichemedicale INT,
Time_fichemedicale INT,
num_fichemedicale INT PRIMARY KEY,
Donenmars2021_fichemedicale VARCHAR (2));














