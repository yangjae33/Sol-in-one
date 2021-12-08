import pandas as pd

filename = 'operating-system-8.txt'
qfilename = "q_"+filename
afilename = "a_"+filename

prefix1 = " <category>\n    <pattern>"
question = ""
prefix2 = "</pattern>\n <template>"
answer = ""
suffix1 = "</template>\n </category>\n"
#content = prefix1+question+prefix2+answer+suffix1

with open('./os_qna/'+qfilename,'r',encoding='UTF-8') as file:
    qcontent = list()

    while True:
        sentence = file.readline()
        if sentence:
            qcontent.append(sentence)
        else:
            break
        
with open('./os_qna/'+afilename,'r',encoding='UTF-8') as file:
    acontent = list()

    while True:
        sentence = file.readline()
        if sentence:
            acontent.append(sentence)
        else:
            break
content = list()
for k in range(0,len(qcontent)-1):
    #print(qcontent[k].split('/')[0])
    content.append(prefix1+qcontent[k].split('/')[0]+prefix2+acontent[k].split('/')[0]+suffix1)
    
print(content)
"""
reader = inputtxt.readline()
content = reader.split("/")[0]
"""
f=open('./os_aiml/'+filename,'w',newline='')
#wr = csv.writer(f)

for line in content:
    f.write(line)    
f.close()