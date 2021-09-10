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



-- Buscando por contato
SELECT NOME_CONT, EMAIL, TELEFONE
FROM CONTATOS
WHERE ID_USUARIO = 1 


SELECT NOME_CONT, EMAIL, TELEFONE
FROM CONTATOS
WHERE ID_USUARIO = 1 
AND NOME_CONT = 'Dani';



/* Alterando os contatos */


SELECT NOME, EMAIL, TELEFONE
FROM CONTATOS_TS
WHERE ID_USUARIO = 1;

UPDATE CONTATOS_TS 
SET EMAIL = 'fernandoJSP@HOTM'
WHERE NOME = 'MANINHO'
AND ID_USUARIO = 1;

+---------+-------------------+-----------+
| NOME    | EMAIL             | TELEFONE  |
+---------+-------------------+-----------+
| MILENA  | NULL              | 999999    |
| CAMILA  | CAMILA@GMAIL.COM  | 333333333 |
| MANINHO | FERNADO@GMAIL.COM | 444444    |
| eliza   | eliza@gmail.com   | 6666666   |
| eliza   | eliza@gmail.com   | 6666666   |
| eliza   | eliza@gmail.com   | 6666666   |
| derick  | deric@gmail.com   | 111111    |
| barbara | bar@gmail.com     | 77777     |
+---------+-------------------+-----------+
+--------------+---------+------------------+-----------+------------+
| IDCONTATO_TS | NOME    | EMAIL            | TELEFONE  | ID_USUARIO |
+--------------+---------+------------------+-----------+------------+
|            1 | MILENA  | NULL             | 999999    |          1 |
|            2 | MILENA  | NULL             | 999999    |          3 |
|            3 | MILENA  | NULL             | 999999    |          2 |
|            4 | CAMILA  | CAMILA@GMAIL.COM | 333333333 |          1 |
|            5 | ZELU    | ZE@HOTMAIL.COM   | 222222222 |          3 |
|            6 | MANINHO | fernandoJSP@HOTM | 444444    |          1 |
|            7 | eliza   | eliza@gmail.com  | 6666666   |          1 |
|            8 | eliza   | eliza@gmail.com  | 6666666   |          1 |
|            9 | eliza   | eliza@gmail.com  | 6666666   |          1 |
|           10 | derick  | deric@gmail.com  | 111111    |          1 |
|           11 | barbara | bar@gmail.com    | 77777     |          1 |
|           12 | zeze    | zz@gmail.com     | 12345678  |          3 |
|           13 | rose    | rose@hotmail.com | 11117778  |          2 |
+--------------+---------+------------------+-----------+------------+


UPDATE CONTATOS_TS 
SET TELEFONE = '1111111111'
WHERE NOME = 'MILENA'
AND ID_USUARIO = 3;
+--------------+---------+------------------+------------+------------+
| IDCONTATO_TS | NOME    | EMAIL            | TELEFONE   | ID_USUARIO |
+--------------+---------+------------------+------------+------------+
|            1 | MILENA  | NULL             | 999999     |          1 |
|            2 | MILENA  | NULL             | 1111111111 |          3 |
|            3 | MILENA  | NULL             | 999999     |          2 |
|            4 | CAMILA  | CAMILA@GMAIL.COM | 333333333  |          1 |
|            5 | ZELU    | ZE@HOTMAIL.COM   | 222222222  |          3 |
|            6 | MANINHO | fernandoJSP@HOTM | 444444     |          1 |
|            7 | eliza   | eliza@gmail.com  | 6666666    |          1 |
|            8 | eliza   | eliza@gmail.com  | 6666666    |          1 |
|            9 | eliza   | eliza@gmail.com  | 6666666    |          1 |
|           10 | derick  | deric@gmail.com  | 111111     |          1 |
|           11 | barbara | bar@gmail.com    | 77777      |          1 |
|           12 | zeze    | zz@gmail.com     | 12345678   |          3 |
|           13 | rose    | rose@hotmail.com | 11117778   |          2 |
+--------------+---------+------------------+------------+------------+
------------------------------------------------------------------------------------


+--------------+-----------+-------+------+
| IDUSUARIO_TS | NOME_USER | SENHA | TIPO |
+--------------+-----------+-------+------+
|            1 | RAFAEL    | 1234  | ADM  |
|            2 | EDNA      | 3564  | ADM  |
|            3 | MANU      | 8756  | USL  |
+--------------+-----------+-------+------+

/* EXCLUINDO CONTATO */


DELETE FROM CONTATOS_TS
WHERE NOME = 'MILENA'
AND ID_USUARIO = 1;




/* APAGANDO REGISTRO DE UMA AGENDA */