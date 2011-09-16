class TestCacheBug(TurtleTest):

    __iterations = 500


    def test_orm_select_with_filter(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            users = User.objects.all()[:500+pk]
            ct = bool(users)


        self._mark_end()

    def test_orm_select_with_filter2(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            users = User.objects.all()[:500]
            ct = bool(users)


        self._mark_end()

    def test_sql_select_with_filter(self):


        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            cursor.execute("SELECT `orm_tests_user`.`id`, `orm_tests_user`.`name`, `orm_tests_user`.`email`, `orm_tests_user`.`age`, `orm_tests_user`.`power_level`, `orm_tests_user`.`info` FROM `orm_tests_user` LIMIT %s", 500+pk)
            row = cursor.fetchone()

        d = None
        self._mark_end()

        cursor.close()

    def test_sql_select_with_filter2(self):


        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            cursor.execute("SELECT `orm_tests_user`.`id`, `orm_tests_user`.`name`, `orm_tests_user`.`email`, `orm_tests_user`.`age`, `orm_tests_user`.`power_level`, `orm_tests_user`.`info` FROM `orm_tests_user` LIMIT %s", 500)
            row = cursor.fetchone()

        d = None
        self._mark_end()

        cursor.close()


  