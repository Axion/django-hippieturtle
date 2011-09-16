class TestSelectOneQuery(TurtleTest):

    __iterations = 5000

    def test_orm_select_onequery(self):
        from orm_tests.models import *

        self._mark_start()

        d = None
        users = User.objects.all()[:self.__iterations]
        for user in users.iterator():
            d = user.power_level
        d = None

        self._mark_end()

    def test_orm_select_onequery_noiterations(self):
        from orm_tests.models import *
        self._mark_start()

        d = None
        users = User.objects.all()[:self.__iterations]
        for user in users:
            d = user.power_level
        d = None

        self._mark_end()

    def test_sql_select_onequery(self):


        cursor = self._get_cursor()

        self._mark_start()

        d = None
        cursor.execute ("SELECT `orm_tests_user`.`id`, `orm_tests_user`.`name`, `orm_tests_user`.`email`, `orm_tests_user`.`age`, `orm_tests_user`.`power_level`, `orm_tests_user`.`info` FROM `orm_tests_user` LIMIT %s", self.__iterations)
        result_set = cursor.fetchall ()
        for row in result_set:
            d = row[4]
            print d
        d = None
        cursor.close()

        self._mark_end()



  