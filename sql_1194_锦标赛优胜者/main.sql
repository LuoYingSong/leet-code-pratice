#https://leetcode-cn.com/problems/tournament-winners/
Create table If Not Exists Players (player_id int, group_id int);
Create table If Not Exists Matches (match_id int, first_player int, second_player int, first_score int, second_score int);
Truncate table Players;
insert into Players (player_id, group_id) values ('10', '2');
insert into Players (player_id, group_id) values ('15', '1');
insert into Players (player_id, group_id) values ('20', '3');
insert into Players (player_id, group_id) values ('25', '1');
insert into Players (player_id, group_id) values ('30', '1');
insert into Players (player_id, group_id) values ('35', '2');
insert into Players (player_id, group_id) values ('40', '3');
insert into Players (player_id, group_id) values ('45', '1');
insert into Players (player_id, group_id) values ('50', '2');
Truncate table Matches;
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('1', '15', '45', '3', '0');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('2', '30', '25', '1', '2');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('3', '30', '15', '2', '0');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('4', '40', '20', '5', '2');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('5', '35', '50', '1', '1');
#add
select group_id,player as 'player_id' from
    (select group_id,player,max(total) from
        (select player,group_id,sum(score) as total from
            (select first_player as 'player',first_score as 'score',group_id
            from Matches
            join Players
            on first_player=player_id
            union all
            select second_player,second_score,group_id
            from Matches
            join Players
            on first_player=player_id
                )t
        group by player
        order by player)t
    group by group_id)t;

select group_id,player as 'player_id' from(
select group_id,player,total,IF(@preGroup=group_id,null,1) as flag,@preGroup:=group_id from
        (select player,group_id,sum(score) as total from
            (select first_player as 'player',first_score as 'score',group_id
            from Matches
            join Players
            on first_player=player_id
            union all
            select second_player,second_score,group_id
            from Matches
            join Players
            on first_player=player_id
                )t
        group by player
        order by group_id,total desc ,player)t,(select @preGroup:=null)t2)
t where flag=1;

select group_id,player,max(total) from
        (select player,group_id,sum(score) as total from
            (select first_player as 'player',first_score as 'score',group_id
            from Matches
            join Players
            on first_player=player_id
            union all
            select second_player,second_score,group_id
            from Matches
            join Players
            on first_player=player_id
                )t
        group by player
        order by player)t
    group by group_id

select group_id,player,total,IF(@preGroup=group_id,null,1) as flag,@preGroup:=group_id from
        (select player,group_id,sum(score) as total from
            (select first_player as 'player',first_score as 'score',group_id
            from Matches
            join Players
            on first_player=player_id
            union all
            select second_player,second_score,group_id
            from Matches
            join Players
            on first_player=player_id
                )t
        group by player
        order by group_id,total desc ,player)t,(select @preGroup:=null)t2