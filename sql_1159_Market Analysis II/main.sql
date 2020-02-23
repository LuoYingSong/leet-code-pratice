# Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10))
# create table if not exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int)
# create table if not exists Items (item_id int, item_brand varchar(10))
# Truncate table Users
# insert into Users (user_id, join_date, favorite_brand) values ('1', '2019-01-01', 'Lenovo')
# insert into Users (user_id, join_date, favorite_brand) values ('2', '2019-02-09', 'Samsung')
# insert into Users (user_id, join_date, favorite_brand) values ('3', '2019-01-19', 'LG')
# insert into Users (user_id, join_date, favorite_brand) values ('4', '2019-05-21', 'HP')
# Truncate table Orders
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2')
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2019-08-02', '2', '1', '3')
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3')
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2019-08-04', '1', '4', '2')
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2019-08-04', '1', '3', '4')
# insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4')
# Truncate table Items
# insert into Items (item_id, item_brand) values ('1', 'Samsung')
# insert into Items (item_id, item_brand) values ('2', 'Lenovo')
# insert into Items (item_id, item_brand) values ('3', 'LG')
# insert into Items (item_id, item_brand) values ('4', 'HP')

select user_id,IF(user_id in (select seller_id from (
select *, @counter:=if(@pre=seller_id,@counter+1,1) as 'counter',@pre:=seller_id from (
select seller_id,u1.favorite_brand,Items.item_brand
from Orders
    left join Users u1 on u1.user_id = seller_id
    left join Users u2 on u2.user_id = buyer_id
    left join Items on Items.item_id = Orders.item_id
order by seller_id,seller_id)t,(select @pre:=null,@counter:=0)t2)t
where favorite_brand=item_brand and counter=2),'yes','no') as '2nd_item_fav_brand' from Users;
(select seller_id from (
select *, @counter:=if(@pre=seller_id,@counter+1,1) as 'counter',@pre:=seller_id from (
select seller_id,u1.favorite_brand,Items.item_brand
from Orders
    left join Users u1 on u1.user_id = seller_id
    left join Users u2 on u2.user_id = buyer_id
    left join Items on Items.item_id = Orders.item_id
order by seller_id,seller_id)t,(select @pre:=null,@counter:=0)t2)t
where favorite_brand=item_brand and counter=2);

select * from
(select * from (
select *, @counter:=if(@pre=seller_id,@counter+1,1) as 'counter',@pre:=seller_id from (
select seller_id,u1.favorite_brand,Items.item_brand
from Orders
    left join Users u1 on u1.user_id = seller_id
    left join Users u2 on u2.user_id = buyer_id
    left join Items on Items.item_id = Orders.item_id
order by seller_id,order_date)t,(select @pre:=null,@counter:=0)t2)t)t;