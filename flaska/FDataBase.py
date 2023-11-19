import math
import mysql
import time


class FDataBase:
    def __init__(self, db) -> None:
        self.__db = db
        self.__cur = db.cursor(buffered=True)

    def get_app_pos(self):
        sql = f'''select application_id, phone_number, email, expirience, salary, position_name, city, letter from application 
                  join vacancy on application.vacancy_id = vacancy.vacancy_id
                  join positions on positions.position_id = vacancy.position_id'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except mysql.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return []

    def flat_view(self, flat_id):
        sql = f'''insert into views(flat_id, date) values({flat_id}, NOW())'''
        self.__cur.execute(sql)
        self.__db.commit()
        return True

    def get_flat_info(self, flat_id):
        sql = f'''select floor, area, rooms, price, street, 
                        parking, floors_count, distance_underground, distance_bus_stop, flat_id 
                    from flat 
                    join house on flat.house_id = house.house_id
                    join transport_accessibility on house.house_id = transport_accessibility.house_id
                    where flat_id = {flat_id};'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except mysql.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return []

    def get_table(self, table):
        sql = f'''select * from {table}'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except mysql.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return []

    def get_unapplied_deals(self):
        sql = f'''select rent_company_id, rent_individual_id,
                             sale_individual_id, deal_date, deal_id
                      from deal
                      join flat on deal.flat_id = flat.flat_id
                      join owner on owner.owner_id = flat.owner_id
                      where status = "unapproved"'''

        self.__cur.execute(sql)
        res = self.__cur.fetchall()
        if res: return res

        return []

    def add_application(self, phone_number, email, letter, vacancy_id):
        try:
            sql = "INSERT INTO application(phone_number, email,letter, vacancy_id) VALUES(%s, %s, %s, %s)"
            data = (phone_number, email, letter, vacancy_id)
            self.__cur.execute(sql, data)
            self.__db.commit()
        except:
            print("Ошибка добавления заявки, пожалуйста введите корректные данные ")
            return False
        return True

    def add_report(self, report_content, status, deal_id, employee_id):
        try:
            sql = "INSERT INTO reports(report_content, status, deal_id, employee_id, report_date) VALUES(%s, %s, %s, %s, NOW())"
            data = (report_content, status, deal_id, employee_id)
            self.__cur.execute(sql, data)
            self.__db.commit()
        except:
            print("Ошибка добавления отзыва, пожалуйста, введите корректные данные ")
            return False
        return True

    def add_rate(self, deal_id, mark, feedback_message):
        try:
            sql = "INSERT INTO feedback(deal_id, mark, feedback_message) VALUES(%s, %s, %s)"
            data = (deal_id, mark, feedback_message)
            self.__cur.execute(sql, data)
            self.__db.commit()
        except:
            print("Ошибка добавления отзыва, пожалуйста, введите корректные данные ")
            return False
        return True

    def delete_application(self, application_id):
        try:
            sql = f"DELETE FROM application where application_id = '{application_id}'"
            # data = (application_id, )
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print("Ошибка удаления")
            return False

    def approve_deal(self, deal_id):
        try:
            sql = f"UPDATE deal SET status = 'approved' where deal_id = '{deal_id}'"
            # data = (application_id, )
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print("Ошибка подтверждения сделки, пожалуйста, введите корректные данные ")
            return False

    def get_number_and_pos_id(self, application_id):
        sql = f'''select phone_number, position_id FROM application 
                    join vacancy on vacancy.vacancy_id = application.vacancy_id 
                    where application_id = {application_id} limit 1'''
        # data = (application_id, )
        self.__cur.execute(sql)
        res = self.__cur.fetchone()
        return res

    def get_vacancy_and_position(self):
        sql = f'''select * FROM positions 
                    join vacancy on positions.position_id = vacancy.position_id'''
        # data = (application_id, )
        self.__cur.execute(sql)
        res = self.__cur.fetchall()
        return res

    def add_company_deal(self, taxpayer_identification_number, contact_information, company_price, flat_id):
        try:
            sql = f"INSERT INTO constituent_documents(taxpayer_identification_number) VALUES({taxpayer_identification_number})"
            self.__cur.execute(sql)
            constituent_documents_id = self.__cur.lastrowid

            sql = "INSERT INTO client_company(constituent_documents_id, company_email) VALUES(%s, %s)"
            data = (constituent_documents_id, contact_information)
            self.__cur.execute(sql, data)
            client_company_id = self.__cur.lastrowid

            sql = "INSERT INTO rent_to_company(client_company_id, price_per_month) VALUES(%s, %s)"
            data = (client_company_id, company_price)
            self.__cur.execute(sql, data)
            rent_company_id = self.__cur.lastrowid

            sql = '''insert into deal(status, rent_company_id, rent_individual_id, sale_individual_id, deal_date, flat_id) 
                        values ('unapproved', %s, null, null, NOW(), %s)'''
            data = (rent_company_id, flat_id)
            self.__cur.execute(sql, data)
            deal_id = self.__cur.lastrowid

            self.__db.commit()
        except:
            print("Ошибка добавления сделки, пожалуйста, введите корректные данные ")
            return False

        return deal_id

    def add_client_deal(self, phone_number, email, type_of_deal, client_price, flat_id):
        try:
            sql = f"INSERT INTO client(phone_number, email) VALUES('{phone_number}', '{email}')"
            self.__cur.execute(sql)
            client_id = self.__cur.lastrowid
            print(flat_id)

            if type_of_deal == 'rent':
                sql = "INSERT INTO rent_individual(client_id, price_per_month) VALUES(%s, %s)"
                data = (client_id, client_price)
                self.__cur.execute(sql, data)
                rent_individual_id = self.__cur.lastrowid
                sql = '''insert into deal(status, rent_company_id, rent_individual_id, sale_individual_id, deal_date, flat_id) 
                            values  ('unapproved', null, %s, null, NOW(), %s)'''
                data = (rent_individual_id, flat_id)

            else:
                sql = "INSERT INTO sale_individual(client_id, price) VALUES(%s, %s)"
                data = (client_id, client_price)
                self.__cur.execute(sql, data)
                sale_individual_id = self.__cur.lastrowid
                sql = '''insert into deal(status, rent_company_id, rent_individual_id, sale_individual_id, deal_date, flat_id) 
                            values  ('unapproved', null, null, %s, NOW(), %s)'''
                data = (sale_individual_id, flat_id)

            self.__cur.execute(sql, data)
            deal_id = self.__cur.lastrowid

            self.__db.commit()
        except:
            print("Ошибка добавления сделки, пожалуйста, введите корректные данные ")
            return False
        return deal_id

    def add_flat(self, floor, area, price, rooms,
                 phone_number,
                 street, parking, playground, floors_count,
                 number, birth_date,
                 distance_underground, distance_bus_stop):
        try:
            sql = "INSERT INTO passport(number, birth_date) VALUES(%s, %s)"
            data = (number, birth_date)
            self.__cur.execute(sql, data)
            passport_id = self.__cur.lastrowid

            sql = "INSERT INTO owner(phone_number, passport_id) VALUES(%s, %s)"
            data = (phone_number, passport_id)
            self.__cur.execute(sql, data)
            owner_id = self.__cur.lastrowid

            sql = "INSERT INTO house(street, parking, playground, floors_count) VALUES(%s, %s, %s, %s)"
            data = (street, parking, playground, floors_count)
            self.__cur.execute(sql, data)
            house_id = self.__cur.lastrowid

            sql = "INSERT INTO transport_accessibility(house_id, distance_underground, distance_bus_stop) VALUES(%s, %s, %s)"
            data = (house_id, distance_underground, distance_bus_stop)
            self.__cur.execute(sql, data)

            sql = "INSERT INTO flat(house_id, owner_id, floor, area, price, rooms) VALUES(%s, %s, %s, %s, %s, %s)"
            data = (house_id, owner_id, floor, area, price, rooms)
            self.__cur.execute(sql, data)
            flat_id = self.__cur.lastrowid

            sql = f"INSERT INTO photo(flat_id, link_to_photo) values ({flat_id}, 'static/images/flat_{flat_id}/photo.jpg')"
            self.__cur.execute(sql)

            self.__db.commit()
        except:
            print("Ошибка добавления квартиры, пожалуйста, введите корректные данные ")
            return False
        return flat_id

    def register_employee(self, login, phone_number, position_id, hash_pwd):
        try:
            self.__cur.execute(f"SELECT COUNT(*) as count FROM employee WHERE login LIKE '{login}'")
            res = self.__cur.fetchone()
            if res[0] > 0:
                print("Пользователь с таким email уже существует")
                return False
            self.__cur.execute(
                "INSERT INTO employee(login, phone_number, position_id, password) VALUES(%s, %s, %s, %s)",
                (login, phone_number, position_id, hash_pwd))
            self.__db.commit()
        except:
            print("Ошибка добавления пользователя в БД ")
            return False
        return True

    def get_record(self, flat_id):
        # try:
        self.__cur.execute(f"SELECT * FROM flat WHERE flat_id = {flat_id} LIMIT 1")
        res = self.__cur.fetchone()
        if not res:
            print("Пользователь не найден")
            return False
        return res

    def get_vacancy(self, vacancy_id):
        # try:
        self.__cur.execute(f"SELECT * FROM vacancy WHERE vacancy_id = {vacancy_id} LIMIT 1")
        res = self.__cur.fetchone()
        if not res:
            print("Пользователь не найден")
            return False
        return res

    def getUserByLogin(self, login):
        try:
            self.__cur.execute(f"SELECT * FROM employee WHERE login = '{login}' LIMIT 1")
            res = self.__cur.fFetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except:
            print("Ошибка получения данных из БД ")

        return False

    def getUser(self, user_id):
        try:
            self.__cur.execute(
                f"SELECT * FROM employee JOIN positions on positions.position_id = employee.position_id WHERE employee_id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except:
            print("Ошибка получения данных из БД ")

        return False
