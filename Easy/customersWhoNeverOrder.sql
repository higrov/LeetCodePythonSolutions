Create table If Not Exists Customers (id int, name varchar(255))
Create table If Not Exists Orders (id int, customerId int)
Truncate table Customers
insert into Customers (id, name) values ('1', 'Joe')
insert into Customers (id, name) values ('2', 'Henry')
insert into Customers (id, name) values ('3', 'Sam')
insert into Customers (id, name) values ('4', 'Max')
Truncate table Orders
insert into Orders (id, customerId) values ('1', '3')
insert into Orders (id, customerId) values ('2', '1')


Select c.name as Customers from 
(Select id, c.name , orderId , customerId from Customers c left join 
(Select  o.id as orderId, customerId from orders o) as o on c.id = o.customerId ) as c 
where c.orderId is Null