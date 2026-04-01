-- Write your query below


-- select name from customers left join customers on orders.customer_id = customers.id 

select name from customers left join orders on customers.id = orders.customer_id where orders.id is null;