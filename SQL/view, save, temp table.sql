use swiggy;
 -- view functions 
-- create the view 
create view rest as 
(select name,rating, city, rating_count as 'orders',
 cuisine, cost, cost*rating_count as revenue from restaurants);
 
 select * from rest;
 -- create view for end user 
 
 create view user_view as 
 (select name,rating, city, rating_count as 'orders',
 cuisine, cost from restaurants);
 
 -- view is just a type to see the data from different angles or adjust it according to whom it is to be sent, 
 -- it is basically an part original data only 
 
 -- create a view for sweet dishes
 create view sweet as 
 (select * from restaurants where cuisine = 'Sweets');
 
 -- Create A view of top 100 restraunts
 
 create view best as 
 (select name,rating, city, rating_count as 'orders',
 cuisine, cost, rating_count*cost as revenue from restaurants 
  group by name,rating, city,  orders,
 cuisine, cost
order by  rating_count*cost desc limit 100);

select * from best;

-- create view 1000 most expensive restaurants
 create view top_1000 as 
 (select * from restaurants order by cost desc limit 1000);
 
 
 -- how to save table and export it 
 -- create a new table sirsa_restraunts containing restraunts of sirsa only
 Create table sirsa_restraunts as  select * from restaurants 
 where city = 'Sirsa';
 -- create new table city_statistics that contains aggregate statistics of cities
 create table city_stats as select city, avg(rating) as averagerating , count(*) as total_restraunts from restaurants 
 group by city;
 select * from city_stats;
 
 -- create new table as expensive restaurants whose cost is more than 500
 Create table Expensive_restaurants as  select * from restaurants 
 where cost > 500;
 select * from  Expensive_restaurants;
 
 
 -- Temporary table 
 create temporary table temp_restaurants as select * from restaurants where city = 'Delhi';
 
 
 