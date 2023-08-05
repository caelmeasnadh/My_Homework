# SQL. Lesson 2|3.
Я вибрав створювати базу фільми-актори-режисери, створював поступово, спочатку створив декілька колонок, потім додав ще пару за допомогою ``` alter table ```.

```sql
create database films;
\c films

create table actors (
    id serial,
    actor_name varchar(255) not null,
    birth_date int not null
);

create table directors (
    id serial,
    director_name varchar(255) not null,
    birth_date int not null
);

create table favorite_films (
    id serial,
    name varchar(255) not null,
    date_of_creation int not null
);

```

Далі заповнив таблиці інформацією :

```sql
insert into actors(actor_name, birth_date) values
('Woody Harrelson', 1961),
('Christian Bale', 1974),
('Morgan Freeman', 1937),
('Matthew McConaughey', 1969),
('Mark Waschke', 1972);

insert into directors(director_name, birth_date) values
('Matt Reeves', 1966)
('Christopher Nolan', 1970)
('Mary Harron', 1953)
('David Fincher', 1962)
('Baran bo Odar', 1978);

insert into favorite_films(name, date_of_creation) values
('War for the planet of Apes', 2017)
('Interstellar', 2014)
('American Psycho', 2000)
('Seven', 1995)
('Dark', 2017);

```
Потім додав ще декілька колонок :

```sql

alter table actors add column number_of_movies int not null default 5;
alter table directors add column director_number_of_movies int not null default 5;
alter table favorite_films add column rating int not null default 5;
alter table favorite_films add column viewed boolean not null default true;

```

Вже залив скріни з домашньою роботою №2, продублюю сюди запити з  ``` update, delete, fetch, truncate ``` :

```sql

update favorite_films set viewed = true where id = 5;

update favorite_films set name = 'Pans Labyrinth', date_of_creation = 2006 where id = 1;

delete from actors where actor_name = 'Mark Waschke';

select * from actors order by id offset 1 fetch first 3 rows only;

truncate table actors;

```

* Як приклад, декілька запитів :
  * перший виведе акторів та режисерів, які працювали разом;
  * другий акторів та фільми, у яких вони грали;
  * третій виведе актрів, режисерів, та фільми, над якими вони працювали.

```sql
select actor_name, director_name from actors a inner join directors d on (a.id = d.id);

select actor_name, name from actors a inner join favorite_films f on(a.id = f.id);

select actor_name, director_name, name from actors a inner join favorite_films f on(a.id = f.id) inner join directors d on (d.id = f.id);
```

[Мій дамп бази даних, ДЗ по SQL №1](https://github.com/caelmeasnadh/my_homework/blob/master/Lesson_1.SQL.sql)

[Друге дз з скріншотами запитів та дампом](https://github.com/caelmeasnadh/my_homework/tree/master/Lesson_2.%20SQL)











