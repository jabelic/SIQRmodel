import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import COVID19_SIQR as siqr

def susceptible(result):
    S = [result[i][0] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, S,label="S")
    plt.title("S:susceptible")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    #plt.savefig("pic/newSIQR-S-case5.png")
    #plt.show()
    print(S[0] - S[100*30])
    print(S[100*30])

def infectious(result):
    I = [result[i][1] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, I,label="I")
    plt.xlim(0,360)
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.title("I:infectious")
    plt.legend()
    #plt.savefig("pic/newSIQR-I-case5.png")
    #plt.show()
    print("30日後の感染者:",I[100*30])



def quarantine(result):
    Q = [result[i][2] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, Q,label="Q")
    plt.title("Q:quarantine")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    #plt.savefig("pic/newSIQR-Q-case5.png")
    #plt.show()
    print("30日後の隔離者",Q[100*30])




def recovery(result):
    R = [result[i][3] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, R,label="R")
    plt.title("R:recovery")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    #plt.savefig("pic/newSIQR-R-case5.png")
    #plt.show()
    print("30日後の快復者/死亡者",R[100*30])

if __name__ == "__main__":
    t_max = 360
    dt = 0.01
    beta_const = 0.126/10000000
    gamma_const = 1/12
    gamma_dash_const = 1/10
    p = 0.08
    times =np.arange(0,t_max, dt)
    R0,result= siqr.calc_proc(times, beta_const, gamma_const, gamma_dash_const, p)
    siqr.plot(R0,p,times,result)
    susceptible(result)
    infectious(result)
    quarantine(result)
    recovery(result)
    plt.show()