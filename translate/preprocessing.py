import pickle


with open("H:\python\pyqt\\translate\\text.txt","r",encoding="utf-8") as f:
    data = f.readlines()
#大数据pickle才会有显著的性能提升
with open("./traslate/train.pkl","wb") as f:
    pickle.dump(data,f)