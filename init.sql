create user IF NOT EXISTS 'www'@'%' identified with mysql_native_password by '$3cureUS';
create database IF NOT EXISTS cs4501 character set utf8;
grant all on cs4501.* to 'www'@'%';