Create table If Not Exists Scores (Id int, Score DECIMAL(3,2));
Truncate table Scores;
insert into Scores (Id, Score) values ('1', '3.5');
insert into Scores (Id, Score) values ('2', '3.65');
insert into Scores (Id, Score) values ('3', '4.0');
insert into Scores (Id, Score) values ('4', '3.85');
insert into Scores (Id, Score) values ('5', '4.0');
insert into Scores (Id, Score) values ('6', '3.65');



select t3.Score,t2.Rank from Scores t3 join
(select t1.score,count(t1.count_) Rank from
(SELECT distinct s1.Score score,s2.Score count_
FROM Scores s1 , Scores s2
where s1.Score <= s2.Score
order by s1.Score DESC ) t1 group by t1.score) t2
on t2.score = t3.Score order by t3.Score DESC;



SELECT Score, Rank FROM
(SELECT Score,
@curRank := IF(@prevRank = Score, @curRank+0,@curRank:=@curRank+1) AS Rank,
@prevRank := Score
FROM Scores, (
SELECT @curRank :=0, @prevRank := NULL
) r
ORDER BY Score DESC) s;

SELECT Score,
@curRank := IF(@prevRank = Score, @curRank+0,@curRank:=@curRank+1) AS Rank,
@prevRank := Score
FROM Scores, (
SELECT @curRank :=0, @prevRank := NULL)t;