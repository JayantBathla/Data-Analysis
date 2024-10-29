use swiggy;
-- write new column containing average rating of restraunts throughout the dataset
select * , round(avg(rating) over(),2) from restaurants ;
-- Create new column containing  avg. rating count of restraunts throughout the dataset
select * , round(avg(rating_count) over()) from restaurants;

-- create column containing avg cost of the city where that specific restraunt is from
select * , round(avg(cost) over(partition by city)) from restaurants;

-- create column containing avg cost of the cuisine  that specific restraunt sells
select * , round(avg(cost) over(partition by cuisine)) from restaurants;
 
-- create both columns together
select * , round(avg(cost) over(partition by city))
         , round(avg(cost) over(partition by cuisine))
 from restaurants;

-- list of restraunt whose cost is more than the avg cost of restraunts
select * ,avg(cost) over() from restaurants;
select * from (select * ,avg(cost) over() as avg_cost from restaurants) t where t.cost > t.avg;


-- rank every restaurant from most expensive to least expensive
select * ,rank() over(order by cost) from restaurants;

-- rank every resaurant from most visited to least visited
select * ,rank() over(order by rating_count Desc) from restaurants;


-- Rank every restrauntfrom most expensice to least expensive based on thier city
select * ,rank() over(partition by city order by cost)
 from restaurants;
   
 -- dense rank every restaurant from most expensive to least expensive as per their city 
 select * , dense_rank() over(partition by city order by cost)
 from restaurants;
 
 -- row number every rank from most expensive to least expensive as per their city
      
 select * ,row_number() over(partition by city order by cost desc)
 from restaurants;
 
 -- rank every restraunt  from most expensive to least expensive as per their city  along with its city as Adilabad - 1, adilabad - 2
 select *,concat(city , '-', row_number() over(partition by city order by cost desc))
 from restaurants;
 
 -- Find top 5 restaurants as per their revenue               
 select * from (select*  ,cost*rating_count, row_number () over(partition by city order by rating_count *  cost desc) as revevnue  from restaurants)t 
 Where t > 6;
 
 use swiggy;
 
 

 
 
 