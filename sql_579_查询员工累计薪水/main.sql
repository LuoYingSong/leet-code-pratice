#add
drop table Employee;
Create table If Not Exists Employee (Id int, Month int, Salary int);
Truncate table Employee;
insert into Employee (Id, Month, Salary) values ('1', '1', '20');
insert into Employee (Id, Month, Salary) values ('2', '1', '20');
insert into Employee (Id, Month, Salary) values ('1', '2', '30');
insert into Employee (Id, Month, Salary) values ('2', '2', '30');
insert into Employee (Id, Month, Salary) values ('3', '2', '40');
insert into Employee (Id, Month, Salary) values ('1', '3', '40');
insert into Employee (Id, Month, Salary) values ('3', '3', '60');
insert into Employee (Id, Month, Salary) values ('1', '4', '60');
insert into Employee (Id, Month, Salary) values ('3', '4', '70');
#end
select Id as 'id',ROUND(Month,0) as 'month',Salary2 as 'Salary' from
(select *,
       @money := ROUND(IF(@preId=Id,@money+Salary,Salary),0) as 'Salary2',
       @preId:=Id from
(select Employee.Id,Employee.Month,Employee.Salary from Employee join (
    select max(Month) as 'max_month',
           id
    from Employee
    group by id)t
    on t.Id=Employee.id where Month !=max_month
)t,(select @preId := null,@money:=null)t2 order by t.id,Month)t order by Id,Month desc ;



select
       @money := ROUND(IF(@preId=Id ,@money+Salary,Salary),0) as 'Salary2',
       @countt := IF(@preId=Id,@countt-1,3),
       @preId:=Id
       from
(select Employee.Id,Employee.Month,Employee.Salary from Employee join (
    select max(Month) as 'max_month',
           id
    from Employee
    group by id)t
    on t.Id=Employee.id where Month !=max_month
)t,(select @preId := null,@money:=null,@countt:=3)t2 order by t.id,Month;

select *
from Employee t1,
     Employee t2,
     Employee t3
where t1.Month = t2.Month - 1 and t2.Month = t3.Month-1 and t1.Id=t2.id and t1.id=t3.Id;

select *,sum(t2.Salary)
from Employee t1,
     Employee t2
where t1.Month<=t2.Month
and t1.Month>=t2.Month-2
and t1.id = t2.id
and t1.Id =1
group by t1.Id,t1.Month
order by t1.id;
;
select *
from Employee t1,
     Employee t2
where
t1.id = t2.id
and t1.Month<=t2.Month
and t1.Month>=t2.Month-2
and t1.id=1;

select t1.id,t2.Month,sum(t1.Salary) as 'Salary'
from Employee t1,
     Employee t2
where
t1.id = t2.id
and t1.Month<=t2.Month
and t1.Month>=t2.Month-2
and (t1.id,t2.Month) not in (select id,max(Month) from Employee group by id)
group by t2.Id,t2.Month
order by Id,Month desc;


