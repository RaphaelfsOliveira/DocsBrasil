def valida_renavam(num_rnv):
    #print(num_rnv)
    num_rnv = str(num_rnv)
    
    if len(num_rnv) < 11:
        #print(len(num_rnv))
        num_rnv = "00" + num_rnv[:len(num_rnv)]
        #print("test_num < 11: " + num_rnv)
    
    if len(num_rnv) == 11:
        print("test_OK 11_dig: " + num_rnv)
        
    reverse_rnv = num_rnv[9::-1]
    #print("test_reversed RNV: " + reverse_rnv)
    
    soma = 0
        
    for n in range(0,8):
        #print("test_mult: ", int(reverse_rnv[n])*(n+2))
        soma += int(reverse_rnv[n])*(n+2)
        #print("soma_total: ",soma)
        
    soma += int(reverse_rnv[8])*(n+2)
    soma += int(reverse_rnv[9])*(n+2)
    #print("soma_total: ",soma)
    
    mod11 = (soma * 10) % 11
    #print("test_mod11: ",mod11)
    
    if mod11 == 10: mod11 = 0
    
    #print("test_rnv DV: ",num_rnv[10])
    #print("test_mod11_DV: ",mod11)
            
    if int(num_rnv[10]) == mod11:        
        return True
    else:
        return False
    
                
print(valida_renavam(639884962))
