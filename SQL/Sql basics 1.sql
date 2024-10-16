 create database  SQL1;
 create database if not exists SQL1;
 create table if not exists table_1 ;
   (
     user_id INT,
     username VARCHAR(255),
     email VARCHAR(50),
     age INT,
     city VARCHAR(100)
   );
 create table if not exists SQL1.table_4 
  (
     user_id INT,
    username VARCHAR(255),
     email VARCHAR(50),
     age INT,
    city VARCHAR(100)
   );
   
Alter table table_4 
     Add column Email_add Varchar(200);
Alter table table_4 
	Rename column Email_id to Email_id1;     
 Alter table table_4 
     Drop column Email_id1;    


 insert into table_1 (user_id, username, email, age, city)
 	Values
    (1,'Jayant', 'jayantbathla@gmail.com', 21, 'Gzb'),
    (1,'Jayant', 'jayantbathla@gmail.com', 21, 'Gzb'),
    (1,'Jayant', 'jayantbathla@gmail.com', 21, 'Gzb');
    
 select * from table_1
 insert into table_1 
   Values
    (1,'Jayant', 'Gzb');
 insert into table_1 (user_id, username, city)
  Values
    (1,'Jayant', 'Gzb');


-- Now we will add constraints which can be added while defining the table definition part 

 create table if not exists SQL1.table_6
     (  
    user_id INT,
    username VARCHAR(255) PRIMARY KEY,
    email VARCHAR(50) NOT NULL UNIQUE,
     -- Not null will ensure that this field is not empty and unique is added so no same emails
    age INT CHECK (age >= 18)  NOT NULL,
    -- check will put constraint on age to be greater than equal to 18
   city VARCHAR(100),
--   marital_status 	BOOLEAN DEFAULT false 
-- if some one fills they married then true if not filled then it will choose default value false
  );
 insert into table_5 (user_id, city)  
 -- (It will give error as we didnt fill username which is primary key)
   Values
  (1, 'Gzb');

 insert into table_5 (username, user_id, age)
    Values
       ('Jayant', 1, 21);
insert into table_5 (username, user_id, age)
    Values
       ('Jayant', 2, 21) 
--  (This shows error as username is primary key and it cant be duplicate)







