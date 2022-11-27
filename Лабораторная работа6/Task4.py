import json

file=open('C:\\Users\\Administrator\\Desktop\\1.csv',"r",encoding='utf-8')
ls=[]
for line in file:
    line=line.replace("\n","")
    ls.append(line.split(","))
file.close()

file2=open("C:\\Users\\Administrator\\Desktop\\1.json","w",encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
json.dump(ls[1:],file2,indent=2,ensure_ascii=False)
file2.close()