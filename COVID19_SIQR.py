import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



def SIQR(v, t, beta, gamma, gamma_dash, p):
    """
    Define the new SIQR model for COVID-19.
    
    Parameters
    ----------------
    v: list
        v = [S, I, Q, R]
        S: 未感染者
        I: 市中感染者
        Q: 隔離者
        R: 回復(抗体保持)
    t: float
        represent time. need for scipy.odeint.
    beta: float
        感染割合
    gamma: float
        回復割合
    p: float
        隔離率
    
    Returns
    -----------
    rvalue: list
        rvalue = [S', I', Q', R']
    """
    rvalue = [0,0,0,0]
    rvalue[0] = - beta * v[0] * v[1]
    rvalue[1] = beta * v[0] * v[1] - p * v[1] - gamma * v[1]
    rvalue[2] = p * v[1] - gamma_dash * v[2]
    rvalue[3] = gamma * v[1] + gamma_dash * v[2]
    return rvalue

def calc_proc(times, beta_const, gamma_const, gamma_dash_const, p):
    """
    数値計算 using odeint.
    
    Parameter
    --------------
    times: list
        数値計算のためのきざみ幅dtでの時間配列.
    
    beta_const: float
        感染率
    
    gamma_const: float
        未発症者の回復率
    
    gamma_dash_const: float
        隔離感染者の回復率
    
    p: float
        感染者の隔離率

    Returns
    -----------
    R0: float
        基本再生産数. 感染した1人の感染者が, 
        誰も免疫を持たない集団に加わったとき
        平均して何人に直接感染させる人数.
    
    result: float
        数値計算の結果.
        
    """
    S_0=9990900
    I_0=700
    Q_0=1500
    R_0=6700
    ini_state = [S_0,I_0,Q_0,R_0]
    #print("p",p)
    args  =(beta_const, gamma_const, gamma_dash_const, p)
    N_total = S_0 + I_0 + Q_0 + R_0
    R0 = N_total * beta_const * (1/gamma_const)
    print("R0: ",R0)
    
    result = odeint(SIQR, ini_state, times, args)
    print(result)
    return R0,result


def plot(R0, p, times, result):
    str_out = "basic rate of reproduction : {}".format(format(R0, ".3f"))
    str_out += "  "
    str_out += "Isolation rate : {}".format(format(p, ".3f"))
    plt.figure(dpi=100)
    plt.title(str_out)
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.ylim(0,10000000)
    plt.plot(times, result)
    plt.legend(['uninfected person','Infection Non-isolator','Infection Quarantine','recuperator'])
    #plt.savefig("pic/newSIQR-case5.png")
    #plt.show()





