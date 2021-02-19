
class Chronic_Kidney_Disease:
    def __init__(self,data):
         count = data.split(',')
         self.age= count[0]
         self.BloodPressure= count[1]
         self.SpecificGravity= count[2]
         self.Albumin = count[3]
         self.sugar = count[4]
         self.RedBloodCells=count[5]
         self.PussCell= count[6]
         self.PussCellClumps = count[7]
         self.Bacteria= count[8]
         self.BloodGlucose =count[9]
         self.BloodUrea=count[10]
         self.SerumCreatinine =count[11]
         self.Sodium =count[12]
         self.Potassium =count[13]
         self.Hemoglobin =count[14]
         self.PackedCellVolume=count[15]
         self.WhiteBloodCellCount=count[16]
         self.RedBloodCellCount =count[17]
         self.Hypertension=count[18]
         self.DiabetesMellitus=count[19]
         self.CoronaryArteryDisease =count[20]
         self.Appetite=count[21]
         self.PedalEdema=count[22]
         self.Anemia=count[23]
         self.Class=count[24]
         
    def get_age(self):    return self.age
    def get_BloodPressure(self):    return self.BloodPressure
    def get_SpecificGravity(self):    return self.SpecificGravity
    def get_Albumin(self):    return self.Albumin
    def get_sugar(self):    return self.sugar
    def get_RedBloodCells(self):    return self.RedBloodCells
    def get_PussCell(self):    return self.PussCell
    def get_PussCellClumps(self):    return self.PussCellClumps
    def get_Bacteria(self):    return self.Bacteria
    def get_BloodGlucose(self):    return self.BloodGlucose
    def get_BloodUrea(self):    return self.BloodUrea
    def get_SerumCreatinine(self):    return self.SerumCreatinine    
    def get_Sodium(self):    return self.Sodium
    def get_Potassium(self):    return self.Potassium
    def get_Hemoglobin(self):    return self.Hemoglobin
    def get_PackedCellVolume(self):    return self.PackedCellVolume
    def get_WhiteBloodCellCount(self):    return self.WhiteBloodCellCount
    def get_RedBloodCellCount(self):    return self.RedBloodCellCount
    def get_Hypertension(self):    return self.Hypertension
    def get_DiabetesMellitus(self):    return self.DiabetesMellitus
    def get_CoronaryArteryDisease(self):    return self.CoronaryArteryDisease
    def get_Appetite(self):    return self.Appetite
    def get_PedalEdema(self):    return self.PedalEdema    
    def get_Anemia(self):    return self.Anemia
    def get_Class(self):    return self.Class
    
    
    
    
         
    def print(self):
        print(self.age,self.BloodPressure, self.SpecificGravity,self.Albumin,self.sugar, self.RedBloodCells,self.PussCell, self.PussCellClumps,self.Bacteria,self.BloodGlucose, self.BloodUrea, self.SerumCreatinine, self.Sodium, self.Potassium, self.Hemoglobin, self.PackedCellVolume, self.WhiteBloodCellCount,self.RedBloodCellCount,self.Hypertension,self.DiabetesMellitus,self.CoronaryArteryDisease, self.Appetite,self.PedalEdema,self.Anemia,self.Class)
              
              
              
             
a=open('chronic_kidney_disease.txt','r')
b=a.readline()
c=Chronic_Kidney_Disease(b)
c.print()
print(c.get_age())

              
             
  
