# https://leetcode-cn.com/problems/average-salary-departments-vs-company/
Create table If Not Exists salary (id int, employee_id int, amount int, pay_date date);
Create table If Not Exists employee (employee_id int, department_id int);
Truncate table salary;
insert into salary (id, employee_id, amount, pay_date) values ('1', '1', '9000', '2017/03/31');
insert into salary (id, employee_id, amount, pay_date) values ('2', '2', '6000', '2017/03/31');
insert into salary (id, employee_id, amount, pay_date) values ('3', '3', '10000', '2017/03/31');
insert into salary (id, employee_id, amount, pay_date) values ('4', '1', '7000', '2017/02/28');
insert into salary (id, employee_id, amount, pay_date) values ('5', '2', '6000', '2017/02/28');
insert into salary (id, employee_id, amount, pay_date) values ('6', '3', '8000', '2017/02/28');
Truncate table employee;
insert into employee (employee_id, department_id) values ('1', '1');
insert into employee (employee_id, department_id) values ('2', '2');
insert into employee (employee_id, department_id) values ('3', '2');
# end


select t.date as 'pay_month',
       department_id,
       IF(department_money=company_money,'same',IF(department_money>company_money,'higher','lower'))
           as 'comparison' from
    (select DATE_FORMAT(pay_date,'%Y-%m') as date,department_id,avg(amount) as 'department_money'
    from salary
    join employee
    on employee.employee_id = salary.employee_id
    group by DATE_FORMAT(pay_date,'%Y-%m'),department_id)t
        join(select avg(amount) as 'company_money' ,DATE_FORMAT(pay_date,'%Y-%m') as 'date'
from salary
group by DATE_FORMAT(pay_date,'%Y-%m'))t2 on t.date=t2.date order by t.date desc,department_id;

select avg(amount),DATE_FORMAT(pay_date,'%Y-%m')
from salary
#     join employee
#         on salary.employee_id = employee.employee_id
group by DATE_FORMAT(pay_date,'%Y-%m');