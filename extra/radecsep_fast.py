import argparse
import numpy as np
import time

#see https://en.wikipedia.org/wiki/Great-circle_distance
#All the angles are written in degree.


def sepfast_normal(ra1,dec1,ra2,dec2):
    fac=np.pi/180.0
    rax1=ra1*fac
    decx1=dec1*fac
    rax2=ra2*fac
    decx2=dec2*fac
    cosdlam=np.cos(np.abs(rax1-rax2))
    return np.arccos(np.sin(decx1)*np.sin(decx2)+np.cos(decx1)*np.cos(decx2)*cosdlam)/fac


def sepfast_harversine(ra1,dec1,ra2,dec2):
    fac=np.pi/180.0
    rax1=ra1*fac
    decx1=dec1*fac
    rax2=ra2*fac
    decx2=dec2*fac
    sindlam2=np.sin((np.abs(rax1-rax2))/2.0)
    sindphi2=np.sin((np.abs(decx1-decx2))/2.0)
    return 2.0*np.arcsin(np.sqrt(sindphi2**2 + +np.cos(decx1)*np.cos(decx2)*(sindlam2**2)))/fac
    
def sepfast_Vinsenty(ra1,dec1,ra2,dec2):
    fac=np.pi/180.0
    rax1=ra1*fac
    decx1=dec1*fac
    rax2=ra2*fac
    decx2=dec2*fac
    sindlam=np.sin(np.abs(rax1-rax2))
    cosdlam=np.cos(np.abs(rax1-rax2))
    sindecx1=np.sin(decx1)
    sindecx2=np.sin(decx2)
    cosdecx1=np.cos(decx1)
    cosdecx2=np.cos(decx2)
    
    fac1=sindecx1*sindecx2+cosdecx1*cosdecx2*cosdlam
    fac2=(cosdecx2**2)*(sindlam**2)+(cosdecx1*sindecx2 - sindecx1*cosdecx2*cosdlam)**2
    return np.arctan2(np.sqrt(fac2),fac1)/fac


def sepslow(ra1,dec1,ra2,dec2):
    from astropy.coordinates import SkyCoord
    from astropy import units as u
    c1 = SkyCoord(ra1, dec1, frame='icrs', unit='deg')
    c2 = SkyCoord(ra2, dec2, frame='icrs', unit='deg')
    c=c1.separation(c2)
    
    return c.degree


def comparison_time(ra1,dec1,ra2,dec2):

    start = time.time()    
    print(sepfast_normal(ra1,dec1,ra2,dec2))
    elapsed_time = time.time() - start
    print(("Normal, elapsed_time:{0}".format(elapsed_time)) + "[sec]")
    print("=================================")
    start = time.time()    
    print(sepfast_harversine(ra1,dec1,ra2,dec2))
    elapsed_time = time.time() - start
    print(("Harversine, elapsed_time:{0}".format(elapsed_time)) + "[sec]")
    print("=================================")

    start = time.time()    
    print(sepfast_Vinsenty(ra1,dec1,ra2,dec2))
    elapsed_time = time.time() - start
    print(("Vinsenty, elapsed_time:{0}".format(elapsed_time)) + "[sec]")
    print("=================================")

    start = time.time()
    print(sepslow(ra1,dec1,ra2,dec2))
    elapsed_time = time.time() - start
    print(("Astropy.coordinate, elapsed_time:{0}".format(elapsed_time)) + "[sec]")
    print("=================================")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute Planck function')
    parser.add_argument('-r', nargs=4,default=[140.0,36.0,141.0,37.0],help='radec (ra1,dec1,ra2,dec2)')
    args = parser.parse_args()           
    ra1=args.r[0]
    dec1=args.r[1]
    ra2=args.r[2]
    dec2=args.r[3]

    comparison_time(ra1,dec1,ra2,dec2)
    
