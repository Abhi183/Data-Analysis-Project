def open_file(): # function to open file 
        
    fp = None    
    while not fp:  # While the file is not loaded (or we haven't tried)
        try:       # Try to load it
            fp = open('chronic_kidney_disease.txt')
        except FileNotFoundError:  
            print("file not found")           
    else: return fp      # When you got the fp, return it
    pass

def read_values(fp): 
    list=[]
    fp.seek(0)
    line = fp.readline()
    list.append(line.split(','))
    for line in fp:
        list.append(line.split(','))
    return list

def write_data(list):
    #write into the file 
    file = open("Arranged_CKD.txt",'w')
    data = "chronic_kidney_disease.\n"
    data = data + "{:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s}{:<5s}{:<5s}{:>5s}".format("Age","BP","SG"," Alb", "Sug","RBC"," PC","PC- Clumps","Bac","BG","BU","SC","Na","Po","HGB","PCV","WBCCount","RBCCount","Hyp","DM","CAD","App","PE","An","Class\n")
   
    for i in range(len(list)-2):
        
        data = data +"{:<4s}{:<4s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:>5s}".format(list[i][0],list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6],list[i][7],list[i][8],list[i][9],list[i][10],list[i][11],list[i][12],list[i][13],list[i][14],list[i][15],list[i][16],list[i][17],list[i][18],list[i][19],list[i][20],list[i][21],list[i][22],list[i][23],list[i][24])
      
    file.write(data)
    file.close

# this part is the main method
def main():
    fp = open_file()
    list = read_values(fp)
    print(list)
    write_data(list)
    fp.close

if __name__ == "__main__":
    main()
    
 
