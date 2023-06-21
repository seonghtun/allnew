use testdb;

drop table customerDetailTBL;

create table customerDetailTBL(
	customerId varchar(20),
	maileage int default 0,
    membershipLevel int default 0,
	foreign key (customerId) references customerTBL(customerId) on update cascade
);

explain customerDetailTBL;

insert into customerDetailTBL values('id', default, default);

select * from customerDetailTBL;