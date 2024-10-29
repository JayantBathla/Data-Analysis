-- Create database myntra;
-- use myntra;
select * from myntra.products;
select product_name, brand_name from products;

select rating ,brand_name, rating_count, marked_price, discounted_price 
, marked_price - discounted_price as dicount_amt from products;
-- marked_price - discounted price is just shown in results its not permanent to make it add in orginal sheet youll have to us alter command
 
select rating ,brand_name, rating_count, marked_price, discounted_price ,discount_percent,
marked_price - discounted_price as dicount_amt, round (((marked_price - discounted_price)/marked_price) * 100,2)
 as discount_perc from products;

select rating_count*rating as rating_filter from products;

select distinct(brand_name) from products;
select product_name, brand_name, rating_count, rating from products where brand_name = 'Nike';

select distinct * from products;
select distinct (brand_name) from products;
select count(distinct(brand_name)) from products;

--  Q1)find how many tshirts are there in the data set

select count(*) from products
        where product_tag = 'tshirts';
        
select distinct(product_tag) from products;

-- Q2) Find brands that are selling tshirts 
select distinct(brand_name) from products
        where product_tag = 'tshirts';

select count(distinct(brand_name)) from products
        where product_tag = 'tshirts';
        

-- how to go for multiple conditions
select distinct * from products
       where brand_tag = 'adidas' and discounted_price > 5000;
       
       
-- Q3) find how many tshirts are there under 1000rs

select count(*) from products
        where product_tag = 'tshirts' and discounted_price < 1000;
        
-- Q4) find the name of brands that are selling shirts with price more than 5000
select distinct(brand_name) from products
        where product_tag = 'shirts' and discounted_price > 5000;

select count(distinct(brand_name)) from products
        where product_tag = 'shirts' and discounted_price > 5000;
        
-- Q5) different categories Blackberrys serves in under 5000rs

select distinct(product_tag) from products
        where brand_name = 'Blackberrys' and discounted_price <5000;

select count(distinct(product_tag)) from products
        where brand_name = 'Blackberrys' and discounted_price <5000;
        
-- Q6) Find Nike tshirts between range 2000-3000

select * from products
        where brand_name = 'NIKE' and product_tag = 'tshirts' and discounted_price between 2000 and 3000;


-- Q7 Find tshirts between 2000- 3000 from either nike or adidas

select * from products
        where brand_name = 'NIKE' or brand_name = 'ADIDAS' and product_tag = 'tshirts' and discounted_price between 2000 and 3000;
        
-- using not
select distinct * from products
  where not (brand_name = 'adidas') and (discounted_price between 5000 and 8000);
  
-- alternate of brand_name = 'NIKE' or brand_name = 'ADIDAS'
 
select distinct * from products
  where brand_name in ('adidas', 'nike') and (discounted_price between 5000 and 8000)






 








