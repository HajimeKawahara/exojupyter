#!/usr/bin/python
import sys
import argparse
import numpy as np
from io import StringIO
import csv
from astropy import constants as const
from astropy import units as u


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute Hohmann orbit')
    parser.add_argument('-a1', nargs=1,default=[7000.0],help='initial radius [km]',type=float)
    parser.add_argument('-a2', nargs=1,default=[42000.0],help='final radius [km]',type=float)
    parser.add_argument('-g', nargs=1,default=[3.986004418e14],help='standard gravitational parameter (GM) m3/s2',type=float)
    parser.add_argument('-V', nargs=1,default=[2100.0],help='the velocity of the exhaust gas in rocket frame [m/s], the default value assumes hydragine',type=float)

    args = parser.parse_args()           
    a1=args.a1[0]*1.e3
    a2=args.a2[0]*1.e3
    GM=args.g[0]
    Vexh=args.V[0]
    dv1=np.sqrt(GM/a1)*(np.sqrt(2*a2/(a1+a2)) - 1.0)
    dv2=np.sqrt(GM/a2)*(- np.sqrt(2*a1/(a1+a2)) + 1.0)
    dv=dv1+dv2
    print("+ Hohmann transfer from a1=",args.a1[0],"[km] to a2=",args.a2[0],"[km]")
    print("----------------------------------")
    print("dv1,dv2,dv [m/s]")
    print(dv1,dv2,dv)
    print("----------------------------------")
    h=dv/Vexh
    mdm=1.0-np.exp(-h)
    print("+ required fuel mass of delta m")
    print("delta m/m=",mdm,"for Vexh",Vexh,"[m/s]")
