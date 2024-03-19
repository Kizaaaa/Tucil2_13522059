import matplotlib.pyplot as plt
import time

# Fungsi untuk mendapatkan titik tengah dari 2 buah titik
def getMidPoint(p1,p2):
    return [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]

# Fungsi untuk menghasilkan titik tengah diantara titik kontrol kemudian
# mencari lagi titik tengahnya secara rekursif
def getPoints(points):
    if len(points) <= 1 :
        return points
    else :
        ret = [points[0]]
        temp = []
        for i in range(len(points) - 1) :
            temp.append(getMidPoint(points[i],points[i+1]))
        ret.extend(getPoints(temp))
        ret.append(points[-1])
        return ret


# Fungsi Divide and Conquer
def divideAndConquer(points, iterate):
    if iterate == 0 :
        return []
    else :
        points = getPoints(points)
        iterate -= 1
        idxMid = len(points)//2
        return divideAndConquer(points[0:idxMid+1],iterate) + [points[idxMid]] + divideAndConquer(points[idxMid:],iterate)
    
def DNCmain(points,iterate) :
    # Mulai waktu perhitungan
    start = time.time()

    # Mulai program Divide and Conquer
    pointAkhir = []
    pointAkhir.append(points[0])
    pointAkhir.extend(divideAndConquer(points,iterate))
    pointAkhir.append(points[-1])

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