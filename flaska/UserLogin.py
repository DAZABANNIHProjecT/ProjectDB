from flask_login import UserMixin


class UserLogin(UserMixin):
    def __init__(self):
        self.__user = None

    def from_db(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user[2])

    @property
    def phone(self):
        return str(self.__user[1])

    @property
    def login(self):
        return str(self.__user[0])

    @property
    def position(self):
        return str(self.__user[5])
