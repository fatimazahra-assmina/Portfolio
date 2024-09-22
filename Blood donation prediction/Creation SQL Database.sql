CREATE DATABASE Don_du_sang;
use Don_du_sang;

create table Donateur (Id_donateur INT PRIMARY KEY NOT NULL,
 Nom_donateur VARCHAR(100),
 age_donateur INT, 
 email_donateur INT, 
 GS_donateur VARCHAR(5) );
 
CREATE TABLE Sang ( GS_sang VARCHAR (5) PRIMARY KEY, 
VS_Sang INT,
 Quantity INT);

CREATE TABLE CDP (Reserve_CDP INT PRIMARY KEY,
 BD_CDP Varchar(1000));
 
CREATE TABLE Fiche ( Frequency_fichemedicale INT PRIMARY KEY,
 Time_fichemedicale INT,
 Don_fiche_medicale2021 VARCHAR (2));
 
 
 
 
