#add
Create table If Not Exists seat(id int, student varchar(255));
Truncate table seat;
insert into seat (id, student) values ('1', 'Abbot');
insert into seat (id, student) values ('2', 'Doris');
insert into seat (id, student) values ('3', 'Emerson');
insert into seat (id, student) values ('4', 'Green');
insert into seat (id, student) values ('5', 'Jeames');

select student from
(select *, if(id%2,id+1,id-1) as 'id2' from seat)t order by id2;

select id from
(select id,student,if(id%2,id+1,id-1) as 'id2' from seat)t order by id2;