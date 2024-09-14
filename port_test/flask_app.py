from flask import Flask, request,Response
import pandas as pd
import json
app = Flask(__name__)

@app.route("/")
def demo_test():
    return "demo_test!"
@app.route("/query/<sno>")
def query_grade(sno):
    token = request.headers.get("token","")
    if not token or token != "123456":
        return "非授权访问"
    df=pd.read_csv("port_test\demo.csv",encoding="gbk")
    res=df[df["学号"]==sno]
    if len(res)==1:
        return json.dumps(res.iloc[0].to_dict(),indent=4,ensure_ascii=False)
    else:
        return "NO DATA"
@app.route("/add", methods=["POST"])
def add():
    token = request.headers.get("token","")
    if not token or token != "123456":
         return "非授权访问"
    data = json.loads(request.get_json())
    df_s=pd.read_excel("port_test\demo.xlsx")
    df=pd.DataFrame(data)
    if len(df_s[df_s["学号"]]==df["学号"])>0:
        return "该学号已存在"
    pd.concat([df_s,df]).to_excel("port_test\demo.xlsx",index=False)
    return "OK"
if __name__ == "__main__":
    app.run()