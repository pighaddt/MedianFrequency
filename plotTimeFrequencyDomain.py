import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft
import scipy.fftpack as fftpack


def plotTimeFrequencyDomain(LRec):
    # # data = pd.read_csv(r'E:\matlab2015a\NTUS_MuscleStartupSequence\1028\right1\swingtest1.csv', skiprows=4, usecols=[3, 8])
    # LRec = data.iloc[:, 1]
    LRec = np.array(LRec)
    Fs = 2000  # Sampling frequency
    T = 1 / Fs  # Sampling period
    L = len(LRec)  # Length of signal
    t = np.arange(len(LRec)) * T  # Time vector
    # 取樣點選擇1400個，因為設定的訊號頻率分量最高為600赫茲，根據取樣定理知取樣頻率要大於訊號頻率2倍，所以這裡設定取樣頻率為1400赫茲（即一秒內有1400個取樣點，一樣意思的）
    x = np.linspace(0, len(LRec) - 1, len(LRec))
    # print(x)
    # 設定需要取樣的訊號，頻率分量有180，390和600
    yy = fft(LRec)  # 快速傅立葉變換
    yf = abs(fft(LRec))  # 取絕對值

    yf1 = abs(fft(LRec) / len(x))  # 歸一化處理
    yf1 = yf1[range(int(len(x) / 2) + 1)] * 2  # 由於對稱性，只取一半區間
    yf1shift = fftpack.fftshift(yf1)

    xf = Fs * np.arange(len(LRec)) / L  # 頻率
    xf1 = xf
    xf2 = xf[range(int(len(x) / 2))]  # 取一半區間
    fStop1 = np.arange(-1 * int(L / 2), int(L / 2))
    # print(np.size(fStop1))
    # fStop1 = fStop1.shape
    fStop2 = np.arange(len(LRec) / 2)

    f1 = Fs * fStop1 / L
    f2 = Fs * fStop2 / L

    ##FFT median frequency
    sum = 0
    for i in range(1, 1000):
        # print(yf[i])
        sum = sum + yf1[i]

    halfSum = int(sum / 2)

    target = 0
    j = 1
    while target < halfSum:
        j = j + 1
        target = target + yf1[j]

    plt.figure()
    plt.vlines(f2[j], 0, 10, colors="r", linestyles='solid')
    plt.plot(f2, yf1, 'b')
    plt.xlim([1, 1000])
    plt.title('FFT of Mixed wave(normalization)', fontsize=9, color='r')
    plt.text(f2[j], 6, "median frequencyHz = " + str(f2[j]))
    # print(f2[j])
    # plt.subplot(224)
    # plt.plot(f2, yf2, 'b')
    # plt.title('FFT of Mixed wave)', fontsize=10, color='#F08080')
    plt.show()
    return f2[j]
