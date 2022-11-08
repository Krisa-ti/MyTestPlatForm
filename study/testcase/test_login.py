import  pytest
import  requests
from jsonpath import jsonpath


class TestLogin:

    def test_03_login(self):
        print("输出登录3")

    @pytest.mark.run(order=1)
    @pytest.mark.skip(reason="试试")
    def test_01_login(self):
        print("输出登录1")
#  -s 输出调试信息
#  -v 类名+方法名


