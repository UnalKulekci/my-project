# Database engine installation on EC2 instance

## After running EC2 instance(Linux or Ubuntu), update ( Best Practice )
```

sudo yum update -y (For linux machine)
sudo apt update && sudo apt upgrade -y (For ubuntu machine)

```

## `Download`, `Start` and `Enable` Mariadb

```
sudo yum install mariadb-server -y (For server and linux machine)
sudo yum install mariadb-client -y (For client and linux machine)
sudo apt-get install mariadb-server -y (For server and ubuntu machine)
sudo apt-get install mariadb-client -y (For client and ubuntu machine)

sudo systemctl start mariadb   ---> Starts mariadb service
sudo systemctl status mariadb  ---> Check of status mariadb service
sudo systemctl enable mariadb  ---> Enable mariadb service

```
## `Login ` to mysql db. `Connect` to the MariaDB Server and open MySQL CLI with root user, no password set as default.
```
mysql -u root 

```
## After this stage, we use `mysql commands` and Database commands are always ` ; ` ends with
```

SHOW DATABASES;     ---> Shows default dbs in mysql
SHOW TABLES;        --->Shows tables in db
USE <namedb>        ---> Switches the db we want to use
USE mysql;          --->Choose a database (mysql db) to work with. ⚠️ 
SELECT Host, User, Password FROM user;    ---># Show users defined in the db server currently.

```
## To establish a `secure connection` with the db
```

sudo mysql_secure_installation

```

##  Create new user 
```
CREATE USER <username> IDENTIED BY <userpassword> ;
```

## Create new database
```
CREATE DATABASE <dbname> ;
```
## Grant permissions to the user for database .
```
GRANT ALL ON <dbname>.* TO <username> IDENTIFIED BY <userpassword> WITH GRANT OPTION;
```

## Update privileges.
```

FLUSH PRIVILEGES;

```
## Login back as <username> using the password defined.
```
mysql -u <username> -p
```
## Create a table named offices.
```
CREATE TABLE `offices` (
  `office_id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  PRIMARY KEY (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Insert some data into the table named offices.
```
INSERT INTO `offices` VALUES (1,'03 Reinke Trail','Cincinnati','OH');
  ....
  ....
  ....
  ....
  ....
```

## List all records within offices table.
```
SELECT * FROM offices;
```

## Close the mysql terminal.
```
EXIT;
```

For detailed information with mariadb service and commands
```
https://mariadb.com/products/skysql/pricing/

```