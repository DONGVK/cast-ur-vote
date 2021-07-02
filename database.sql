#------------------------------------------------------------
#        Script MySQL.
#	@Author : DONG
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
        id_candidat Int,
        img varchar(500)
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
INSERT INTO Utilisateur(last_name, first_name, birth_date, email, password, vote, id_candidat, img) VALUES
	("DENTE", "Alberto", "2000-06-21", "quelque@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 123456789, NULL, NULL),
    ("MACRON", "Emmanuel", "1977-12-21", "macron@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 654123789, 1, "https://upload.wikimedia.org/wikipedia/commons/c/c3/Emmanuel_Macron_%28cropped%29.jpg"),
    ("LE PEN", "Marine", "1968-08-05", "lepen@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 147852145, 2, "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Marine_Le_Pen_%282017-03-24%29_01_cropped.jpg/220px-Marine_Le_Pen_%282017-03-24%29_01_cropped.jpg"),
    ("HAMON", "Benoît", "1967-06-26", "hamont@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 12784596, 3, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Beno%C3%AEt_Hamon_place_de_R%C3%A9publique_plan_serr%C3%A9_%28cropped%29.jpg/220px-Beno%C3%AEt_Hamon_place_de_R%C3%A9publique_plan_serr%C3%A9_%28cropped%29.jpg"),
    ("POUTOU", "Philippe", "1967-03-14", "poutou@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 659874184, 4, "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Philippe_Poutou_-_Gilets_jaunes_%282019%29.jpg/220px-Philippe_Poutou_-_Gilets_jaunes_%282019%29.jpg"),
    ("LASALLE", "Jean", "1955-05-03", "lasalle@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 745881233, 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Jean_Lassalle_03_%28cropped%29.jpg/220px-Jean_Lassalle_03_%28cropped%29.jpg"),
    ("FILLON", "François", "1954-03-04", "lasalle@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 547812364, 6, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Fran%C3%A7ois_Fillon_2010.jpg/220px-Fran%C3%A7ois_Fillon_2010.jpg")
    ;
    
INSERT INTO Candidat(prog) VALUES
    ("La République en marche ( LERM )"),
    ("Rassemblement National (RN)"),
    ("Mouvement des jeunes socialistes"),
    ("Nouveau Parti anticapitaliste"),
    ("Résistons !"),
    ("Groupe Union pour un mouvement populaire (UMP)")
    ;

INSERT INTO Admin(last_name, first_name, birth_date, email, password) VALUES
    ("DONG", "Jean", "2000-11-06", "jean@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO");
    
INSERT INTO ACandidat(last_name, first_name, birth_date, email, password, vote) VALUES
	("SOSO", "Sophie", "2000-06-21", "sophie@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 123456789),
    ("MOMO", "Moha", "1977-12-21", "moha@mail.com", "$2b$12$TegbtNfT/zJ9yGTr8FRUL.9iuGUAGJLncTvXysHiFpfFmjr40vFIO", 654123789);
