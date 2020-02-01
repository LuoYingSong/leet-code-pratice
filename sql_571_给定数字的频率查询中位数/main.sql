Create table If Not Exists Numbers (Number int, Frequency int);
Truncate table Numbers;
insert into Numbers (Number, Frequency) values ('0', '7');
insert into Numbers (Number, Frequency) values ('1', '1');
insert into Numbers (Number, Frequency) values ('2', '3');
insert into Numbers (Number, Frequency) values ('3', '1');

select sum(Frequency) from Numbers;

select round(avg(Number),1) from
(select *,IF((select sum(Frequency) from Numbers)%2,IF(sum_<round((select sum(Frequency) from Numbers)/2)+1,1,0),IF(sum_<=round((select sum(Frequency) from Numbers)/2)+1,1,0)) as 'flag' from
              (select * ,@sum_:=@sum_+Frequency as 'sum_' from Numbers,(select @sum_:=0)t)t
where sum_ >= (select sum(Frequency) from Numbers)/2)t
where flag = 1
group by flag;

select round(avg(Number),1) as 'median' from
(select *,IF((select sum(Frequency) from Numbers)%2,IF(sum_<round((select sum(Frequency) from Numbers)/2)+1,1,0),
    IF(sum_<=round((select sum(Frequency) from Numbers)/2)+1,1,0)) as 'flag' from
              (select * ,@sum_:=@sum_+Frequency as 'sum_' from (select * from Numbers order by Number asc)t2,(select @sum_:=0)t)t
where sum_ >= (select sum(Frequency) from Numbers)/2)t
where flag = 1;

select IF((select sum(Frequency) from Numbers)%2,min(Number),
    IF(sum_=round((select sum(Frequency) from Numbers)/2),min(Number),avg(Number))) as 'flag' from
(select * from
              (select * ,@sum_:=@sum_+Frequency as 'sum_' from (select * from Numbers order by Number asc)t2,(select @sum_:=0)t)t
where sum_ >= (select sum(Frequency) from Numbers)/2 limit 2) t;


select
n1.number,
n1.frequency,
(select sum(frequency) from Numbers n2 where n2.Number<=n1.number) as asc_frequency,
(select sum(frequency) from Numbers n3 where n3.Number>=n1.number) as desc_frequency
from Numbers n1;

select IF((select sum(Frequency) from Numbers)%2,min(Number),
    IF(sum_=round((select sum(Frequency) from Numbers)/2),avg(Number),min(Number))) as 'median' from
(select * from
              (select * ,@sum_:=@sum_+Frequency as 'sum_' from (select * from Numbers order by Number asc)t2,(select @sum_:=0)t)t
where sum_ >= (select sum(Frequency) from Numbers)/2 limit 2) t;