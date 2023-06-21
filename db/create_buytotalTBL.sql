use testdb;

drop table buytotal;

create table buytotal(
	_index int auto_increment primary key, 
	buyid varchar(20) not null,
    buyer varchar(20) not null,
	customerid varchar(20),
    flight varchar(20) not null,
    flightdate date not null,
    amount int not null,
    buydate date not null,
    note boolean not null   
);

select * from buytotal;

explain buytotal;

insert into buytotal values (NULL,'1','1','1','1','2023-01-01',4,'2023');