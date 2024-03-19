import numpy as np
import matplotlib.pyplot as plt
from dnc import *
from bf import *

# Fungsi untuk mengecek apakah input adalah float yang valid atau tidak
def isFloat(strings):
    if(strings[0] == "-"):
        strings = strings[1:]
    if strings.replace(".", "").isnumeric():
        return True
    else:
        return False

# Input banyak titik
inputs = input("Masukkan banyak titik (minimal 3) : ")
while not inputs.isdigit() or int(inputs) < 3 :
    print("Masukan tidak valid!")
    inputs = input("Masukkan banyak titik (minimal 3) : ")

manyPoint = int(inputs)

# Input titik
points = []

for i in range(1,manyPoint+1):
    print(f"Masukkan titik ke-{i} (x y) : ", end="")
    inputs = list(map(str,input().split()))
    while len(inputs) != 2 or not isFloat(inputs[0]) or not isFloat(inputs[1]) :
        print("Masukan tidak valid!")
        print(f"Masukkan titik ke-{i} (x y) : ", end="")
        inputs = list(map(str,input().split()))
    points.append([float(inputs[0]),float(inputs[1])])

# Input banyak iterasi
inputs = input("Masukkan banyak iterasi (minimal 1) : ")
while not inputs.isdigit() or int(inputs) < 1  :
    print("Masukan tidak valid!")
    inputs = input("Masukkan banyak iterasi (minimal 1) : ")

iterasi = int(inputs)

# Memilih algoritma yang digunakan
inputs = input("Pilih algoritma yang digunakan (1. Divide and Conquer 2. Brute Force) : ")
while inputs != "1" and inputs != "2" :
    print("Masukan tidak valid!")
    inputs = input("Pilih algoritma yang digunakan (1. Divide and Conquer 2. Brute Force) : ")


if inputs == "1" :
    DNCmain(points,iterasi)
else :
    BFMain(points,iterasi)