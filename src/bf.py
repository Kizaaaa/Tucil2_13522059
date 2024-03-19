import matplotlib.pyplot as plt
import math
import time

# Fungsi Brute Force
def BruteForce(points,iterate):
    ret = []
    t = 1 / (iterate*1.0 + 1)
    for i in range(iterate+2):
        x = 0.0
        y = 0.0
        for j in range(len(points)):
            x += float(math.comb(len(points)-1,j)*((1-t*i)**(len(points)-1-j))*((t*i)**j)*points[j][0])
            y += float(math.comb(len(points)-1,j)*((1-t*i)**(len(points)-1-j))*((t*i)**j)*points[j][1])
        ret.append([x,y])
    return ret

# Fungsi bruteforce
def BFMain(points,iterate):
    # Mulai waktu perhitungan
    start = time.time()

    # Mulai program Brute Force
    pointAkhir = BruteForce(points,iterate)

    # Stop waktu perhitungan
    end = time.time()

    # Menghitung lama waktu yang diperlukan
    totalWaktu = end - start

    # Menggambar kurva
    for i in range(len(points)-1) :
        plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], marker='o', linestyle='-', color="blue", label = "Titik Kontrol" if i == 0 else "")
    for i in range(len(pointAkhir)-1) :
        plt.plot([pointAkhir[i][0], pointAkhir[i+1][0]], [pointAkhir[i][1], pointAkhir[i+1][1]], marker='o', linestyle='-', color="red", label = "Kurva Bezier" if i == 0 else "")

    xMin, xMax = plt.xlim()
    yMin, yMax = plt.ylim()
    plt.text(xMin,yMax, f"Waktu program: {totalWaktu:.4f} detik", fontsize=14)

    plt.grid(True)
    plt.legend(loc = "best")
    plt.show()