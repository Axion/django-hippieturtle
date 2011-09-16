class TestSelectOneField(TurtleTest):


    __iterations = 5000

    def test_orm_select(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.only("power_level").get(pk = pk)
            d = user.power_level

        self._mark_end()

    def test_sql_select_onefield(self):
        from orm_tests.models import User

        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            cursor.execute("SELECT `orm_tests_user`.`power_level` FROM `orm_tests_user` WHERE `orm_tests_user`.`id` = %(pk)s", {'pk' : pk})
            row = cursor.fetchone()
            d = row[0]

        d = None

        cursor.close()

        self._mark_end()


    def test_sql_select_twofields_pk(self):

        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            cursor.execute("SELECT `orm_tests_user`.`name`,`orm_tests_user`.`power_level` FROM `orm_tests_user` WHERE `orm_tests_user`.`id` = %(pk)s", {'pk' : pk})
            row = cursor.fetchone()
            d = row[1]
        d = None

        cursor.close()

        self._mark_end()

    def test_sql_select_onefield_pk(self):

        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            cursor.execute("SELECT `orm_tests_user`.`id`,`orm_tests_user`.`power_level` FROM `orm_tests_user` WHERE `orm_tests_user`.`id` = %(pk)s", {'pk' : pk})
            row = cursor.fetchone()
            d = row[1]
        d = None

        cursor.close()

        self._mark_end()

    def test_sql_select_all(self):
        from orm_tests.models import User

        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            cursor.execute("SELECT `orm_tests_user`.`id`, `orm_tests_user`.`name`, `orm_tests_user`.`email`, `orm_tests_user`.`age`, `orm_tests_user`.`power_level`, `orm_tests_user`.`info` FROM `orm_tests_user` WHERE `orm_tests_user`.`id` = %(pk)s", {'pk' : pk})
            row = cursor.fetchone()
            d = row[4]
        d = None

        cursor.close()

        self._mark_end()


    def test_orm_defer(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.defer("name","email","age","info").get(pk = pk)
            d = user.power_level

        self._mark_end()

    def test_orm_values(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.values("power_level").get(pk = pk)
            d = user['power_level']

        self._mark_end()

    def test_orm_only(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.only("power_level").get(pk = pk)
            d = user.power_level

        self._mark_end()




