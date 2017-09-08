#!/usr/bin/python
import sys
import argparse
import numpy as np
from io import StringIO
import csv
from astropy import constants as const
from astropy import units as u

def Blambda(T,lamb):
    lamb5=(lamb.to(u.m))**5    
    fac=const.h*const.c/(lamb.to(u.m)*const.k_B*T)
    bl=2.0*(const.c**2)*const.h/lamb5/(np.exp(fac)-1)
    return bl.to(u.erg/u.cm/u.cm/u.angstrom/u.s)

def Blunitless(T,lamb):
    lamb5=(lamb.to(u.m))**5    
    fac=const.h*const.c/(lamb.to(u.m)*const.k_B*T)
    bl=2.0*(const.c**2)*const.h/lamb5/(np.exp(fac)-1)
    return bl


def photon_Blunitless(T,lamb):
    pB=Blambda(T,lamb)/(const.h*const.c/(lamb.to(u.m)))

    return pB

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute Planck function')
    parser.add_argument('-t', nargs=1,required=True,help='temperature [K]')
    parser.add_argument('-micron', nargs=1,help='lambda (micron)')
    parser.add_argument('-nm', nargs=1,help='lambda (nm)')

    parser.add_argument('-d', nargs=1,help='distance [pc]')
    parser.add_argument('-r', nargs=2,help='radius, unit ex) 2.0 RE, 3.0 Rsol')

    parser.add_argument('-Dm', nargs=1,help='telescope diameter [m]')
    parser.add_argument('-dmicron', nargs=1,help='band width [micron]')
    parser.add_argument('-th', nargs=1,help='exposure [hour]')
    parser.add_argument('-tp', nargs=1,help='throughput')

    args = parser.parse_args()           
    tin=float(args.t[0])*u.K
    
    if args.micron:
        lamin=float(args.micron[0])*u.micron
    elif args.nm:
        lamin=float(args.nm[0])*u.nm
    else:
        print("set wavelength (-micron or -nm).")
        sys.exit("EXIT")

    print("B(lambda) for",tin,"at ",lamin)
    print('{:e}'.format(Blunitless(tin,lamin).to(u.erg/u.cm/u.cm/u.angstrom/u.s)))
    print('{:e}'.format(Blunitless(tin,lamin).to(u.erg/u.cm/u.cm/u.micron/u.s)))
    print('{:e}'.format(Blunitless(tin,lamin).to(u.J/u.m/u.m/u.m/u.s)))

    if args.d and args.r:
        d=float(args.d[0])*u.pc
        if args.r[1]=="RE" or args.r[1]=="Re":
            runit=const.R_earth
        elif args.r[1]=="RJ" or args.r[1]=="Rj":
            runit=const.R_jup
        elif args.r[1]=="RSun" or args.r[1]=="Rsun" or args.r[1]=="Rsol" or args.r[1]=="Rs":
            runit=const.R_sun
        else:
            sys.exit("No unit for radius. Use Re, Rj, Rsun etc.")

            
        r=float(args.r[0])*runit
        
        flux=np.pi*Blunitless(tin,lamin)*r*r/(d*d)
        print("---------------------")
        print("FLUX from a sphere with r=",args.r[0],runit.name,"and","d=",d)
        print(flux.to(u.erg/u.cm/u.cm/u.micron/u.s))

        photonf=np.pi*photon_Blunitless(tin,lamin)*r*r/(d*d)
        print("---------------------")
        print("Photon FLUX from a sphere with r=",args.r[0],runit.name,"and","d=",d)
        print(photonf.to(1/u.cm/u.cm/u.micron/u.s))

        if args.Dm and args.dmicron and args.th and args.tp:
            a=np.pi*(float(args.Dm[0])/2.0*u.m)**2
            dl=float(args.dmicron[0])*u.micron
            texp=float(args.th[0])*u.h
            throughput=float(args.tp[0])
            photon=photonf*a*dl*texp*throughput
            print("---------------------")
            print("Photon Count with observation:")
            print("  telescope diameter", args.Dm[0], "[m]")
            print("  band width", args.dmicron[0],"[micron]")
            print("  exposure", args.th[0],"[hour]")
            print("  throughput", args.tp[0])

            print("N=",'{:e}'.format(photon.to(1)))
            print("photon noise 1/sqrt(N)=",np.sqrt(1.0/photon.to(1))*1e6,"[ppm]")
