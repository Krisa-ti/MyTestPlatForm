# '''
# 字符串格式化   .2f 保留2位小数精度
# '''
# name = "白鲨"
# setup_year = 2006
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# total = stock_price * stock_price_daily_growth_factor ** growth_days
# message = "公司：%s,成立于：%d年,股票代码：%s,当前股价为：%.2f,每日增长系数是：%.1f,经过%d天的增长后，股价达到了%.2f" % (
#     name, setup_year, stock_code, stock_price, stock_price_daily_growth_factor, growth_days, total)
# print(message)
username= input("请输入你的用户名")
usertype= input("请输入你的类型")
print(f"你好，{username},你是尊贵的{usertype}")