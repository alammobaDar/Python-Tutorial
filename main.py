import threading
import time

def lalaki ():

    time.sleep(1.5)
    print("Mababaw lang naman kaligayahan ko ehh\n")

    time.sleep(2)
    print("okay na sakin yung...\n")

    time.sleep(1.5)
    print("tipong...\n")

    time.sleep(2.3)
    print("Katulad mo..\n")

    time.sleep(3)
    print("Ou ahihi\n")

def babai():


    print("Ikaw, ano pangarap mo sa buhay??\n")



    time.sleep(9)
    print("Katulad ko??\n")
# def reverse_count():
#
#     for i in range(10,0,-1):
#         time.sleep(2)
#         print(i)

x = threading.Thread(target = babai)

y = threading.Thread(target = lalaki)
x.start()
y.start()



