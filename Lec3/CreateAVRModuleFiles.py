ModuleName = input("Enter Module Name : ")

f1 = open(ModuleName+"_interface.h" , "x")  #create Interface H File
f2 = open(ModuleName+"_config.h" , "x")     #create Configuration H File
f3 = open(ModuleName+"_private.h" , "x")    #create Private H File
f4 = open(ModuleName+"_Program.c" , "x")    #create Program C File

f1 = open(ModuleName+"_interface.h" , "a+") #Open Interface H File to read it and append data
f2 = open(ModuleName+"_config.h" , "a+")    #Open Configuration H File to read it and append data
f3 = open(ModuleName+"_private.h" , "a+")   #Open private H File to read it and append data
f4 = open(ModuleName+"_Program.c" , "a+")   #Open Program C File to read it and append data

#Writting Header Guard to the Interface H File
f1.write("#ifndef "+ModuleName+"_INTERFACE_H_\n")
f1.write("#define "+ModuleName+"_INTERFACE_H_")
f1.write("\n\n\n\n\n")
f1.write("#endif /* "+ModuleName+"_INTERFACE_H_ */")

#Writting Header Guard to the Configuration H File
f2.write("#ifndef "+ModuleName+"_CONFIGURATION_H_\n")
f2.write("#define "+ModuleName+"_CONFIGURATION_H_")
f2.write("\n\n\n\n\n")
f2.write("#endif /* "+ModuleName+"_CONFIGURATION_H_ */")

#Writting Header Guard to the private H File
f3.write("#ifndef "+ModuleName+"_PRIVATE_H_\n")
f3.write("#define "+ModuleName+"_PRIVATE_H_")
f3.write("\n\n\n\n\n")
f3.write("#endif /* "+ModuleName+"_PRIVATE_H_ */")

f1 = open(ModuleName+"_interface.h" , "r") #open Interface H File to read it and append string(s)
f2 = open(ModuleName+"_config.h" , "r")    #open Configuration H File to read it and append string(s)
f3 = open(ModuleName+"_private.h" , "r")   #open private H File to read it and append string(s)
f4 = open(ModuleName+"_program.c" , "r")   #open Program C File to read it and append string(s)

f1.close()              #open Interface H File
f2.close()              #open Configuration H File
f3.close()              #open private H File
f4.close()              #open Program C File