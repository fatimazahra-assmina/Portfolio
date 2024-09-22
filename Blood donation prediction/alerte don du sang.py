#importer les bibliothèques dont on a besoin 
import pandas as pd
import smtplib

#variables relatives au centre
reserve_sang=2000
stock_securite=3000 

#les informations de l'adresse électronique du centre 
your_email = "bloodcenter@gmail.com"
your_password = "bloodcenter"

#etablir la connection via gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

#lecture de la feuille excel (notre base de données)
email_list = pd.read_excel('C:\Users\HP\Downloads\Base de données-don du sang .xlsx')

#obtenir les noms et les adresses mails des donateurs 
names = email_list['NAME']
emails = email_list['EMAIL']


if reserve_sang < stock_securite :
    #parcourir la base de données 
    for i in range(len(emails)):
        
        #obtenir le nom et l'adresse e-mail du i-ème donateur
        name = names[i]
        email = emails[i]
        
        #le message d'alerte et d'appel au don
        message = "Bonjour " + name + "\nNous espérons que vous allez bien. Notre réserve du sang est sur le point de s’épuiser.\nDonner du sang et sauvez des vies !" 
        
        #envoyer un email
        server.sendmail(your_email, [email], message)

#fermer le serveur smtp 
server.close()