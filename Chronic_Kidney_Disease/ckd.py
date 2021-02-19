class Chronic_Kidney_Disease:
    def __init__(self,ag=0,bp=0,sg=0.0,alb=0.0,sugar=0,rbc='',pc='',pcc='',bac='',bg=0,bu=0,sc=0,na=0,k=0,hg=0,pcv=0,wbcc=0,rbcc=0,hyp='',dm='',cad='',apt='',pe='',anm='',c=''):
         self.age=ag
         self.blood_pressure=bp
         self.specific_gravity=sg
         self.albumin = alb
         self.sugar = sugar
         self.red_blood_cells=rbc
         self.pus_cell=pc
         self.pus_cell_clumps =pcc
         self.bacteria= bac
         self.blood_glucose_random =bg
         self.blood_urea=bu
         self.serum_creatinine =sc
         self.sodium =na
         self.potassium =k
         self.hemoglobin =hg
         self.packed_cell_volume=pcv
         self.white_blood_cell_count=wbcc
         self.red_blood_cell_count =rbcc
         self.hypertension=hyp
         self.diabetes_mellitus=dm
         self.coronary_artery_disease =cad
         self.appetite=apt
         self.pedal_edema=pe
         self.anemia=anm
         self.Class=c
         
    def get_age(self):
        return self.age
    def get_blood_pressure(self):
        return self.blood_pressure
    def get_specific_gravity(self):
        return self.specific_gravity
    def get_albumin(self):
        return self.albumin
    def get_sugar(self):
        return self.sugar
    def get_red_blood_cells(self):
        return self.red_blood_cells
    def get_pus_cell(self):
        return self.pus_cell
    def get_pus_cell_clumps(self):
        return self.pus_cell_clumps
    def get_bacteria(self):
        return self.bacteria
    def get_blood_glucose_random(self):
        return self.blood_glucose_random
    def get_blood_urea(self):
        return self.blood_urea
    def get_serum_creatinine(self):
        return self.serum_creatinine
    def get_sodium(self):
        return self.sodium
    def get_potassium(self):
        return self.potassium
    def get_hemoglobin(self):
        return self.hemoglobin
    def get_packed_cell_volume(self):
        return self.packed_cell_volume
    def get_white_blood_cell_count(self):
        return self.white_blood_cell_count
    def get_red_blood_cell_count(self):
        return self.red_blood_cell_count
    def get_hypertension(self):
        return self.hypertension
    def get_diabetes_mellitus(self):
        return self.diabetes_mellitus
    def get_coronary_artery_disease(self):
        return self.coronary_artery_disease
    def get_appetite(self):
        return self.appetite
    def get_pedal_edema(self):
        return self.pedal_edema
    def get_anemia(self):
        return self.anemia
    def get_Class(self):
        return self.Class

    def set_age(self, age):
        self.age = age
    def set_blood_pressure(self, bp):
        self.blood_pressure = bp
    def set_specific_gravity(self, sg):
        self.specific_gravity = sg
    def set_albumin(self, al):
        self.albumin = al
    def set_sugar(self, su):
        self.sugar = su
    def set_red_blood_cells(self, rbc):
        self.red_blood_cells = rbc
    def set_pus_cell(self, pc):
        self.pus_cell = pc
    def set_pus_cell_clumps(self, pcc):
        self.pus_cell_clumps = pcc
    def set_bacteria(self, ba):
        self.bacteria = ba
    def set_blood_glucose_random(self, bgr):
        self.blood_glucose_random = bgr
    def set_blood_urea(self, bu):
        self.blood_urea = bu
    def set_serum_creatinine(self, sc):
        self.serum_creatinine = sc
    def set_sodium(self, sod):
        self.sodium = sod
    def set_potassium(self, pot):
        self.potassium = pot
    def set_hemoglobin(self, hemo):
        self.hemoglobin = hemo
    def set_packed_cell_volume(self, pcv):
        self.packed_cell_volume = pcv
    def set_white_blood_cell_count(self, wc):
        self.white_blood_cell_count = wc
    def set_red_blood_cell_count(self, rc):
        self.red_blood_cell_count = rc
    def set_hypertension(self, htn):
        self.hypertension = htn
    def set_diabetes_mellitus(self, dm):
        self.diabetes_mellitus = dm
    def set_coronary_artery_disease(self, cad):
        self.coronary_artery_disease = cad
    def set_appetite(self, appet):
        self.appetite = appet
    def set_pedal_edema(self, pe):
        self.pedal_edema = pe
    def set_anemia(self, ane):
        self.anemia = ane
    def set_Class(self, Class):
        self.category = Class
         
    def print(self):
        print('Age:{}\nBlood Pressure:{}\nSpecific Gravity:{}\nAlbumin::{}\nSugar:{}\nRed Blood Cells:{}\npus_cell:{}\nPus Cell Clumps:{}\nbacteria:{}\nblood_glucose:{}\nBlood Urea:{}\nSerum Creatinine:{}\nsodium:{}\npotassium:{}\nhemoglobin:{}\nPacked CellVolume:{}\nWhite Blood CellCount:{}\nRed Blood Cell Count:{}\nhypertension:{}\nDiabetes Mellitus:{}\nCoronary Artery Disease:{}\nappetite:{}\nPedal Edema:{}\nanemia:{}\nClass:{}'.format(self.age,self.blood_pressure, self.specific_gravity,self.albumin,self.sugar, self.red_blood_cells,self.pus_cell, self.pus_cell_clumps,self.bacteria,self.blood_glucose_random, self.blood_urea, self.serum_creatinine, self.sodium, self.potassium, self.hemoglobin, self.packed_cell_volume, self.white_blood_cell_count,self.red_blood_cell_count,self.hypertension,self.diabetes_mellitus,self.coronary_artery_disease, self.appetite,self.pedal_edema,self.anemia,self.Class))
             
             
             
a=open('chronic_kidney_disease.txt','r')
a.seek(0)

d = {'ag':0,'bp':0,'sg':0.0,'alb':0.0,"sugar":0,'rbc':'','pc':'','pcc':'','bac':'','bg':0,'bu':0,'sc':0,'na':0,'k':0,'hg':0,'pcv':0,'wbcc':0,'rbcc':0,'hyp':'','dm':'','cad':'','apt':'','pe':'','anm':'','c':''}
c=1
while a != (None):
    
    c=c+1
    v=a.readline().split(',')
    
    print(v)
    count = 0
    for k in d.keys():
        d[k]=v[count] 
        count = count + 1
        
   
 
    test=Chronic_Kidney_Disease(**d)
    test.print()

         
