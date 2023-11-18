drop database agency;
create database agency;
USE agency;


CREATE TABLE application
(
	application_id       BIGINT auto_increment primary key,
	vacancy_id           BIGINT NOT NULL,
	phone_number         CHAR(20) NOT NULL,
	email           TEXT NOT NULL
);

CREATE TABLE client
(
	client_id            BIGINT auto_increment primary key,
	phone_number         CHAR(20) NOT NULL,
	email                CHAR(18) NOT NULL
);






CREATE TABLE client_company
(
	client_company_id    BIGINT auto_increment primary key,
	company_email  TEXT NOT NULL,
	constituent_documents_id BIGINT NOT NULL
);





CREATE TABLE constituent_documents
(
	constituent_documents_id BIGINT auto_increment primary key,
	taxpayer_identification_number TEXT NOT NULL,
	memorandum_of_association_status TEXT NOT NULL
);





CREATE TABLE deal
(
	deal_id              BIGINT auto_increment primary key,
	status               TEXT NOT NULL,
	employee_id          BIGINT NOT NULL,
	rent_company_id      BIGINT,
	rent_individual_id   BIGINT,
	sale_individual_id   BIGINT,
    deal_date            DATETIME NOT NULL,
	flat_id              BIGINT NOT NULL
);




CREATE TABLE employee
(
	login            TEXT NOT NULL,
	phone_number         CHAR(20) NOT NULL,
	employee_id          BIGINT auto_increment primary key,
    password			TEXT NOT NULL,
	position_id         BIGINT NOT NULL
);





CREATE TABLE feedback
(
	mark                 INTEGER NOT NULL,
	feedback_message    TEXT NOT NULL,
	deal_id              BIGINT NOT NULL
);



ALTER TABLE feedback
ADD PRIMARY KEY (deal_id);



CREATE TABLE flat
(
	floor                INTEGER NOT NULL,
	area                 DECIMAL NOT NULL,
	rooms                INTEGER NOT NULL,
    price				 INTEGER NOT NULL,
	owner_id             BIGINT NOT NULL,
	house_id             BIGINT NOT NULL,
	photo_id             BIGINT,
	flat_id              BIGINT auto_increment primary key
);





CREATE TABLE house
(
	street               TEXT NOT NULL,
	parking              TEXT NOT NULL,
	playground           TEXT NOT NULL,
	floors_count         INTEGER NOT NULL,
	house_id             BIGINT auto_increment primary key,
    rate				 int
);



-- ALTER TABLE house ADD `house_id` INT NOT NULL AUTO_INCREMENT;
-- ALTER TABLE house
-- ADD UNIQUE (house_id);



CREATE TABLE owner
(
	owner_id             BIGINT auto_increment primary key,
	phone_number         CHAR(20) NOT NULL,
	passport_id          BIGINT NOT NULL
);





CREATE TABLE passport
(
	passport_id          BIGINT auto_increment primary key,
    number               CHAR(10) NOT NULL,
    birth_date			 DATE NOT NULL
);




CREATE TABLE photo
(
	flat_id              BIGINT,
	photo_id             BIGINT auto_increment primary key,
	link_to_photo        TEXT NOT NULL
);




CREATE TABLE positions
(
	position_name        TEXT NOT NULL,
	city TEXT NOT NULL,
	position_id         BIGINT auto_increment primary key
);




CREATE TABLE rent_individual
(
	rent_individual_id   BIGINT auto_increment primary key,
	price_per_month      NUMERIC NULL,
	client_id            BIGINT NOT NULL
);




CREATE TABLE rent_to_company
(
	rent_company_id      BIGINT auto_increment primary key,
	price_per_month                DECIMAL NOT NULL,
	client_company_id    BIGINT NOT NULL
);



CREATE TABLE reports
(
	report_date          DATETIME NOT NULL,
	status               TEXT NOT NULL,
	deal_id              BIGINT NOT NULL
);



ALTER TABLE reports
ADD PRIMARY KEY (deal_id);



CREATE TABLE sale_individual
(
	price                NUMERIC NOT NULL,
	sale_individual_id   BIGINT auto_increment primary key,
	client_id            BIGINT NOT NULL
);




CREATE TABLE transport_accessibility
(
	house_id             BIGINT NOT NULL,
	distance_underground TEXT NULL,
	distance_bus_stop    TEXT NULL
);



ALTER TABLE transport_accessibility
ADD PRIMARY KEY (house_id);



CREATE TABLE vacancy
(
	vacancy_id           BIGINT auto_increment primary key,
	expirience           int NOT NULL,
    salary				 int not null,	
	position_id         BIGINT NOT NULL
);




CREATE TABLE views
(
	client_id            BIGINT NOT NULL,
	date                 DATETIME NOT NULL,
	flat_id              BIGINT NOT NULL,
    amount 				 INT
);



ALTER TABLE views
ADD PRIMARY KEY (flat_id,client_id);



ALTER TABLE application
ADD FOREIGN KEY R_79 (vacancy_id) REFERENCES vacancy (vacancy_id);



ALTER TABLE client_company
ADD FOREIGN KEY R_54 (constituent_documents_id) REFERENCES constituent_documents (constituent_documents_id);



ALTER TABLE deal
ADD FOREIGN KEY R_56 (employee_id) REFERENCES employee (employee_id);



ALTER TABLE deal
ADD FOREIGN KEY R_80 (flat_id) REFERENCES flat (flat_id);



ALTER TABLE deal
ADD FOREIGN KEY R_44 (rent_company_id) REFERENCES rent_to_company (rent_company_id);



ALTER TABLE deal
ADD FOREIGN KEY R_45 (rent_individual_id) REFERENCES rent_individual (rent_individual_id);



ALTER TABLE deal
ADD FOREIGN KEY R_46 (sale_individual_id) REFERENCES sale_individual (sale_individual_id);



ALTER TABLE employee
ADD FOREIGN KEY R_83 (position_id) REFERENCES positions (position_id);



ALTER TABLE feedback
ADD FOREIGN KEY R_94 (deal_id) REFERENCES deal (deal_id);



ALTER TABLE flat
ADD FOREIGN KEY R_74 (owner_id) REFERENCES owner (owner_id);



ALTER TABLE flat
ADD FOREIGN KEY R_82 (house_id) REFERENCES house (house_id);



ALTER TABLE flat
ADD FOREIGN KEY R_85 (photo_id) REFERENCES photo (photo_id);



ALTER TABLE owner
ADD FOREIGN KEY R_18 (passport_id) REFERENCES passport (passport_id);



ALTER TABLE rent_individual
ADD FOREIGN KEY R_78 (client_id) REFERENCES client (client_id);



ALTER TABLE rent_to_company
ADD FOREIGN KEY R_55 (client_company_id) REFERENCES client_company (client_company_id);



ALTER TABLE reports
ADD FOREIGN KEY R_86 (deal_id) REFERENCES deal (deal_id);



ALTER TABLE sale_individual
ADD FOREIGN KEY R_77 (client_id) REFERENCES client (client_id);



ALTER TABLE transport_accessibility
ADD FOREIGN KEY R_73 (house_id) REFERENCES house (house_id);



ALTER TABLE vacancy
ADD FOREIGN KEY R_84 (position_id) REFERENCES positions (position_id);



ALTER TABLE views
ADD FOREIGN KEY R_69 (client_id) REFERENCES client (client_id);



ALTER TABLE views
ADD FOREIGN KEY R_64 (flat_id) REFERENCES flat (flat_id);


