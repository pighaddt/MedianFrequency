import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def RMSStartPoint(data, mask):
    def rms_function(data, window):
        rms = np.array(data)

        halfMask = round(window)
        for index in range(len(data)):
            # lower upper setting
            if index < halfMask:
                lower = 1
            else:
                lower = index - halfMask

            if index > len(data) - halfMask:
                upper = len(data)
            else:
                upper = index + halfMask

            current = data[lower:upper]
            power2 = current * current
            mean = power2.mean()
            sqrt = np.sqrt(mean)
            rms[index] = sqrt

        return rms

    data = np.array(data)
    plt.figure(1)
    plt.plot(data)
    # print(data)
    rms = rms_function(data, 25)

    # Threshold setting
    i = 0
    threshold = 300
    for index in range(len(data)):
        if rms[index] < threshold:
            i = i + 1
        else:
            break

    timer = float(i) / 2000
    # print(i) # startPointIndex
    plt.figure(1)
    plt.title('Raw Data && RMS Line && Start Point', fontsize=15, color='Black')
    plt.plot(rms, '--')
    plt.plot(i, rms[i], marker="o", color="black")
    # plt.hlines(rms[i], i-1000, i, colors="r", linestyles='solid')
    plt.text(i, rms[i] + 600, "start point time = " + str(round(timer, 4)) + "(s)")
    plt.grid(True)
    plt.show()

##test function 20210111
# if __name__ == '__main__':
#     path = r"C:\Users\angus\Desktop\Python\GUIFunction\swingtest1.csv"
#     data = pd.read_csv(path,
#                        skiprows=3,
#                        usecols=[3])
#     RMSStartPoint(data, 25)