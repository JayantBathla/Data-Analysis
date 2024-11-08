select * from employee;
select * from album;
-- Who is the senior most employee based on job title?
select * from employee 
       order by levels desc limit 1;


-- Which countries have the most Invoices?
select billing_country , count(billing_country) from invoice
       group by billing_country
	   Order by count(billing_country)
	   Desc limit 5;

-- What are top 3 values of total invoice?
select total from invoice 
      order by total
	  desc limit 3
	  ;



-- Which city has the best customers? We would like to throw a promotional Music Festival in the city we made the most money.
-- Write a query that returns one city that has the highest sum of invoice totals. Return both the city name & sum of all invoice totals
select billing_city , sum(total) from invoice
      group by billing_city
	  order by sum(total)
	  desc limit 1;


-- Who is the best customer? The customer who has spent the most money will be declared the best customer. 
-- Write a query that returns the person who has spent the most money

select customer.customer_id, customer.first_name,customer.last_name , sum(total) from customer
    join invoice 
	on customer.customer_id = invoice.customer_id
	group by customer.customer_id 
	order by sum(total)
	desc limit 1;



-- Write query to return the email, first name, last name, & Genre of all Rock Music listeners.
-- Return your list ordered alphabetically by email starting with A

SELECT DISTINCT (email),first_name, last_name
FROM customer
JOIN invoice ON customer.customer_id = invoice.customer_id
JOIN invoice_line ON invoice.invoice_id = invoice_line.invoice_id
WHERE track_id IN(
	SELECT track_id FROM track
	JOIN genre ON track.genre_id = genre.genre_id
	WHERE genre.name LIKE 'Rock'
)
ORDER BY email;


-- Let's invite the artists who have written the most rock music in our dataset.
-- Write a query that returns the Artist name and total track count of the top 10 rock bands


select artist.name , artist.artist_id, count(track.track_id) from track
	  join album on album.album_id = track.album_id
	  join artist on artist.artist_id = album.artist_id
	  join genre on track.genre_id = genre.genre_id
	  where genre.name like 'Rock'
	  group by  artist.artist_id
	  order by count(track.track_id)
	  desc limit 10;



-- Return all the track names that have a song length longer than the average song length. 
-- Return the Name and Milliseconds for each track. Order by the song length with the longest songs listed first
select track.name,  track.milliseconds from track 
where length(track.name) > (select round(avg(length(track.name)),2) from track)
order by track.milliseconds desc ;



-- Find how much amount spent by each customer on artists? 
-- Write a query to return customer name, artist name and total spent

with customer_details as 
    (select invoice_line.invoice_id as idd, customer.first_name as f_name, sum(invoice_line.unit_price * invoice_line.quantity) as amt_spent
	  from customer join invoice on customer.customer_id = invoice.customer_id
	  join invoice_line on invoice.invoice_id = invoice_line.invoice_id
	  group by customer.first_name, idd order by amt_spent desc) ,

	  artist_deets as
	  (select artist.name as a_name,invoice_line.invoice_id as idd1, count(invoice_id) from artist
	  join album on artist.artist_id = album.artist_id
	  join track on track.album_id = album.album_id 
	  join invoice_line on  invoice_line.track_id =track.track_id 
	  group by artist.name, idd1 order by count(invoice_id))

select customer_details.f_name, customer_details.amt_spent, artist_deets.a_name from customer_details
join artist_deets on artist_deets.idd1 = customer_details.idd



-- We want to find out the most popular music Genre for each country. 
-- We determine the most popular genre as the genre with the highest amount of purchases. 
-- Write a query that returns each country along with the top Genre. 
-- For countries where the maximum number of purchases is shared return all Genres

WITH popular_genre AS 
(
    SELECT COUNT(invoice_line.quantity) AS purchases, customer.country, genre.name, genre.genre_id, 
	ROW_NUMBER() OVER(PARTITION BY customer.country ORDER BY COUNT(invoice_line.quantity) DESC) AS RowNo 
    FROM invoice_line 
	JOIN invoice ON invoice.invoice_id = invoice_line.invoice_id
	JOIN customer ON customer.customer_id = invoice.customer_id
	JOIN track ON track.track_id = invoice_line.track_id
	JOIN genre ON genre.genre_id = track.genre_id
	GROUP BY 2,3,4
	ORDER BY 2 ASC, 1 DESC
)
SELECT * FROM popular_genre WHERE RowNo <= 1




-- Write a query that determines the customer that has spent the most on music for each country. 
-- Write a query that returns the country along with the top customer and how much they spent. 
-- For countries where the top amount spent is shared, provide all customers who spent this amount

WITH Customter_with_country AS (
		SELECT customer.customer_id,first_name,last_name,billing_country,SUM(total) AS total_spending,
	    ROW_NUMBER() OVER(PARTITION BY billing_country ORDER BY SUM(total) DESC) AS RowNo 
		FROM invoice
		JOIN customer ON customer.customer_id = invoice.customer_id
		GROUP BY 1,2,3,4
		ORDER BY 4 ASC,5 DESC)
SELECT * FROM Customter_with_country WHERE RowNo <= 1
