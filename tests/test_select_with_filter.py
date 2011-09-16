class TestSelectWithFilter(TurtleTest):

    __iterations = 500


    def test_orm_select_with_filter(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            users = User.objects.all()[:500+pk]
            ct = bool(users)


        self._mark_end()

    def test_orm_select_with_filter3(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            users = User.objects.filter(power_level__gt=0)[:500+pk]
            ct = bool(users)


        self._mark_end()

    def test_orm_select_with_filter_q(self):
        from django.db.models import Q
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            users = User.objects.filter(Q(power_level__gt=0))[:500+pk]
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

    def test_sql_select_with_filter3(self):


        cursor = self._get_cursor()

        self._mark_start()

        d = None
        for pk in xrange(1, 20):
            cursor.execute("SELECT `orm_tests_user`.`id`, `orm_tests_user`.`name`, `orm_tests_user`.`email`, `orm_tests_user`.`age`, `orm_tests_user`.`power_level`, `orm_tests_user`.`info` FROM `orm_tests_user` WHERE `orm_tests_user`.`power_level` > 0  LIMIT %s", 500+pk)
            row = cursor.fetchone()

        d = None
        self._mark_end()

        cursor.close()
  