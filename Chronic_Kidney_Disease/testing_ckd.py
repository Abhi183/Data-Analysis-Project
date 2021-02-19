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
    while fp != (None):
        v=fp.readline().split(',')
    

        
    return v

def write_data(data):
    file = open('random.txt','w')
    for i in range(len(v)-1):
        test=Chronic_Kidney_Disease(v[i])
        




      
    file.write(test)
    file.close

# this part is the main method
def main():
    fp = open_file()
    a = read_values(fp)
    print(a)
    write_data(a)
    fp.close

if __name__ == "__main__":
    main()
    
  
