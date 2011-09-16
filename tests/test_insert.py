class TestInsert(TurtleTest):

    __iterations = 1000

    def __init__(self):
        pass

    def __save(self, userdata):

        from orm_tests.models import *

        for entry in userdata:
            User(**entry).save()
        #transaction.commit()

    def _gen_data(self):
        userdata = list()
        for i in range(self.__iterations):
            userdata.append({'name': r(20), 'email': r(20), \
                             'age': random.randint(10, 80), \
                             'power_level': random.randint(-100, 100), \
                             'info': r(400)})
        return userdata

    def test_orm_insert(self):

        self.pipe_print("Init")

        userdata = self._gen_data()

        self._mark_start()
        self.__save(userdata)
        self._mark_end()

    def test_sql_insert(self):
        self.pipe_print("Init")

        userdata = self._gen_data()
        cursor = self._get_cursor()

        self._mark_start()

        for entry in userdata:
            cursor.execute("INSERT INTO `orm_tests_user`" \
                           " (`name`, `email`, `age`, `power_level`, `info`) "\
                           "VALUES (%(name)s, %(email)s, %(age)s, " \
                           "%(power_level)s, %(info)s)", entry)

        self._mark_end()

        cursor.close()
  