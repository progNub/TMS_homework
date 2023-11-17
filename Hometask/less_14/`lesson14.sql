drop database TMS;
create database TMS;

use TMS;
create table users
(
    id       int primary key auto_increment,
    username varchar(50) not null,
    password varchar(50) not null,
    email    varchar(50) unique
);

create table orders
(
    id         int primary key auto_increment,
    user_id    int,
    product_id int,
    count      int,
    foreign key (user_id) references users (id)
);

create table products
(
    id        int primary key auto_increment,
    name      varchar(50),
    cost      int,
    count     int,
    seller_id int
);

alter table orders
    add foreign key (product_id) references products (id);

create table seller
(
    id      int primary key auto_increment,
    company varchar(50),
    phone   varchar(20)
);

alter table products
    add foreign key (seller_id) references seller (id);
