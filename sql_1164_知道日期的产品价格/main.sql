# Create table If Not Exists Products (product_id int, new_price int, change_date date)
# Truncate table Products
# insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14')
# insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14')
# insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15')
# insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16')
# insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17')
# insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18')

select product_id,new_price as 'price' from
    (select *,@flag:=IF(product_id=@preId,0,1) as 'flag' ,@preId:=product_id
from
(select *
from Products
where change_date<='2019-08-16'
order by product_id,change_date desc)t,(select @preId:=null,@flag:=null)t2)t
where flag
union
select product_id,10 from Products where product_id not in (select product_id from Products
    where change_date<='2019-08-16');
