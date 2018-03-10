# exojupyter
Jupyter notebooks to generate various figures for exoplanets and Earth. This repository is for reproducing figures in my textbook written in Japanese, ["Exoplanet Exploration: Toward Exolife"](http://www.utp.or.jp/book/b345372.html).

<img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/hyoushi.jpg" Titie="explanation" Height=300px>

このレポジトリは [「系外惑星探査：地球外生命をめざして」（東大出版会)](http://www.utp.or.jp/book/b345372.html) に掲載した図や計算を再現するためのコード集です。Python3とjupyter notebookを用いています。[Anaconda](https://www.python.jp/install/windows/anaconda/install_anaconda.html) 等でインストールしてお使いください。また系外惑星データベースには[exodata](https://github.com/ryanvarley/ExoData) を用いています。

- exodataのインストール例

```
git clone git://github.com/python-quantities/python-quantities.git
cd python-quantities/
python setup.py install
cd ../
git clone https://github.com/ryanvarley/ExoData
cd ExoData/
python setup.py install
```

<img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/planetdist.png" Titie="explanation" Height=250px><img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/circular.jpg" Titie="explanation" Height=250px>

## ipynb (Jupyter notebook)

- Figure 1.2 and 3.3 -- Exoplanet Positions on Galctic Plane and in a Distance-Teff Plane.ipynb
銀河上での系外惑星の分布など
- Figure 1.3 -- Orbits of exoplanets.ipynb
代表的な系外惑星の軌道
- Figure 2.21 -- Color version of Beetles after circular porizers (a pair of glasses for Harry Potter 3D).ipynb
黄金虫の円偏光（カラーバージョン）
- Figure 4.18 -- Microlensing magnification curve.ipynb
マイクロレンジングの増光曲線
- Figure 4.5 -- Radial Velocity Curves.ipynb
視線速度カーブ
- Figure 6.2-6.3 gray atmosphere in radiative equilibrium.ipynb
放射平衡状態の灰色大気
- Figure 6.4-6.5 Komabayashi-Ingersoll Limit.ipynb
成層圏の射出限界
- Figure 6.7-6.9-6.10 Moist Adiabat and Radiative-Convective Adjustment.ipynb
放射層と対流層の接続(湿潤大気)
- Figure 6.11 Radiative-Convective Adjustment for Dry Atmosphere.ipynb
放射層と対流層の接続(乾燥大気)
- Figure 7.11 -- Grating.ipynb
回折格子
- Figure 8.5-8.7 Spin-Orbit Tomography.ipynb
系外惑星のマッピング手法
- Figures 8.1,8.2,8.3 -- Markov Chain Monte Carlo.ipynb
マルコフ鎖モンテカルロの例(emceeを使用)

## extra (おまけ)

- planckf.py: Photon noise from an isothermal sphere. 等温球を観測した時の光子数とノイズ
- radecsep_fast.py: Separation angle between two "radec"s. 天球上の二点の(RA,DEC)から離角を計算する速いコード

<img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/circular.jpg" Titie="explanation" Width=300px>
