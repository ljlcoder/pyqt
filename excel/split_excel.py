import pandas as pd


def split_excel(path,split_col,save_path):
    """
    :param path: 文件路径
    :param split_col: 列名
    :param save_path: 保存路径
    :return:
    """
    df = pd.read_excel(path)
    unique_values=df[split_col].unique()
    for unique_value in unique_values:
        df_single=df[df[split_col]==unique_value]
        df_single.to_excel(f"{save_path}/拆分后-{unique_value}.xlsx",index=False)



if __name__ == '__main__':
    split_excel(path="excel/订单数据表.xlsx",split_col="产品名称",save_path="excel/ouput")