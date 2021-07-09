from django.test import TestCase
from myapp.models import MyModel


class MyTest(TestCase):
    def test_db(self):
        model = MyModel.objects.create(name="test")
        assert MyModel.objects.filter(name="test").count() == 1
        assert MyModel.objects.filter(name="abcde").count() == 0

    def test_view(self):
        response = self.client.get("/hello/")
        assert response.status_code == 200
        assert response.json() == {"msg" : "hello"}
