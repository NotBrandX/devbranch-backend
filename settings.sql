DROP DATABASE devbranch;
DROP USER devbranchuser;
CREATE DATABASE devbranch;
CREATE USER devbranchuser WITH PASSWORD 'devbranch';
GRANT ALL PRIVILEGES ON DATABASE devbranch TO devbranchuser;