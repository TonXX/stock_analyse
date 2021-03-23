# 导入tushare库
import tushare as ts
from datetime import datetime

# 设置token
ts.set_token('58416eccf52c88ff93344531998b2973ac8d3aa6180c46d6299801e1')
# 初始化pro接口
pro = ts.pro_api()
# 获取日线数据
dayofWeek = datetime.strptime("20210211", "%Y%m%d").weekday()
print(dayofWeek)
df = pro.index_daily(ts_code='000001.SH', start_date='20000311', end_date='20210311')
print(df.head().pct_chg[0])
trade_day_num = df.shape[0]
yestday_close=0
yestday_chg=0
up = 0
down = 0
green = 0
red = 0
for idx in reversed(range(0, trade_day_num)):
    day = df.trade_date[idx]
    dayofWeek = datetime.strptime(str(day), "%Y%m%d").weekday()

    if dayofWeek in (1, 2, 3, 4, 5):
        if yestday_chg > 2 and df.pct_chg[idx] > 0:
            up = up + 1
            print("周", dayofWeek + 1)
            print(df.trade_date[idx])
            print("涨跌幅", df.pct_chg[idx])
            print("开盘价", df.open[idx])
            print("昨日收盘价", yestday_close)
            print("收盘价", df.close[idx])
            if df.close[idx] > df.open[idx]:
                red = red + 1
            else:
                green = green + 1
            print("-----------------")
        if yestday_chg > 2 and df.pct_chg[idx] < 0:
            down = down + 1
            print("周", dayofWeek + 1)
            print(df.trade_date[idx])
            print("涨跌幅", df.pct_chg[idx])
            print("开盘价", df.open[idx])
            print("昨日收盘价", yestday_close)
            print("收盘价", df.close[idx])
            if df.close[idx] > df.open[idx]:
                red = red + 1
            else:
                green = green + 1
            print("-----------------")
    yestday_close = df.close[idx]
    yestday_chg = df.pct_chg[idx]

print("涨", up, "跌", down, "阳线", red, "阴线", green)

