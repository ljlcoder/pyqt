import pandas as pd
import os



def merge_excel(excel_paths,save_dir):
    """
    合并excel
    """
    df_lists=[]
    for excel_path in excel_paths:
        if not os.path.exists(excel_path):
            continue
        df_lists.append(pd.read_excel(excel_path))
    df_all=pd.concat(df_lists)
    df_all.to_excel(save_dir,index=False)
if __name__ == "__main__":
    merge_excel(r"H:\python\pyqt\excel\ouput\*.xlsx","./output.xlsx")