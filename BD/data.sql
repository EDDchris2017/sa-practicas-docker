USE TIENDA;

CREATE TABLE VIDEOJUEGOS
(
    id int PRIMARY KEY,
    nombre varchar(30),
    genero varchar(20),
    plataforma varchar(20)
);

INSERT INTO VIDEOJUEGOS VALUES (1,"Super Mario Galaxy","Plataformas","Wii");
INSERT INTO VIDEOJUEGOS VALUES (2,"Forza Horizon 4","Conduccion","Xbox One");
INSERT INTO VIDEOJUEGOS VALUES (3,"God of War","Accion/Aventuras","PS4");
INSERT INTO VIDEOJUEGOS VALUES (4,"Resident evil 7","Survival Horror","Multiplataforma");
INSERT INTO VIDEOJUEGOS VALUES (5,"Gears of War 5","Accion","Xbox One");