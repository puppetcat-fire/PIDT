"""
多变量转移熵计算
"""
import matplotlib.pyplot as plt
from pathlib import Path
Path.ls = lambda x: list(x.iterdir())
from tqdm import tqdm
import numpy as np
import jpype
from jpype import *
import initJvm

class TransferEntropyCalculatorMultiVariateKraskov:

    """
    Description:


    """

    def __init__(
        self,
        source=None,
        destination=None,
        sourceDimensions=2,
        destDimensions=2,
        k_HISTORY=1,
        k_TAU=1,
        l_HISTORY=1,
        l_TAU=1,
        DELAY=1,
        k=4,
        NOISE_LEVEL_TO_ADD=1e-8,
        ALG_NUM=1,
        cal_sig=False,
        sig_num=100,
    ):

        self.source = source
        self.destination = destination
        self.sourceDimensions = sourceDimensions
        self.destDimensions = destDimensions
        self.k_HISTORY = k_HISTORY
        self.k_TAU = k_TAU
        self.l_HISTORY = l_HISTORY
        self.l_TAU = l_TAU
        self.DELAY = DELAY
        self.k = k
        self.cal_sig = cal_sig
        self.sig_num = sig_num
        self.NOISE_LEVEL_TO_ADD = NOISE_LEVEL_TO_ADD
        self.ALG_NUM = ALG_NUM

    def __call__(self, source, destination, tau, m=1, n=1):

        self.source = source
        self.destination = destination
        self.sourceDimensions = np.min(source.shape)
        self.destDimensions = np.min(destination.shape)
        self.DELAY = tau

        calcClass = JPackage(
            "infodynamics.measures.continuous.kraskov"
        ).TransferEntropyCalculatorMultiVariateKraskov
        calc = calcClass()

        calc.setProperty("sourceDimensions", str(self.sourceDimensions))
        calc.setProperty("destDimensions", str(self.destDimensions))
        calc.setProperty("k_HISTORY", str(self.k_HISTORY))
        calc.setProperty("k_TAU", str(self.k_TAU))
        calc.setProperty("l_HISTORY", str(self.l_HISTORY))
        calc.setProperty("l_TAU", str(self.l_TAU))
        calc.setProperty("DELAY", str(self.DELAY))
        calc.setProperty("k", str(self.k))
        calc.setProperty("NOISE_LEVEL_TO_ADD", str(self.NOISE_LEVEL_TO_ADD))
        calc.setProperty("ALG_NUM", str(self.ALG_NUM))

        calc.initialise(m,n)
        self.calc = calc
        self.calc.setObservations(
            JArray(JDouble, 2)(source), JArray(JDouble, 2)(destination)
        )

        result = self.calc.computeAverageLocalOfObservations()
        if not self.cal_sig:
            return result
        else:
            measDist = self.calc.computeSignificance(self.sig_num)
            mean = (measDist.getMeanOfDistribution(),)
            std = (measDist.getStdOfDistribution(),)
            pVal = measDist.pValue
            return result, [mean, std, pVal]    

if __name__ == "__main__":
    estimator_ksg = TransferEntropyCalculatorMultiVariateKraskov()        
    datas = None
    with open("out2.txt") as f:
        datas = f.readlines()
    if datas:
        raws1 = []
        raws2 = []
        for data in datas:
            raws1.append(int(data[:16][6]))
            raws2.append(int(data[:16][7]))

    x = np.array([[i]for i in raws1])
    y = np.array([[i]for i in raws2])

    fig, axs = plt.subplots(2, 1, figsize=(6, 4))
    axs[0].plot(x, label="Electric_field", color="blue")
    axs[0].legend()
    axs[1].plot(y, label="Dst", color="red")
    axs[1].legend()
    plt.show()

    # 计算转移熵结果，并绘制图像
    result = []
    taus = 95
    for tau in tqdm(range(taus)):
        result.append(estimator_ksg(source=x, destination=y, tau=tau))

    plt.figure(figsize=(8, 3))
    plt.plot(range(taus), result)
    plt.show()