# import sqlite3 module
import sqlite3
  
# create con object to connect 
# the database geeks_db.db
con = sqlite3.connect("db.sqlite3")
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data
cur.executescript("""

CREATE TABLE UsuCab
(
  IdeUsu INTEGER NOT NULL,
  PriNomUsu varchar(50) NOT NULL,
  SegNomUsu varchar(50) NOT NULL,
  PriApeUsu varchar(50) NOT NULL,
  SegApeUsu varchar(50) NOT NULL,
  SexUsu character(1) NOT NULL,
  CorUsu varchar(50) NOT NULL,
  ImgUsu varchar(100) NOT NULL,
  ConUsu varchar(100) NOT NULL,
  CONSTRAINT PK_UsuCab PRIMARY KEY (IdeUsu)
);
-- Table ZonTurHor

CREATE TABLE ZonTurHor
(
  ZonTurIde INTEGER NOT NULL,
  ZonTurIng time NOT NULL,
  ZonTurSal time NOT NULL,
  ZonTurDia varchar(50) NOT NULL,
  CONSTRAINT PK_ZonTurHor PRIMARY KEY (ZonTurIde)
);
-- Table TipAtr

CREATE TABLE TipAtr
(
  TipAtrIde INTEGER NOT NULL,
  TipAtrNom varchar(50) NOT NULL,
  TipAtrIdeEst boolean NOT NULL,
  CONSTRAINT PK_TipAtr PRIMARY KEY (TipAtrIde)
);
-- Table Atr

CREATE TABLE Atr
(
  AtrIde INTEGER NOT NULL,
  AtrNom varchar(50) NOT NULL,
  AtrDes TEXT NOT NULL,
  TipAtrIde INTEGER,
  CONSTRAINT PK_Atr PRIMARY KEY (AtrIde),
  CONSTRAINT Relationship9 FOREIGN KEY (TipAtrIde) REFERENCES TipAtr (TipAtrIde)
);

CREATE INDEX IX_Relationship9 ON Atr (TipAtrIde);



-- Table ZonTur

CREATE TABLE ZonTur
(
  ZonTurIde INTEGER NOT NULL,
  ZonTurNom varchar(50) NOT NULL,
  ZonTurDir varchar(200) NOT NULL,
  ZonTurPun INTEGER NOT NULL,
  ZonTurIma varchar(100) NOT NULL,
  ZonTurDes TEXT NOT NULL,
  ZonTurNumVis INTEGER NOT NULL,
  FecPub date NOT NULL,
  FecIngUsu date NOT NULL,
  AtrIde INTEGER NOT NULL,
  identificador_usuario INTEGER,
  CONSTRAINT PK_ZonTur PRIMARY KEY (ZonTurIde,AtrIde),
  CONSTRAINT Relationship16 FOREIGN KEY (ZonTurIde) REFERENCES ZonTurHor (ZonTurIde),
  CONSTRAINT Relationship22 FOREIGN KEY (AtrIde) REFERENCES Atr (AtrIde),
  CONSTRAINT Relationship30 FOREIGN KEY (identificador_usuario) REFERENCES UsuCab (IdeUsu)
);

CREATE INDEX IX_Relationship16 ON ZonTur (ZonTurIde);

CREATE INDEX IX_Relationship30 ON ZonTur (identificador_usuario);



-- Table ZonTurCom

CREATE TABLE ZonTurCom
(
  ComIde INTEGER NOT NULL,
  ComCon TEXT NOT NULL,
  ComNumLik INTEGER NOT NULL,
  IdeUsu INTEGER NOT NULL,
  ZonTurIde INTEGER NOT NULL,
  AtrIde INTEGER NOT NULL,
  CONSTRAINT PK_ZonTurCom PRIMARY KEY (ComIde,IdeUsu,ZonTurIde,AtrIde),
  CONSTRAINT Relationship23 FOREIGN KEY (IdeUsu) REFERENCES UsuCab (IdeUsu),
  CONSTRAINT Relationship31 FOREIGN KEY (ZonTurIde, AtrIde) REFERENCES ZonTur (ZonTurIde, AtrIde)
);


-- Table List

CREATE TABLE List
(
  IdeLis INTEGER NOT NULL,
  NomLis varchar(50) NOT NULL,
  IdeZonTur varchar(100) NOT NULL,
  IdeUsu INTEGER NOT NULL,
  CONSTRAINT PK_List PRIMARY KEY (IdeLis,IdeUsu),
  CONSTRAINT Relationship7 FOREIGN KEY (IdeUsu) REFERENCES UsuCab (IdeUsu)
);

-- Table ZonTur_List

CREATE TABLE ZonTur_List
(
  ZonTurIde INTEGER NOT NULL,
  IdeLis INTEGER NOT NULL,
  IdeUsu INTEGER NOT NULL,
  AtrIde INTEGER NOT NULL,
  CONSTRAINT PK_ZonTur_List PRIMARY KEY (ZonTurIde,IdeLis,IdeUsu,AtrIde),
  CONSTRAINT Relationship18 FOREIGN KEY (ZonTurIde, AtrIde) REFERENCES ZonTur (ZonTurIde, AtrIde),
  CONSTRAINT Relationship19 FOREIGN KEY (IdeLis, IdeUsu) REFERENCES List (IdeLis, IdeUsu)
);
""")
  
# display the data in the table by 
# executing the cursor object
  
# fetch all the data
print(cur.fetchall())