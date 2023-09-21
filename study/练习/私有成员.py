class Phone:
    __is_5g_enable = True

    def __check_5g(self,__is_5g_enable):
        if __is_5g_enable  == True:
            print("5G 开启")
        else:
            print("5G关闭，使用4g网络")

    def call_by_5g(self,__is_5g_enable):
        self.__check_5g(__is_5g_enable)
        print("正在通话中")


phone = Phone()

phone.call_by_5g(False)