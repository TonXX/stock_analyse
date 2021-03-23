# 导入tushare库
import tushare as ts
from datetime import datetime

# 设置token
ts.set_token('58416eccf52c88ff93344531998b2973ac8d3aa6180c46d6299801e1')
# 初始化pro接口
pro = ts.pro_api()


#df = pro.ths_index()
#trade_day_num = df.shape[0]


day = 20140215
while day < 20200503:
    start = day
    end = start + 105
    df = pro.ths_daily(ts_code='885497.TI', start_date=str(start), end_date=str(end), fields='close')
    trade_day_num = df.shape[0]
    mid = int(trade_day_num/2)
    print(start, "=" , df.close[0], "mid" , df.close[mid], end, "=",  df.close[trade_day_num - 2 ])
    day = day + 10000

#for idx in reversed(range(0, trade_day_num)):
#    nm = df.name[idx]
#    code = df.ts_code[idx]
#    print(nm, code)
print("aaa")