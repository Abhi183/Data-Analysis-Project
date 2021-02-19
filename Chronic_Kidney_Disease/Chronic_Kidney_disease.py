text = open('chronic_kidney_disease.txt')

line = text.read()
list = line.split('\n')
new_list=[]
for i in range(len(list)):
    new_list.append(list[i].split(','))
    

file = open("Arranged_CKD.txt",'w')
data = "Chronic Kidney Disease .\n"
data = data + "{:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s}{:<5s}{:<5s}{:>5s}".format("Age","BP","SG"," Alb", "Sug","RBC"," PC","PC Clumps","Bac","BG","BU","SC","Na","Po","HGB","PCV","WBCCount","RBCCount","Hyp","DM","CAD","App","PE","An","Class" "\n")
for n in range(len(new_list)):
    data =data + "{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:>5s}".format(list[n][0],list[n][1],list[n][2],list[n][3],list[n][4],list[n][5],list[n][6],list[n][7],list[n][8],list[n][9],list[n][10],list[n][11],list[n][12],list[n][13],list[n][14],list[n][15],list[n][16],list[n][17],list[n][18],list[n][19],list[n][20],list[n][21],list[n][22],list[n][23],list[n][24])
file.write(data)
file.close


