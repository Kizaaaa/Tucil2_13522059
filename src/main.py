import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk mengecek apakah input adalah float yang valid atau tidak
def isFloat(strings):
    if(strings[0] == "-"):
        strings = strings[1:]
    if strings.replace(".", "").isnumeric():
        return True
    else:
        return False

# Fungsi untuk mendapatkan titik tengah dari 2 titik
def getMiddle(x1,x2,y1,y2):
    return (x1+x2)/2,(y1+y2)/2

# Fungsi Divide and Conquer
def divideAndConquer():
    pass

# Input banyak titik
inputs = input("Masukkan banyak titik (minimal 3) : ")
while not inputs.isdigit() or int(inputs) < 3 :
    print("Masukan tidak valid!")
    inputs = input("Masukkan banyak titik (minimal 3) : ")

points = int(inputs)

# Input titik
xArray = []
yArray = []

for i in range(1,points+1):
    print(f"Masukkan titik ke-{i} (x y) : ", end="")
    inputs = list(map(str,input().split()))
    while len(inputs) != 2 or not isFloat(inputs[0]) or not isFloat(inputs[1]) :
        print("Masukan tidak valid!")
        print(f"Masukkan titik ke-{i} (x y) : ", end="")
        inputs = list(map(str,input().split()))
    xArray.append(float(inputs[0]))
    yArray.append(float(inputs[1]))

# Input banyak iterasi

inputs = input("Masukkan banyak iterasi (minimal 1) : ")
while not inputs.isdigit() or int(inputs) < 1  :
    print("Masukan tidak valid!")
    inputs = input("Masukkan banyak iterasi (minimal 1) : ")

points = int(inputs)



# xPoints = np.array(xArray)
# yPoints = np.array(yArray)

# plt.plot(xPoints, yPoints)
# plt.show()