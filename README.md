# exojupyter
Jupyter notebooks to generate various figures for exoplanets and Earth. This repository is for reproducing figures in my textbook written in Japanese, ["Exoplanet Exploration: Toward Exolife"](http://www.utp.or.jp/book/b345372.html).

このレポジトリは [「系外惑星探査：地球外生命をめざして」（東大出版会)](http://www.utp.or.jp/book/b345372.html) に掲載した図や計算を再現するためのコード集です。Python 3とJupyter notebookを使用しています。

<img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/planetdist.png" Titie="explanation" Width=300px>

python3とjupyter notebookを用いています。Anaconda(https://www.python.jp/install/windows/anaconda/install_anaconda.html)等でインストールしてお使いください。また系外惑星データベースにはexodata(https://github.com/ryanvarley/ExoData)を用いています。

-exodataのインストール例

```
git clone git://github.com/python-quantities/python-quantities.git
cd python-quantities/
python setup.py install
cd ../
git clone https://github.com/ryanvarley/ExoData
cd ExoData/
python setup.py install
```

##ipynb (Jupyter notebook)

- Figure 1.2 and 3.3 -- Exoplanet Positions on Galctic Plane and in a Distance-Teff Plane.ipynb
- Figure 1.3 -- orbits of exoplanets.ipynb
- Figure 2.21 -- Color version of Beetles after circular porizers (a pair of glasses for Harry Potter 3D).ipynb
- Figure 4.18 -- Microlensing magnification curve.ipynb
- Figure 4.5 -- Radial Velocity Curves.ipynb
- Figure 6.11 Radiative-Convective Adjustment for Dry Atmosphere.ipynb
- Figure 6.2-6.3 gray atmosphere in radiative equilibrium.ipynb
- Figure 6.4-6.5 Komabayashi-Ingersoll Limit.ipynb
- Figure 6.7-6.9-6.10 Moist Adiabat and Radiative-Convective Adjustment.ipynb
- Figure 7.11 -- Grating.ipynb
- Figure 8.5-8.7 Spin-Orbit Tomography.ipynb
- Figures 8.1,8.2,8.3 -- Markov Chain Monte Carlo.ipynb

## extra (おまけ)

- planckf.py: Photon noise from an isothermal sphere. 等温球を観測した時の光子数とノイズ
- radecsep_fast.py: Separation angle between two "radec"s. 天球上の二点の(RA,DEC)から離角を計算する速いコード

<img src="https://github.com/HajimeKawahara/exojupyter/blob/master/fig/circular.jpg" Titie="explanation" Width=300px>
