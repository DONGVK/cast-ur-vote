#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

DROP DATABASE IF EXISTS sf;
CREATE DATABASE sf;
USE sf;

#------------------------------------------------------------
# Table: Utilisateur
#------------------------------------------------------------

CREATE TABLE Utilisateur(
        id_user          Int  Auto_increment  NOT NULL ,
        last_name         Varchar (50) NOT NULL ,
        first_name        Varchar (50) NOT NULL ,
        birth_date       Date NOT NULL ,
        email            Varchar (50) NOT NULL ,
        password         Varchar (100) NOT NULL ,
        vote 	Int NOT NULL,
        id_candidat Int
	,CONSTRAINT Utilisateur_PK PRIMARY KEY (id_user)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Candidat
#------------------------------------------------------------

CREATE TABLE Candidat(
        id_candidat   Int  Auto_increment  NOT NULL ,
        prog          TEXT,
	CONSTRAINT Candidat_PK PRIMARY KEY (id_candidat)
)ENGINE=InnoDB;

#------------------------------------------------------------
# Table: Acandidat
#------------------------------------------------------------
CREATE TABLE ACandidat(
        id_acandidat          Int  Auto_increment  NOT NULL ,
        last_name         Varchar (50) NOT NULL ,
        first_name        Varchar (50) NOT NULL ,
        birth_date       Date NOT NULL ,
        email            Varchar (50) NOT NULL ,
        password         Varchar (100) NOT NULL ,
        vote 	Int NOT NULL,
	CONSTRAINT Utilisateur_PK PRIMARY KEY (id_acandidat)
)ENGINE=InnoDB;

#------------------------------------------------------------
# Table: Admin
#------------------------------------------------------------

CREATE TABLE Admin(
        id_admin          Int Auto_increment NOT NULL ,
        last_name         Varchar (50) NOT NULL ,
        first_name        Varchar (50) NOT NULL ,
        birth_date       Date NOT NULL ,
        email            Varchar (50) NOT NULL ,
        password         Varchar (100) NOT NULL ,
	CONSTRAINT Admin_PK PRIMARY KEY (id_admin)
)ENGINE=InnoDB;

/*
ALTER TABLE Utilisateur
	ADD CONSTRAINT Utilisateur_Candidat_FK
	FOREIGN KEY (id_candidat)
	REFERENCES Candidat(id_candidat);
*/
#------------------------------------------------------------
# INSERT
#------------------------------------------------------------
INSERT INTO Utilisateur(last_name, first_name, birth_date, email, password, vote, id_candidat) VALUES
	("DENTE", "Alberto", "2000-06-21", "quelque@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 123456789, NULL),
    ("MACRON", "Emmanuel", "1977-12-21", "macron@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 654123789, 1);
    
INSERT INTO Candidat(prog) VALUES
    ("La République en marche ( LRM )");

INSERT INTO Admin(last_name, first_name, birth_date, email, password) VALUES
    ("DONG", "Jean", "2000-11-06", "jean@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO");
    
INSERT INTO ACandidat(last_name, first_name, birth_date, email, password, vote) VALUES
	("SOSO", "Sophie", "2000-06-21", "sophie@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 123456789),
    ("MOMO", "Moha", "1977-12-21", "moha@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 654123789);