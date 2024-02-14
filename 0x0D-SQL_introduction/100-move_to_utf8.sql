-- a script that converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table CONVERTE TO CHARACTER SET utf8mb COLLATE utf8mb4_unicode_ci;
