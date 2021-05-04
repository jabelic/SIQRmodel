import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import COVID19_SIQR as siqr

def susceptible(result, casename:str):
    S = [result[i][0] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, S,label="S")
    plt.title(f"S:susceptible  {casename}")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    plt.savefig(f"pic/newSIQR-S-{casename}.png")
    #plt.show()
    print("30日間の新規感染者数: ", S[0] - S[100*30])
    print("30日後の未感染者数: ",S[100*30])

def infectious(result, casename:str):
    I = [result[i][1] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, I,label="I")
    plt.xlim(0,360)
    plt.title(f"I:infectious  {casename}")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    plt.savefig(f"pic/newSIQR-I-{casename}.png")
    #plt.show()
    print("30日後の感染者: ",I[100*30])



def quarantine(result, casename:str):
    Q = [result[i][2] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, Q,label="Q")
    plt.title(f"Q:quarantine  {casename}")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    plt.savefig(f"pic/newSIQR-Q-{casename}.png")
    #plt.show()
    print("30日後の隔離者: ",Q[100*30])



def recovery(result, casename:str):
    R = [result[i][3] for i in range(36000)]
    plt.figure(dpi=100)
    plt.plot(times, R,label="R")
    plt.title(f"R:recovery  {casename}")
    plt.xlabel('number of days')
    plt.ylabel('the number of people')
    plt.legend()
    plt.savefig(f"pic/newSIQR-R-{casename}.png")
    #plt.show()
    print("30日後の快復者/死亡者: ",R[100*30])
    

if __name__ == "__main__":
    case1 = {
        'beta_const': 0.126/10000000, # 接触率
        'p': 0.01,                    # 陽性者隔離率
        'name': 'case1'
    }
    case2 = {
        'beta_const': 0.126/10000000, # 接触率
        'p': 0.05,                    # 陽性者隔離率
        'name': 'case2'
    }
    case3 = {
        'beta_const': 0.096/10000000, # 接触率
        'p': 0.01,                    # 陽性者隔離率
        'name': 'case3'
    }
    case4 = {
        'beta_const': 0.096/10000000, # 接触率
        'p': 0.05,                    # 陽性者隔離率
        'name': 'case4'
    }
    case5 = {
        'beta_const': 0.126/10000000, # 接触率
        'p': 0.08,                    # 陽性者隔離率
        'name': 'case5'
    }
    t_max = 360
    dt = 0.01
    gamma_const = 1/12
    gamma_dash_const = 1/10
    times =np.arange(0,t_max, dt)
    results = {}
    for index, item in enumerate([case1, case2, case3, case4, case5]):
        print(f'\n ===== case{index+1} ===== \n')
        R0,result= siqr.calc_proc(times, item['beta_const'], gamma_const, gamma_dash_const, item['p'])
        results[index] = {'R0': R0, 'result': result}
    for index, item in enumerate([case1, case2, case3, case4, case5]):
        print(f'\n ===== case{index+1} ===== \n')
        siqr.plot(results[index]['R0'], item['p'], times, results[index]['result'], item['name'])
        susceptible(results[index]['result'], item['name'])
        infectious(results[index]['result'], item['name'])
        quarantine(results[index]['result'], item['name'])
        recovery(results[index]['result'], item['name'])
        plt.show()
    