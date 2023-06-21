use testdb;

drop table customerTBL;

create table customerTBL(
	customerid varchar(20), 
    passwd varchar(20),
    customername char(20),
    birthdate char(8),
    gender boolean,
    phonenumber char(13),
    email varchar(20),
    addr nchar(30),
    pnum char(11)
    );
    
alter table customerTBL add constraint pk_customerid primary key(customerid);
alter table customerTBL modify column passwd varchar(20) not null;
alter table customerTBL modify customername char(20) not null;
alter table customerTBL modify birthdate char(8) not null;
alter table customerTBL modify gender boolean not null;
alter table customerTBL modify column phoneNumber char(13) not null;
alter table customerTBL modify column addr char(30) not null;
alter table customerTBL modify column email varchar(20) not null;
alter table customerTBL modify column pnum char(11) not null;

explain customerTBL;


insert into customerTBL values('user','12345678!@','seongha', "20000103", true, '01012345678', 'op_gg@naver.com','한국', 'as9103922'); 
select * from customerTBL;

delete from customerTBL where customerid = 'admin';
SELECT * FROM customerTBL;

SELECT * FROM customerTBL where customerid = 'id' and phoneNumber= '01012345678'; 

use testdb;
select * from st_info;