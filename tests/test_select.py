class TestSelect(TurtleTest):

    __iterations = 50000

    def test_orm_select(self):
        from orm_tests.models import *

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.get(pk=pk)
            d = user.power_level

        self._mark_end()

    def test_sql_select(self):
        from orm_tests.models import *

        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            cursor.execute("SELECT `orm_tests_user`.`id`, `orm_tests_user`." \
                            "`name`, `orm_tests_user`.`email`," \
                            " `orm_tests_user`.`age`, `orm_tests_user`." \
                            "`power_level`, `orm_tests_user`.`info` FROM " \
                            "`orm_tests_user` WHERE `orm_tests_user`." \
                            "`id` = %(pk)s", {'pk': pk})
            row = cursor.fetchone()
            d = row[4]
        d = None

        self._mark_end()
  