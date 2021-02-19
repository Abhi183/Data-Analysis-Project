from ckd_ver2 import Chronic_Kidney_Disease

def open_file(): # function to open file 
        
    fp = None    
    while not fp:  # While the file is not loaded (or we haven't tried)
        try:       # Try to load it
            fp = open('chronic_kidney_disease.txt')
        except FileNotFoundError:  
            print("file not found")           
    else: return fp      # When you got the fp(), return it
    pass

def read_values(fp):
    
   
    line = fp.read().split('\n')
    
    
    return line

def write_data(a):
    #write into the file 
    file = open("CKD.txt_ver2",'w')
    data = "chronic_kidney_disease.\n"
    data = data + "{:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s} {:<5s}{:<5s}{:<5s}{:>5s}".format("Age","BP","SG"," Alb", "Sug","RBC"," PC","PC- Clumps","Bac","BG","BU","SC","Na","Po","HGB","PCV","WBCCount","RBCCount","Hyp","DM","CAD","App","PE","An","Class\n")
   
    for i in range(len(a)-3):
       
        
        temp = Chronic_Kidney_Disease(a[i])
        
        
        
        data = data + "{:<4s}{:<4s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:>5s}".format(temp.get_age(),temp.get_BloodPressure(),temp.get_SpecificGravity(),temp.get_Albumin(),temp.get_sugar(),temp.get_RedBloodCells(),temp.get_PussCell(),temp.get_PussCellClumps(),temp.get_Bacteria(),temp.get_BloodGlucose(),temp.get_BloodUrea(),temp.get_SerumCreatinine(),temp.get_Sodium(),temp.get_Potassium(),temp.get_Hemoglobin(),temp.get_PackedCellVolume(),temp.get_WhiteBloodCellCount(),temp.get_RedBloodCellCount(),temp.get_Hypertension(),temp.get_DiabetesMellitus(),temp.get_CoronaryArteryDisease(),temp.get_Appetite(),temp.get_PedalEdema(),temp.get_Anemia(),temp.get_Class())
      
    file.write(data)
    file.close

# this part is the main method
def main():
    fp = open_file()
    data = read_values(fp)
    print(data)
    write_data(data)
    fp.close

if __name__ == "__main__":
    main()
    
  
