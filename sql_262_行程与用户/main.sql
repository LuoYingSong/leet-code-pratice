#
# select count_,t.Request_at,case t.Request_at when  @prevDate then
#     case t.Status when  'completed'
#         then @curCompete := t.count_
#         else @curyUncompete :=  @curyUncompete + t.count_ end
#     else case t.Status when 'completed'
#         then @curCompete := t.count_  @curyUncompete := 0
#         else @curyUncompete := t.count_  @curCompete := 0 end end,
#     @print:=@curCompete/(@curyUncompete+@curCompete)  ,@prevDate := t.Request_at from
# (select
#        Trips.Status,Request_at,count(Request_at) count_
# from Trips join
#     (select * from Users where Role='client') c
#         on Trips.Client_Id =  c.Users_Id
# join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
# where c.Banned='No' and d.Banned='No' group by Request_at, Trips.Status order by Request_at,Status) t
# ,(SELECT @curCompete :=0, @curyUncompete :=0 ,@prevDate := NULL,@print := NULL) t2;
select * from (select * from
(select t1.Request_at Day ,round(ifnull(t2.count_,0)  / (ifnull(t2.count_,0)+ifnull(t1.count_,0)),2) as  'Cancellation Rate' from
((select
       Trips.Status,Request_at,count(Request_at) count_
from Trips join
    (select * from Users where Role='client') c
        on Trips.Client_Id =  c.Users_Id
join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
where c.Banned='No' and d.Banned='No'and Status='completed'
group by Request_at, Trips.Status
order by Request_at,Status)t1 left outer join (select
       Trips.Status,Request_at,count(Request_at) count_
from Trips join
    (select * from Users where Role='client') c
        on Trips.Client_Id =  c.Users_Id
join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
where c.Banned='No' and d.Banned='No'and Status!='completed' and Request_at is not null
group by Request_at, Trips.Status
order by Request_at,Status)t2 on t1.Request_at=t2.Request_at)where t1.Request_at >= '2013-10-01' and t1.Request_at <= '2013-10-03')t1
union
(select t1.Request_at Day ,round(ifnull(t2.count_,0)  / (ifnull(t2.count_,0)+ifnull(t1.count_,0)),2) as  'Cancellation Rate' from
((select
       Trips.Status,Request_at,count(Request_at) count_
from Trips join
    (select * from Users where Role='client') c
        on Trips.Client_Id =  c.Users_Id
join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
where c.Banned='No' and d.Banned='No'and Status='completed'
group by Request_at, Trips.Status
order by Request_at,Status)t1 right join (select
       Trips.Status,Request_at,count(Request_at) count_
from Trips join
    (select * from Users where Role='client') c
        on Trips.Client_Id =  c.Users_Id
join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
where c.Banned='No' and d.Banned='No'and Status!='completed' and Request_at is not null
group by Request_at, Trips.Status
order by Request_at,Status)t2 on t1.Request_at=t2.Request_at) where t1.Request_at >= '2013-10-01' and t1.Request_at <= '2013-10-03') )t;

select
       Trips.Status,Request_at,count(Request_at) count_
from Trips join
    (select * from Users where Role='client') c
        on Trips.Client_Id =  c.Users_Id
join (select * from Users where Role='driver') d on d.Users_Id=Trips.Driver_Id
where c.Banned='No' and d.Banned='No'and Trips.Status='completed'
group by Request_at, Trips.Status
order by Request_at,Status




##############################
select count(null)
