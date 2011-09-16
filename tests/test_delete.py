class TestDelete(TurtleTest):
    __iterations = 50000

    def test_orm_delete(self):
        from orm_tests.models import User

        self._mark_start()

        d = None
        for pk in xrange(1, self.__iterations):
            user = User.objects.get(pk = pk).delete()
            d = user.power_level

        self._mark_end()
  