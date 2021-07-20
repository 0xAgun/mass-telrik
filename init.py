import os
import sys
print('''
  
                                                                                  
                                      ,--.         ,--.              ,--.,--.     
,--,--,--. ,--,--. ,---.  ,---.     ,-'  '-. ,---. |  | ,---. ,--.--.`--'|  |,-.  
|        |' ,-.  |(  .-' (  .-'     '-.  .-'| .-. :|  || .-. :|  .--',--.|     /  
|  |  |  |\ '-'  |.-'  `).-'  `)      |  |  \   --.|  |\   --.|  |   |  ||  \  \  
`--`--`--' `--`--'`----' `----'       `--'   `----'`--' `----'`--'   `--'`--'`--' 
                                
                                modified by 0xAgun
                                

''')

print('''

1. scan site for vulnerability
2. mass exploit telerik
''')

input_chosse = str(input("root@nsbh: "))
wlist = str(input("enter you site list: "))

if input_chosse == '1':
    os.system("scanner.py " + wlist+ " 10")
    print("")
elif input_chosse == '2':
    os.system("mass.py " + wlist+ " 10")
    print("")
else:
    print("unknown command")

    
    