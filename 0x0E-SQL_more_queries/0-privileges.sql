-- a script that lists user previlages
SELECT *
FROM INFORMATION_SCHEMA.USER_PRIVILEGES
WHERE GRANTEE = 'user_0d_1';
SELECT *
FROM INFORMATION_SCHEMA.USER_PRIVILEGES
WHERE GRANTEE = 'user_0d_2';
