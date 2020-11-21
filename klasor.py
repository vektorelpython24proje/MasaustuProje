import os
liste = ["BERKE","SAKIR","SUDE","SEMA",\
    "FIKRIYE","IBRAHIM","ARDA","HUNKAR","OMER","BUSRA"]
for item in liste:
    os.mkdir(item)
    os.chdir(os.getcwd()+os.sep+item)
    dosya = open("ilk.py","w")
    os.chdir(r"D:\ibrahimhocaPython\MasaustuProje")
    