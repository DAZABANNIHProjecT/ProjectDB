use agency;
insert into passport(number, birth_date) 
values  (7173747326, '1998-10-17'),
		(7542734544, '1996-11-18'),
		(6477944460, '1995-04-21'),
		(6093802026, '1998-09-21'),
		(8499033354, '1999-03-07'),
		(5010246565, '1997-12-17'),
		(6219220669, '1997-08-10'),
		(1697914010, '1995-10-06'),
		(6484599165, '1999-05-19'),
		(6699699644, '1997-04-02');
        
insert into owner(phone_number, passport_id) 
values  (8278000733, 1),
		(8456959793, 2),
		(8545089151, 3),
		(8893401832, 4),
		(8043720601, 5),
		(8300723811, 6),
		(8401686903, 7),
		(8665803121, 8),
		(8588453300, 9),
		(8085816431, 10);
        
insert into house(street, parking, playground, floors_count) 
values  ('Народного Ополчения', 0, 3, 54),
		('Потаповский переулок', 0, 1, 48),
		('Ленинградский проспект', 1, 3, 41),
		('Ленинградский проспект', 2, 1, 58),
		('Дмитровское шоссе', 1, 3, 6),
		('Липчанского', 1, 0, 6),
		('4-я Марьиной рощи', 1, 2, 66),
		('4-я Марьиной рощи', 1, 3, 58),
		('Потаповский переулок', 0, 3, 66),
		('Народного Ополчения', 1, 0, 58);
        
insert into transport_accessibility(house_id, distance_underground, distance_bus_stop) 
values  (1, 747, 150),
		(2, 429, 779),
		(3, 868, 868),
		(4, 284, 341),
		(5, 754, 196),
		(6, 361, 312),
		(7, 137, 342),
		(8, 788, 633),
		(9, 530, 107),
		(10, 775, 651);

insert into photo(flat_id, link_to_photo) 
values  (1, 'static/images/flat_1/photo.jpg'),
		(2, 'static/images/flat_2/photo.jpg'),
		(3, 'static/images/flat_3/photo.jpg'),
		(4, 'static/images/flat_4/photo.jpg'),
		(5, 'static/images/flat_5/photo.jpg'),
		(6, 'static/images/flat_6/photo.jpg'),
		(7, 'static/images/flat_7/photo.jpg'),
		(8, 'static/images/flat_8/photo.jpg'),
		(9, 'static/images/flat_9/photo.jpg'),
		(10, 'static/images/flat_10/photo.jpg');

insert into flat(house_id, floor, area, rooms, price, owner_id, photo_id) 
values  (1, 1, 35, 2, 8839823, 1, 1),
		(2, 2, 31, 2, 6839823, 2, 2),
		(3, 6, 45, 1, 8842313, 3, 3),
		(4, 1, 33, 1, 3456789, 4, 4),
		(5, 3, 40, 1, 5678900, 5, 5),
		(6, 5, 33, 2, 4567890, 6, 6),
		(7, 3, 47, 2, 3499789, 7, 7),
		(8, 6, 35, 1, 8797898, 8, 8),
		(9, 5, 46, 1, 9876546, 9, 9),
		(10, 2, 31, 2, 7646578, 10, 10);
        
insert into client(phone_number, email)
values (8903030459, 'user1@mail.ru'),
		(8509478151, 'user2@mail.ru'),
		(8871585022, 'user3@mail.ru'),
		(8845979268, 'user4@mail.ru'),
		(8881398321, 'user5@mail.ru'),
		(8782118867, 'user6@mail.ru'),
		(8544565203, 'user7@mail.ru'),
		(8114758196, 'user8@mail.ru'),
		(8639681986, 'user9@mail.ru'),
		(8887234360, 'user10@mail.ru');
        
insert into positions(position_name, city)
values ('analyst', 'Moscow'),
		('agent', 'Vladimir'),
		('supervisor', 'Sochi'),
		('agent', 'Kaliningrad'),
        ('analyst', 'Kaliningrad'),
		('agent', 'Sochi'),
		('supervisor', 'Vladimir'),
		('supervisor', 'Moscow'),
        ('analyst', 'Vladimir'),
		('agent', 'Moscow');

        
insert into vacancy(position_id, expirience, salary)
values (1, 4, 82403),
		(2, 4, 182101),
		(3, 6, 86038),
		(4, 1, 193199),
		(5, 4, 167749),
		(6, 5, 93032),
		(7, 5, 103546),
		(8, 4, 113753),
		(9, 3, 109307),
		(10, 3, 170923);
        
insert into application(vacancy_id, phone_number, letter,  email)
values (1, 8381319404, 'letter1', 'applicator1@mail.ru' ),
		(2, 8995433897, 'letter2', 'applicator2@mail.ru' ),
		(3, 8563408347, 'letter3', 'applicator3@mail.ru' ),
		(4, 8750082458, 'letter4', 'applicator4@mail.ru' ),
		(5, 8748268413, 'letter5', 'applicator5@mail.ru' ),
		(6, 8449060844, 'letter6', 'applicator6@mail.ru' ),
		(7, 8881264061, 'letter7', 'applicator7@mail.ru' ),
		(8, 8065355565, 'letter8', 'applicator8@mail.ru' ),
		(9, 8796947095, 'letter9', 'applicator9@mail.ru' ),
		(10, 8763009777, 'letter10', 'applicator10@mail.ru' );
        
insert into employee(position_id, phone_number, login, password)
values (1, 89297223199, 'emp1', 'pbkdf2:sha256:260000$UClwC3zTPINBHdsK$68bbadce10f9f1a1c9c1bf0d11d1f739756c05a98619e92c86879f84fa363cb0'),
		(2, 95500450124, 'emp2', 'pbkdf2:sha256:260000$NoWd2YIMbbmnF3TF$44bee57119b08507b69df952dfde6a940814026d1846ede492c3745e5407dc58'),
		(3, 93164399972, 'emp3', 'pbkdf2:sha256:260000$mN8u4CjIff0gYhaT$78e5d5c2af02c6a86794353fb600525bf16d2eadd359957bd4e7e2fd24719d80'),
		(4, 89700470320, 'emp4', 'pbkdf2:sha256:260000$Ppsa4OZ1vbwRIJzU$64208c83008865e1300b479b18178d6734406183b7877211b6201926fd6d5387'),
		(5, 96091721279, 'emp5', 'pbkdf2:sha256:260000$XLgGFZvPe0FRY525$132d3869c7954649c3f3bfd904af9250f8300205d9d67ffc025a948f0c6b7245'),
		(6, 93385455930, 'emp6', 'pbkdf2:sha256:260000$CDPrUOvRHdyMP00k$3aadee92da0a2f542b536ca93db964271807ad153d15525b1fe0e9041feebf8a'),
		(7, 95236752937, 'emp7', 'pbkdf2:sha256:260000$9KwpGzj6LZeq3Io6$eaa72eb185231952ba391f08f10381ddcea8e4dfb076d41f36bccbf21332f277'),
		(8, 96146250880, 'emp8', 'pbkdf2:sha256:260000$NwLno6QKTgdN4EYT$90535b2207fc44e117a84e62de1ef1830c7e6b91ce0dc308c661dd7b3fbb8022'),
		(9, 97020246030, 'emp9', 'pbkdf2:sha256:260000$PF0JlnNz0zVlT9nt$9067ad4105e6e05662cf764343d3a0f90014b4160372f3ff934abdfa40b02105'),
		(10, 8295162419, 'emp10', 'pbkdf2:sha256:260000$8r9tQishR0NgS6j9$4a27c9ce584828877a8fd18722bf7741fde3d067d7fd289c686c41e60aa42373');
        
insert into constituent_documents(taxpayer_identification_number)
values  (2493322460),
		(2023016000),
		(3157244264),
		(3089011021),
		(2229891811),
		(3340770128),
		(2174771888),
		(3963406694),
		(3048176289),
		(3764772514);
        
insert into client_company(constituent_documents_id, company_email)
values (1, 'company1mail.ru'),
		(2, 'company2mail.ru'),
		(3, 'company3mail.ru'),
		(4, 'company4mail.ru'),
		(5, 'company5mail.ru'),
		(6, 'company6mail.ru'),
		(7, 'company7mail.ru'),
		(8, 'company8mail.ru'),
		(9, 'company9mail.ru'),
		(10, 'company10mail.ru');
        
insert into rent_to_company(client_company_id, price_per_month)
values (1, 271162),
		(2, 254924),
		(3, 275434),
		(4, 326580),
		(5, 298783),
		(6, 299614),
		(7, 212690),
		(8, 229880),
		(9, 311939),
		(10, 323988);	

insert into rent_individual(client_id, price_per_month)
values (1, 22480),
		(2, 25558),
		(3, 37218),
		(4, 21999),
		(5, 25636),
		(6, 31537),
		(7, 28576),
		(8, 26462),
		(9, 24764),
		(10, 34158);
        
insert into sale_individual(client_id, price)
values(1, 7549134),
		(2, 5391679),
		(3, 5209222),
		(4, 5463078),
		(5, 5552385),
		(6, 6418442),
		(7, 5002916),
		(8, 5058690),
		(9, 5268586),
		(10, 7080836);
        
insert into deal(status, rent_company_id, rent_individual_id, sale_individual_id, deal_date, flat_id)
values  ('approved', null, null, 1, '2022-08-21', 1),
		('approved', null, 1, null, '2022-11-10', 2),
		('approved', 1, null, null, '2022-09-23', 3),
		('approved', null, null, 2, '2022-12-11', 4),
		('approved', null, 2, null, '2022-08-20', 5),
		('approved', 2, null, null, '2022-07-11', 6),
		('approved', null, null, 3, '2022-12-02', 7),
		('approved', null, 3, null, '2022-08-24', 8),
		('approved', 3, null, null, '2023-01-01', 9),
		('approved', null, null, 4, '2022-12-10', 10);
        
insert into feedback(deal_id, mark, feedback_message)
values(1, 4, 'great service'),
		(2, 4, 'great service'),
		(3, 3, 'normal service'),
		(4, 3, 'normal service'),
		(5, 4, 'great service'),
		(6, 3, 'normal service'),
		(7, 1, 'awful service'),
		(8, 3, 'normal service'),
		(9, 5, 'great service!!!'),
		(10, 5, 'great service!!!');
        
insert into reports(deal_id, employee_id, report_date, report_content, status)
values  (1, 1, '2022-10-17', 'con1', 'done'),
		(2, 2, '2022-12-03', 'con2', 'done'),
		(3, 3,'2022-12-07', 'con3', 'done'),
		(4, 4,'2022-10-21', 'con4', 'done'),
		(5, 5,'2022-08-22', 'con5', 'done'),
		(6, 6,'2022-03-15', 'con6', 'done'),
		(7, 7,'2022-11-12', 'con7', 'done'),
		(8, 8,'2022-05-31', 'con8', 'done'),
		(9, 9,'2022-09-11', 'con9', 'done'),
		(10, 10, '2022-05-14', 'con10', 'done');
        
insert into views(flat_id, date)
values  (1, '2022-07-16'),
		(2, '2022-10-25'),
		(3, '2022-09-04'),
		(4, '2022-05-23'),
		(5, '2022-08-08'),
		(6, '2022-06-20'),
		(7, '2022-04-28'),
		(8, '2022-09-02'),
		(9, '2022-06-30'),
		(10, '2022-04-20');