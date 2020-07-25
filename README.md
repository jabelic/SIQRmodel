
# New SIQRmodel for COVID-19

SIQRモデルによる分析により、7.16.2020現在での新型コロナウイルス感染症の今後の感染拡大の予想とそれを抑える有効な政策を提案する。


## SIQR model

SIQRモデルはSIRモデルという疫学における区画モデルの発展型とされる数理モデルである。主にSIRモデルは感染症のシミュレーションに用いられるが、SNSの拡散モデルなど幅広い汎用例がある。
今度の感染症の感染拡大のシミュレーションでは全人口を、「未感染者(susceptible)」「市中感染者(infectious)」「隔離感染者(quarantine)」「治癒者/死亡者(recovery)」という４つのパートに分けてこれらの人口の移動を考える。ここで考えられる。

> ここに数式の画像を貼る(LaTeXiT)


## Simulation
simulationには`scipy.odeint`を使用した。数値解法はadams法(どのそれかは不明)である。
初期値は7.16.2020現在の[東京都新型コロナウイルス感染症対策サイト](https://stopcovid19.metro.tokyo.lg.jp/)の値を参考に概算で出したものを使用した。

|S|Q|I|R|
| --- | --- | --- | --- |
|9990900(人)|700(人)|1500(人)|6700(人)|


感染者の数が人口に対して非常に少ないため、ここでは感染者と快復者のグラフを示す。

>ここで画像を貼る




## Analysis






# reference
[The SIR Model for Spread of Disease - The Differential Equation Model](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model)
