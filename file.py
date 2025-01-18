def update_details(file_name,att,value):
    with open(file_name,"r") as rfile:
        line =rfile.readlines()
    
    with open(file_name,"w") as wfile:
        for sui in line:
            if att in sui:
                wfile.write(att+"=="+value+"\n")
            else:
                wfile.write(sui)
update_details("qwert.txt","a","50")