update member set passwd='3759' where id='honekd@aaa.com';

select* from member;

update member set id='hongkd@aaa.com' where passwd='3759'

delete from member where id='hongkd@aaa.com';

delete from member;
alter

select reg_date from member;

select DATE_FORMAT(reg_date, '%Y-%m-%d %H:%i:%s') AS reg_date
FROM member;