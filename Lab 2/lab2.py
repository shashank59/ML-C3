import numpy as np 
import pandas as pd
# Reading the data from CSV file
data = pd.read_csv('data.csv')
concepts = np.array(data.iloc[:,:-1])
print("\nInstances are:\n",concepts)
target = np.array(data.iloc[:,-1])
print("\nTarget Values are: ",target)


def train(concepts, target): 
    
    # Initializing general and specific hypothesis
    specific_h = concepts[0].copy()
    print("\nInitialization of specific hypothesis and general hypothesis")
    print("\nSpecific Boundary: ", specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    
    for i, val in enumerate(concepts):
        print("\nInstance", i+1 , "is ", val)
        #positive example
        if target[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific_h)): 
                if val[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
        #negative example           
        if target[i] == "no":             
            print("Instance is Negative ")
            for x in range(len(specific_h)): 
                if val[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                              
                else:                    
                    general_h[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
        print("Generic Boundary after ", i+1, "Instance is ", general_h)
        print("\n")

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        general_h.remove(['?', '?', '?', '?', '?', '?']) 
    
    return specific_h, general_h 
s_final, g_final = train(concepts, target)
# displaying Specific_hypothesis
print("Final Specific_h: ", s_final, sep="\n")
# displaying Generalized_Hypothesis
print("Final General_h: ", g_final, sep="\n")
