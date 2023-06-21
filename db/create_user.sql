use testdb;

-- drop table user;

create table user(userid char(6), passwd varchar(20)) default charset=utf8;

show tables;

explain user;

insert into user values('root', '1234');
insert into user values('admin', '1234');
insert into user values('user1', '1234');

-- select * from user;

SELECT * FROM customerTBL where email = '1234@naver.com';