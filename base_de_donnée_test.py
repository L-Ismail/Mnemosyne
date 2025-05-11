import sqlite3 as sl 

connexion = sl.connect("bd_test.db")

curseur = connexion.cursor()

curseur.execute ('''CREATE TABLE eleve(
identifiant VARCHAR (15) PRIMARY KEY,
nom VARCHAR (20),
prenom VARCHAR(80),
departement VARCHAR (30),
age INTEGRER
)
''')


curseur.execute ('''INSERT INTO eleve (identifiant, nom, prenom, departement, age) VALUES
('0805', 'Dumont', 'Alice', 'Economie et Gestion', 24),
('0905', 'Levesque', 'Robert', 'Medecine', 23),
('1005', 'Lemoine', 'Jean', 'Informatique', 22) ''')

#Un test pour vérifier que j'ai bien inséré les données:

def info_eleve(identifiant) :
    curseur.execute("SELECT * FROM eleve WHERE identifiant = ?", (identifiant,))
    print ("Information élève-------\n", curseur.fetchall())


info_eleve('0805')

curseur.close()
connexion.close()