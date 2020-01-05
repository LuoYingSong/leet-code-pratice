Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-01', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

# end

select * from Activity t1,Activity t2
where datediff(t1.event_date,t2.event_date) = 1;

select t.event_date as 'install_dt',
       count(t.player_id) as 'installs',
       round(count(distinct Activity.player_id)/count(t.player_id),2) as 'Day1_retention'
from
(select player_id,min(event_date) as 'event_date' from Activity group by player_id)t
left join Activity on   Activity.event_date - t.event_date= 1 AND t.player_id = Activity.player_id
group by t.event_date;

select count(null);

select *,min(event_date) from Activity group by player_id