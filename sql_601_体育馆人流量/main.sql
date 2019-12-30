#init
Create table If Not Exists stadium (id int, visit_date DATE NULL, people int)
Truncate table stadium
insert into stadium (id, visit_date, people) values ('1', '2017-01-01', '10')
insert into stadium (id, visit_date, people) values ('2', '2017-01-02', '109')
insert into stadium (id, visit_date, people) values ('3', '2017-01-03', '150')
insert into stadium (id, visit_date, people) values ('4', '2017-01-04', '99')
insert into stadium (id, visit_date, people) values ('5', '2017-01-05', '145')
insert into stadium (id, visit_date, people) values ('6', '2017-01-06', '1455')
insert into stadium (id, visit_date, people) values ('7', '2017-01-07', '199')
insert into stadium (id, visit_date, people) values ('8', '2017-01-08', '188'
)

#end
select * from stadium where people>100;

select id,visit_date,people from
(select COUNT(*) counter,group1 from
(select @count_:=IF(id-1=@preid,@count_+1,1),
       @groupID:=IF(id-1=@preid,@groupID,@groupID+1) as group1,
       if(@count>=3,people,null),
       @preid:=id,visit_date,id
from stadium,(select @preid:=null,@groupID:=0,@count_:=0)value where people>100)t2 GROUP BY t2.group1)t
join ((select @count_:=IF(id-1=@preid,@count_+1,1),
       @groupID2:=IF(id-1=@preid,@groupID2,@groupID2+1) as group1,
       if(@count>=3,people,null),people,
       @preid:=id,visit_date,id
from stadium,(select @preid:=null,@groupID2:=0,@count_:=0)value where people>100))t2
    on t.group1=t2.group1
where counter>3;



select id,group1,group_concat(id) from
(select @count_:=IF(id-1=@preid,@count_+1,1),
       @groupID:=IF(id-1=@preid,@groupID,@groupID+1) as group1,
       if(@count>=3,people,null),
       @preid:=id,visit_date,id
from stadium,(select @preid:=null,@groupID:=0,@count_:=0)value where people>100)t2 GROUP BY t2.group1
having count(*)>2 ;

(select @count_:=IF(id-1=@preid,@count_+1,1),
       @groupID:=IF(id-1=@preid,@groupID,@groupID+1) as group1,
       if(@count>=3,people,null),
       @preid:=id,visit_date,id,people
from stadium,(select @preid:=null,@groupID:=0,@count_:=0)value where people>100)


#end
SELECT r1.*, @flag := if((r1.countt >= 3 OR @flag = 1) AND r1.countt != 0, 1, 0) AS flag
	FROM (
		SELECT s.*, @count := if(s.people >= 100, @count + 1, 0) AS `countt`
		FROM stadium s, (SELECT @count := 0) b
	) r1, (SELECT @flag := 0) c
	ORDER BY id DESC

SELECT s.*, @count := if(s.people >= 100, @count + 1, 0) AS `countt`
		FROM stadium s, (SELECT @count := 0) b
# 作者：zhangyi
# 链接：https://leetcode-cn.com/problems/human-traffic-of-stadium/solution/zhi-xing-yong-shi-136msji-bai-963de-yong-hu-nei-cu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。