-- SUB QUERY -- Very Important (nesting means subquery)
-- its a query inside another query
select * from products;
Select * from products
	where discounted_price = (select max(discounted_price) from products);
    
    
Create database Swiggy;
-- Which restraunt of abohar is visited by least number of people?
select min(rating_count) from restaurants;
use swiggy ;
select *
  from restaurants
  Where rating_count = (select min(rating_count) from restaurants
    ) and city = 'Abohar';


-- Which restraunt has generated maximum revenue all over india?

select max(rating_count*cost) from restaurants;
select * from restaurants
   WHERE rating_count*cost = (select max(rating_count*cost) from restaurants);
   
select * from restaurants;
-- how many restaurants have rating more than the average rating?

select avg(rating) from restaurants;
select count(*) from restaurants
   where rating >= (select avg(rating) from restaurants);
   
-- Which restraunt of delhi has generated most revenue?
select *
  from restaurants
  Where rating_count*cost = (select max(rating_count*cost) from restaurants where city = 'Delhi'
    ) and city = 'Delhi';
select * from restaurants 
where rating_count * cost = (select max(rating_count * cost) from restaurants 
where city = 'Delhi') 
and city = 'Delhi';

-- Which restraunt of more than average cost of an restraunt in delhi has generated most revenue
select avg(cost) from restaurants 
where city = ' delhi';
select max(rating_count*cost) from restaurants ;

select * from restaurants 
  where rating_count*cost = (select max(rating_count*cost) from restaurants Where city = 'Delhi')
  and cost > (select avg(cost) from restaurants 
where city = 'Delhi') 
and city = 'Delhi';
select * from restaurants where 
rating_count * cost = (select max(rating_count * cost) from restaurants where city = 'Delhi' 
						and cost > (select avg(cost) from restaurants where city = 'Delhi'))  and city = 'Delhi';
                        
                        





