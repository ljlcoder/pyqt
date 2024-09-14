import baostock as bs
import pandas as pd


def get_data():
    # 登陆系统
    """
    :return: None
    :rtype: None

    login system of baostock, get all stocks in hs300 index, and print to console
    and save to csv file named `hs300_stocks.csv` in disk D.

    1. login system
    2. get all stocks in hs300 index
    3. print to console
    4. save to csv file
    5. logout system
    """
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取沪深300成分股
    rs = bs.query_hs300_stocks()
    print('query_hs300 error_code:'+rs.error_code)
    print('query_hs300  error_msg:'+rs.error_msg)

    # 打印结果集
    hs300_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        hs300_stocks.append(rs.get_row_data())
    result = pd.DataFrame(hs300_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    # result.to_csv("./hs300_stocks.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

def get_single_data(code,start_state,end_state):
    lg = bs.login()
    rs=bs.query_history_k_data_plus(code,"date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",frequency="d",adjustflag="3",start_date=start_state,end_date=end_state)
    # 打印结果集
    hs300_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        hs300_stocks.append(rs.get_row_data())
    result = pd.DataFrame(hs300_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    # result.to_csv("./hs300_stocks.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

if __name__ == '__main__':
    get_single_data("sh.600000","2018-01-01","2020-01-01")