import  pytest
import  requests
from jsonpath import jsonpath


class TestApi:

    def setup_method(self):
        print("在执行用例之前进行初始化")
    def teardown_method(self):
        print("在执行用例之后结束")
    def setup_class(self):
        print("开始时只执行一次")
    def teardown_class(self):
        print("结尾时只执行一次")

    def test_01_api(self):
        print("输出成功01")

    def test_02_api(self):
        print("输出成功02")
#  -s 表示输出调试信息，包括print打印的信息
#  -v  显示更详细的信息
#  -vs 这2个参数一起用
#  -n  分布式运行测试用例
#  --reruns=num  失败用例重跑几次
#  -- maxfail =num  出现几次失败就停止
#  -k 根据测试用例的部分字符串指定测试用例
#  -v 类名+方法名


