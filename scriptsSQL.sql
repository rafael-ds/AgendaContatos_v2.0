/*Scripts SQL*/

CREATE TABLE CONTATOS(

	IDCONTATOS INT PRIMARY KEY AUTO_INCREMENT,
	NOME_CONT VARCHAR(30) NOT NULL,
	EMAIL VARCHAR(15),
	TELEFONE VARCHAR(15) NOT NULL,
	ID_USUARIO INT NOT NULL,

	FOREIGN KEY(ID_USUARIO)
	REFERENCES USUARIO(IDUSUARIO)


);



 contatos;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| IDCONTATOS | int(11)     | NO   | PRI | NULL    | auto_increment |
| NOME_CONT  | varchar(30) | NO   |     | NULL    |                |
| EMAIL      | varchar(15) | YES  |     | NULL    |                |
| TELEFONE   | varchar(15) | NO   |     | NULL    |                |
| ID_USUARIO | int(11)     | NO   | MUL | NULL    |                |
+------------+-------------+------+-----+---------+----------------+

# ALTERANDO A COLUNA EMAIL
ALTER TABLE CONTATOS
CHANGE EMAIL EMAIL VARCHAR(30);

-- Buscando todos os contatos apartir de ID
SELECT NOME_CONT, EMAIL, TELEFONE
FROM CONTATOS
WHERE ID_USUARIO = 1;





