INSERT into Donateur (Id_Donateur,Name_donateur,Age_donateur,Email_donateur,GS_donateur) 
values ("Donateur1","Aadi",55,"Donateur1@gmail.com","O+"), ("Donateur2","Aakav",38,"Donateur2@gmail.com","O+"), 
("Donateur3","Aakesh",18,"Donateur3@gmail.com","O-"), ("Donateur4","Aakil",53,"Donateur4@gmail.com","AB+"), 
("Donateur5","Aaliyah",33,"Donateur5@gmail.com","A-"), ("Donateur6","Aalok",24,"Donateur6@gmail.com","A+"), 
("Donateur7","Aamin",35,"Donateur7@gmail.com","A+"),("Donateur8","Aanan",35,"Donateur8@gmail.com","A-"),
("Donateur9","Aanandini",39,"Donateur9@gmail.com","AB-"),("Donateur10","Aandalib",42,"Donateur10@gmail.com","AB-"),
("Donateur11","Aaron",37,"Donateur11@gmail.com","AB-"), ("Donateur12","Aarona",49,"Donateur12@gmail.com","O+"),
("Donateur13","Aasta",33,"Donateur13@gmail.com","O-"),("Donateur14","Aatmadeva",43,"Donateur14@gmail.com","B+"),
("Donateur15","Aatmik",27,"Donateur15@gmail.com","B-");
INSERT into Sang (GS_sang,Quantity,idpoche_sang) 
values ("O+",12500,2816962967936),("O+",3250,6472350708713),("O-",4000,2696853734099),("AB+",5000,4411677536097),
("A-",6000,2139988392489),("A+",1000,9042678128738),("A+",1750,6687177490356),("A-",3000,5293098351972),
("AB-",2250,7577405528507),
("AB-",11500,1547587821744),("AB-",5750,3325850186467),("O+",750,8767832893859),("O-",2500,8358970650849),
("B+",3250,4852152692835),("B-",1500,8517654572714);
INSERT into Fichemedicale (Frequency_fichemedicale, Time_fichemedicale, donenmars2021_fichemedicale,num_fichemedicale) 
values (50,98,1,1),(13,28,1,2),(16,35,1,3),(20,45,1,4),(24,77,0,5),(4,4,0,6),(7,14,1,7),(12,35,0,8),(9,22,1,9),(46,98,1,10),
(23,58,0,11),(3,4,0,12),
(10,28,1,13),(13,47,0,14),(6,15,1,15);
ALTER TABLE Donateur
MODIFY COLUMN Id_Donateur VARCHAR(50) UNIQUE;



