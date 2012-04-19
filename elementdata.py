# Copyright 2010 Torbjorn Bjorkman
# This file is part of cif2cell
#
# cif2cell is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cif2cell is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cif2cell.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************************
#  Description: Chemical element data useful for generating setups for electronic
#               structure programs.
#  Author:      Torbjorn Bjorkman, torbjorn.bjorkman(at)aalto.fi
#  Affiliation: COMP, Aaalto University School of Science,
#               Department of Applied Physics, Espoo, Finland
#******************************************************************************************
class ElementData:
    """
    Class for storing some data about the chemical elements.

    elementnr       :  dictionary of the element numbers.
                       Example: elementnr['O'] is 8.
    elementblock    :  dictionary of which block an element belong to (spdf).
                       Example: elementblock['Fe'] is 'd'
    angularmomentum :  dictionary for the angular momentum quantum number of s,p,d,f states
    emtoelements    :  element setups for EMTO
    """
    def __init__(self):
        # Element numbers
        self.elementnr = {
            'H'  : 1  ,
            'D'  : 1  ,
            'He' : 2  ,
            'Li' : 3  ,
            'Be' : 4  ,
            'B'  : 5  ,
            'C'  : 6  ,
            'N'  : 7  ,
            'O'  : 8  ,
            'F'  : 9  ,
            'Ne' : 10 ,
            'Na' : 11 ,
            'Mg' : 12 ,
            'Al' : 13 ,
            'Si' : 14 ,
            'P'  : 15 ,
            'S'  : 16 ,
            'Cl' : 17 ,
            'Ar' : 18 ,
            'K'  : 19 ,
            'Ca' : 20 ,
            'Sc' : 21 ,
            'Ti' : 22 ,
            'V'  : 23 ,
            'Cr' : 24 ,
            'Mn' : 25 ,
            'Fe' : 26 ,
            'Co' : 27 ,
            'Ni' : 28 ,
            'Cu' : 29 ,
            'Zn' : 30 ,
            'Ga' : 31 ,
            'Ge' : 32 ,
            'As' : 33 ,
            'Se' : 34 ,
            'Br' : 35 ,
            'Kr' : 36 ,
            'Rb' : 37 ,
            'Sr' : 38 ,
            'Y'  : 39 ,
            'Zr' : 40 ,
            'Nb' : 41 ,
            'Mo' : 42 ,
            'Tc' : 43 ,
            'Ru' : 44 ,
            'Rh' : 45 ,
            'Pd' : 46 ,
            'Ag' : 47 ,
            'Cd' : 48 ,
            'In' : 49 ,
            'Sn' : 50 ,
            'Sb' : 51 ,
            'Te' : 52 ,
            'I'  : 53 ,
            'Xe' : 54 ,
            'Cs' : 55 ,
            'Ba' : 56 ,
            'La' : 57 ,
            'Ce' : 58 ,
            'Pr' : 59 ,
            'Nd' : 60 ,
            'Pm' : 61 ,
            'Sm' : 62 ,
            'Eu' : 63 ,
            'Gd' : 64 ,
            'Tb' : 65 ,
            'Dy' : 66 ,
            'Ho' : 67 ,
            'Er' : 68 ,
            'Tm' : 69 ,
            'Yb' : 70 ,
            'Lu' : 71 ,
            'Hf' : 72 ,
            'Ta' : 73 ,
            'W'  : 74 ,
            'Re' : 75 ,
            'Os' : 76 ,
            'Ir' : 77 ,
            'Pt' : 78 ,
            'Au' : 79 ,
            'Hg' : 80 ,
            'Tl' : 81 ,
            'Pb' : 82 ,
            'Bi' : 83 ,
            'Po' : 84 ,
            'At' : 85 ,
            'Rn' : 86 ,
            'Fr' : 87 ,
            'Ra' : 88 ,
            'Ac' : 89 ,
            'Th' : 90 ,
            'Pa' : 91 ,
            'U'  : 92 ,
            'Np' : 93 ,
            'Pu' : 94 ,
            'Am' : 95 ,
            'Cm' : 96 ,
            'Bk' : 97 ,
            'Cf' : 98 ,
            'Es' : 99 ,
            'Fm' : 100,
            'Me' : 101,
            'No' : 102,
            'Lr' : 103,
            'Rf' : 104,
            'Db' : 105,
            'Sg' : 106,
            'Bh' : 107,
            'Hs' : 108,
            'Mt' : 109,
            'Uun': 110,
            'Uuu': 111,
            'Uub': 112}
        
        # Periods
        self.elementperiod = {
            'H'  : 1 ,
            'D'  : 1 ,
            'He' : 2 ,
            'Li' : 2 ,
            'Be' : 2 ,
            'B'  : 2 ,
            'C'  : 2 ,
            'N'  : 2 ,
            'O'  : 2 ,
            'F'  : 2 ,
            'Ne' : 2 ,
            'Na' : 3 ,
            'Mg' : 3 ,
            'Al' : 3 ,
            'Si' : 3 ,
            'P'  : 3 ,
            'S'  : 3 ,
            'Cl' : 3 ,
            'Ar' : 3 ,
            'K'  : 4 ,
            'Ca' : 4 ,
            'Sc' : 4 ,
            'Ti' : 4 ,
            'V'  : 4 ,
            'Cr' : 4 ,
            'Mn' : 4 ,
            'Fe' : 4 ,
            'Co' : 4 ,
            'Ni' : 4 ,
            'Cu' : 4 ,
            'Zn' : 4 ,
            'Ga' : 4 ,
            'Ge' : 4 ,
            'As' : 4 ,
            'Se' : 4 ,
            'Br' : 4 ,
            'Kr' : 4 ,
            'Rb' : 5 ,
            'Sr' : 5 ,
            'Y'  : 5 ,
            'Zr' : 5 ,
            'Nb' : 5 ,
            'Mo' : 5 ,
            'Tc' : 5 ,
            'Ru' : 5 ,
            'Rh' : 5 ,
            'Pd' : 5 ,
            'Ag' : 5 ,
            'Cd' : 5 ,
            'In' : 5 ,
            'Sn' : 5 ,
            'Sb' : 5 ,
            'Te' : 5 ,
            'I'  : 5 ,
            'Xe' : 5 ,
            'Cs' : 6 ,
            'Ba' : 6 ,
            'La' : 6 ,
            'Ce' : 6 ,
            'Pr' : 6 ,
            'Nd' : 6 ,
            'Pm' : 6 ,
            'Sm' : 6 ,
            'Eu' : 6 ,
            'Gd' : 6 ,
            'Tb' : 6 ,
            'Dy' : 6 ,
            'Ho' : 6 ,
            'Er' : 6 ,
            'Tm' : 6 ,
            'Yb' : 6 ,
            'Lu' : 6 ,
            'Hf' : 6 ,
            'Ta' : 6 ,
            'W'  : 6 ,
            'Re' : 6 ,
            'Os' : 6 ,
            'Ir' : 6 ,
            'Pt' : 6 ,
            'Au' : 6 ,
            'Hg' : 6 ,
            'Tl' : 6 ,
            'Pb' : 6 ,
            'Bi' : 6 ,
            'Po' : 6 ,
            'At' : 6 ,
            'Rn' : 6 ,
            'Fr' : 7 ,
            'Ra' : 7 ,
            'Ac' : 7 ,
            'Th' : 7 ,
            'Pa' : 7 ,
            'U'  : 7 ,
            'Np' : 7 ,
            'Pu' : 7 ,
            'Am' : 7 ,
            'Cm' : 7 ,
            'Bk' : 7 ,
            'Cf' : 7 ,
            'Es' : 7 ,
            'Fm' : 7 ,
            'Me' : 7 ,
            'No' : 7 ,
            'Lr' : 7 ,
            'Rf' : 7 ,
            'Db' : 7 ,
            'Sg' : 7 ,
            'Bh' : 7 ,
            'Hs' : 7 ,
            'Mt' : 7 ,
            'Uun': 7 ,
            'Uuu': 7 ,
            'Uub': 7 }
        
        # Element groups
        self.elementgroup = {
            'H'  : 1  ,
            'D'  : 1  ,
            'He' : 18 ,
            'Li' : 1  ,
            'Be' : 2  ,
            'B'  : 13 ,
            'C'  : 14 ,
            'N'  : 15 ,
            'O'  : 16 ,
            'F'  : 17 ,
            'Ne' : 18 ,
            'Na' : 1  ,
            'Mg' : 2  ,
            'Al' : 13 ,
            'Si' : 14 ,
            'P'  : 15 ,
            'S'  : 16 ,
            'Cl' : 17 ,
            'Ar' : 18 ,
            'K'  : 1  ,
            'Ca' : 2  ,
            'Sc' : 3  ,
            'Ti' : 4  ,
            'V'  : 5  ,
            'Cr' : 6  ,
            'Mn' : 7  ,
            'Fe' : 8  ,
            'Co' : 9  ,
            'Ni' : 10 ,
            'Cu' : 11 ,
            'Zn' : 12 ,
            'Ga' : 13 ,
            'Ge' : 14 ,
            'As' : 15 ,
            'Se' : 16 ,
            'Br' : 17 ,
            'Kr' : 18 ,
            'Rb' : 1  ,
            'Sr' : 2  ,
            'Y'  : 3  ,
            'Zr' : 4 ,
            'Nb' : 5 ,
            'Mo' : 6 ,
            'Tc' : 7 ,
            'Ru' : 8 ,
            'Rh' : 9 ,
            'Pd' : 10 ,
            'Ag' : 11 ,
            'Cd' : 12 ,
            'In' : 13 ,
            'Sn' : 14 ,
            'Sb' : 15 ,
            'Te' : 16 ,
            'I'  : 17 ,
            'Xe' : 18 ,
            'Cs' : 1 ,
            'Ba' : 2 ,
            'La' : 19 ,
            'Ce' : 19 ,
            'Pr' : 19 ,
            'Nd' : 19 ,
            'Pm' : 19 ,
            'Sm' : 19 ,
            'Eu' : 19 ,
            'Gd' : 19 ,
            'Tb' : 19 ,
            'Dy' : 19 ,
            'Ho' : 19 ,
            'Er' : 19 ,
            'Tm' : 19 ,
            'Yb' : 19 ,
            'Lu' : 3 ,
            'Hf' : 4 ,
            'Ta' : 5 ,
            'W'  : 6 ,
            'Re' : 7 ,
            'Os' : 8 ,
            'Ir' : 9 ,
            'Pt' : 10 ,
            'Au' : 11 ,
            'Hg' : 12 ,
            'Tl' : 13 ,
            'Pb' : 14 ,
            'Bi' : 15 ,
            'Po' : 16 ,
            'At' : 17 ,
            'Rn' : 18 ,
            'Fr' : 1 ,
            'Ra' : 2 ,
            'Ac' : 19 ,
            'Th' : 19 ,
            'Pa' : 19 ,
            'U'  : 19 ,
            'Np' : 19 ,
            'Pu' : 19 ,
            'Am' : 19 ,
            'Cm' : 19 ,
            'Bk' : 19 ,
            'Cf' : 19 ,
            'Es' : 19 ,
            'Fm' : 19 ,
            'Me' : 19 ,
            'No' : 19 ,
            'Lr' : 3 ,
            'Rf' : 4 ,
            'Db' : 5 ,
            'Sg' : 6 ,
            'Bh' : 7 ,
            'Hs' : 8 ,
            'Mt' : 9 ,
            'Uun': 10 ,
            'Uuu': 11 ,
            'Uub': 12 }
        
        # Element classification in s, p, d and f blocks
        self.elementblock = { 
            'H'  : 's'  ,
            'D'  : 's'  ,
            'He' : 's'  ,
            'Li' : 's'  ,
            'Be' : 's'  ,
            'B'  : 'p'  ,
            'C'  : 'p'  ,
            'N'  : 'p'  ,
            'O'  : 'p'  ,
            'F'  : 'p'  ,
            'Ne' : 'p' ,
            'Na' : 's' ,
            'Mg' : 's' ,
            'Al' : 'p' ,
            'Si' : 'p' ,
            'P'  : 'p' ,
            'S'  : 'p' ,
            'Cl' : 'p' ,
            'Ar' : 'p' ,
            'K'  : 's' ,
            'Ca' : 's' ,
            'Sc' : 'd' ,
            'Ti' : 'd' ,
            'V'  : 'd' ,
            'Cr' : 'd' ,
            'Mn' : 'd' ,
            'Fe' : 'd' ,
            'Co' : 'd' ,
            'Ni' : 'd' ,
            'Cu' : 'd' ,
            'Zn' : 'd' ,
            'Ga' : 'p' ,
            'Ge' : 'p' ,
            'As' : 'p' ,
            'Se' : 'p' ,
            'Br' : 'p' ,
            'Kr' : 'p' ,
            'Rb' : 's' ,
            'Sr' : 's' ,
            'Y'  : 'd' ,
            'Zr' : 'd' ,
            'Nb' : 'd' ,
            'Mo' : 'd' ,
            'Tc' : 'd' ,
            'Ru' : 'd' ,
            'Rh' : 'd' ,
            'Pd' : 'd' ,
            'Ag' : 'd' ,
            'Cd' : 'd' ,
            'In' : 'p' ,
            'Sn' : 'p' ,
            'Sb' : 'p' ,
            'Te' : 'p' ,
            'I'  : 'p' ,
            'Xe' : 'p' ,
            'Cs' : 's' ,
            'Ba' : 's' ,
            'La' : 'f' ,
            'Ce' : 'f' ,
            'Pr' : 'f' ,
            'Nd' : 'f' ,
            'Pm' : 'f' ,
            'Sm' : 'f' ,
            'Eu' : 'f' ,
            'Gd' : 'f' ,
            'Tb' : 'f' ,
            'Dy' : 'f' ,
            'Ho' : 'f' ,
            'Er' : 'f' ,
            'Tm' : 'f' ,
            'Yb' : 'f' ,
            'Lu' : 'f' ,
            'Hf' : 'd' ,
            'Ta' : 'd' ,
            'W'  : 'd' ,
            'Re' : 'd' ,
            'Os' : 'd' ,
            'Ir' : 'd' ,
            'Pt' : 'd' ,
            'Au' : 'd' ,
            'Hg' : 'd' ,
            'Tl' : 'p' ,
            'Pb' : 'p' ,
            'Bi' : 'p' ,
            'Po' : 'p' ,
            'At' : 'p' ,
            'Rn' : 'p' ,
            'Fr' : 's' ,
            'Ra' : 's' ,
            'Ac' : 'f' ,
            'Th' : 'f' ,
            'Pa' : 'f' ,
            'U'  : 'f' ,
            'Np' : 'f' ,
            'Pu' : 'f' ,
            'Am' : 'f' ,
            'Cm' : 'f' ,
            'Bk' : 'f' ,
            'Cf' : 'f' ,
            'Es' : 'f' ,
            'Fm' : 'f',
            'Me' : 'f',
            'No' : 'f',
            'Lr' : 'd',
            'Rf' : 'd',
            'Db' : 'd',
            'Sg' : 'd',
            'Bh' : 'd',
            'Hs' : 'd',
            'Mt' : 'd',
            'Uun': 'd',
            'Uuu': 'd',
            'Uub': 'd' }

        # Angular momentum quantum numbers
        self.angularmomentum = { 's' : 0, 'p' : 1, 'd' : 2, 'f' : 3 }

        # Covalent radii
        self.CovalentRadius = {
            'H'  : 0.32 ,
            'Ne' : 0.71 ,
            'F'  : 0.72 ,
            'O'  : 0.73 ,
            'N'  : 0.75 ,
            'C'  : 0.77 ,
            'B'  : 0.82 ,
            'Be' : 0.90 ,
            'He' : 0.93 ,
            'Ar' : 0.98 ,
            'Cl' : 0.99 ,
            'S'  : 1.02 ,
            'P'  : 1.06 ,
            'Si' : 1.11 ,
            'Kr' : 1.12 ,
            'Br' : 1.14 ,
            'Ni' : 1.15 ,
            'Se' : 1.16 ,
            'Co' : 1.16 ,
            'Cu' : 1.17 ,
            'Fe' : 1.17 ,
            'Mn' : 1.17 ,
            'Al' : 1.18 ,
            'Cr' : 1.18 ,
            'As' : 1.20 ,
            'Ge' : 1.22 ,
            'V'  : 1.22 ,
            'Li' : 1.23 ,
            'Rh' : 1.25 ,
            'Ru' : 1.25 ,
            'Zn' : 1.25 ,
            'Ga' : 1.26 ,
            'Os' : 1.26 ,
            'Ir' : 1.27 ,
            'Tc' : 1.27 ,
            'Re' : 1.28 ,
            'Pd' : 1.28 ,
            'W'  : 1.30 ,
            'Pt' : 1.30 ,
            'Mo' : 1.30 ,
            'Xe' : 1.31 ,
            'Ti' : 1.32 ,
            'I'  : 1.33 ,
            'Ta' : 1.34 ,
            'Nb' : 1.34 ,
            'Ag' : 1.34 ,
            'Au' : 1.34 ,
            'Te' : 1.36 ,
            'Mg' : 1.36 ,
            'Sn' : 1.41 ,
            'Sb' : 1.41 ,
            'U'  : 1.42 ,
            'In' : 1.44 ,
            'Sc' : 1.44 ,
            'Hf' : 1.44 ,
            'Zr' : 1.45 ,
            'At' : 1.45 ,
            'Bi' : 1.46 ,
            'Po' : 1.46 ,
            'Pb' : 1.47 ,
            'Cd' : 1.48 ,
            'Tl' : 1.48 ,
            'Hg' : 1.49 ,
            'Na' : 1.54 ,
            'Tm' : 1.56 ,
            'Lu' : 1.56 ,
            'Er' : 1.57 ,
            'Ho' : 1.58 ,
            'Dy' : 1.59 ,
            'Tb' : 1.59 ,
            'Gd' : 1.61 ,
            'Y'  : 1.62 ,
            'Sm' : 1.62 ,
            'Pm' : 1.63 ,
            'Nd' : 1.64 ,
            'Th' : 1.65 ,
            'Ce' : 1.65 ,
            'Pr' : 1.65 ,
            'La' : 1.69 ,
            'Yb' : 1.74 ,
            'Ca' : 1.74 ,
            'Eu' : 1.85 ,
            'Pu' : 1.87 ,
            'Sr' : 1.91 ,
            'Ba' : 1.98 ,
            'K'  : 2.03 ,
            'Rb' : 2.16 ,
            'Cs' : 2.35 
            }

        # Covalent radii, stolen from Jmol
        self.CovalentRadius2 = {
            'H'  : .230,  
            'He' : .930,  
            'Li' : .680,  
            'Be' : .350,  
            'B'  : .830,  
            'C'  : .680,  
            'N'  : .680,  
            'O'  : .680,  
            'F'  : .640,  
            'Ne' : 1.120, 
            'Na' : .970,  
            'Mg' : 1.100, 
            'Al' : 1.350, 
            'Si' : 1.200, 
            'P'  : .750,  
            'S'  : 1.020, 
            'Cl' : .990,  
            'Ar' : 1.570, 
            'K'  : 1.330, 
            'Ca' : .990,  
            'Sc' : 1.440, 
            'Ti' : 1.470, 
            'V'  : 1.330, 
            'Cr' : 1.350, 
            'Mn' : 1.350, 
            'Fe' : 1.340, 
            'Co' : 1.330, 
            'Ni' : 1.500, 
            'Cu' : 1.520, 
            'Zn' : 1.450, 
            'Ga' : 1.220, 
            'Ge' : 1.170, 
            'As' : 1.210, 
            'Se' : 1.220, 
            'Br' : 1.210, 
            'Kr' : 1.910, 
            'Rb' : 1.470, 
            'Sr' : 1.120, 
            'Y'  : 1.780, 
            'Zr' : 1.560, 
            'Nb' : 1.480, 
            'Mo' : 1.470, 
            'Tc' : 1.350, 
            'Ru' : 1.400, 
            'Rh' : 1.450, 
            'Pd' : 1.500, 
            'Ag' : 1.590, 
            'Cd' : 1.690, 
            'In' : 1.630, 
            'Sn' : 1.460, 
            'Sb' : 1.460, 
            'Te' : 1.470, 
            'I'  : 1.400, 
            'Xe' : 1.980, 
            'Cs' : 1.670, 
            'Ba' : 1.340, 
            'La' : 1.870, 
            'Ce' : 1.830, 
            'Pr' : 1.820, 
            'Nd' : 1.810, 
            'Pm' : 1.800, 
            'Sm' : 1.800, 
            'Eu' : 1.990, 
            'Gd' : 1.790, 
            'Tb' : 1.760, 
            'Dy' : 1.750, 
            'Ho' : 1.740, 
            'Er' : 1.730, 
            'Tm' : 1.720, 
            'Yb' : 1.940, 
            'Lu' : 1.720, 
            'Hf' : 1.570, 
            'Ta' : 1.430, 
            'W'  : 1.370, 
            'Re' : 1.350, 
            'Os' : 1.370, 
            'Ir' : 1.320, 
            'Pt' : 1.500, 
            'Au' : 1.500, 
            'Hg' : 1.700, 
            'Tl' : 1.550, 
            'Pb' : 1.540, 
            'Bi' : 1.540, 
            'Po' : 1.680, 
            'At' : 1.700, 
            'Rn' : 2.400, 
            'Fr' : 2.000, 
            'Ra' : 1.900, 
            'Ac' : 1.880, 
            'Th' : 1.790, 
            'Pa' : 1.610, 
            'U'  : 1.580, 
            'Np' : 1.550, 
            'Pu' : 1.530, 
            'Am' : 1.510, 
            'Cm' : 1.500, 
            'Bk' : 1.500, 
            'Cf' : 1.500, 
            'Es' : 1.500, 
            'Fm' : 1.500, 
            'Md' : 1.500, 
            'No' : 1.500, 
            'Lr' : 1.500, 
            'Rf' : 1.600, 
            'Db' : 1.600, 
            'Sg' : 1.600, 
            'Bh' : 1.600, 
            'Hs' : 1.600, 
            'Mt' : 1.600, 
            }
        
        # Ionic radii, stolen from Jmol
        self.IonicRadius = {
            'H1-'  : 1.540, 
            'Li1+' : 0.680,
            'Be1+' : 0.440,
            'Be2+' : 0.350,
            'B1+'  : 0.350,
            'B3+'  : 0.230,
            'C4-'  : 2.600, 
            'C4+'  : 0.160,
            'N3-'  : 1.710, 
            'N1+'  : 0.680,
            'N3+'  : 0.160,
            'N5+'  : 0.130,
            'O2-'  : 1.360,
            'O1-'  : 0.680,
            'O1+'  : 0.220,
            'O6+'  : 0.090, 
            'F1-'  : 1.330, 
            'F7+'  : 0.080, 
            'Ne1+' : 1.120,
            'Na1+' : 0.970, 
            'Mg1+' : 0.820, 
            'Mg2+' : 0.660, 
            'Al3+' : 0.510, 
            'Si4-' : 2.710,
            'Si1-' : 3.840,
            'Si1+' : 0.650, 
            'Si4+' : 0.420, 
            'P3-'  : 2.120, 
            'P3+'  : 0.440, 
            'P5+'  : 0.350, 
            'S2-'  : 1.840, 
            'S2+'  : 2.190,
            'S4+'  : 0.370, 
            'S6+'  : 0.300, 
            'Cl1-' : 1.810, 
            'Cl4+' : 0.340, 
            'Cl7+' : 0.270,  
            'Ar1+' : 1.540, 
            'K1+'  : 1.330, 
            'Ca1+' : 1.180, 
            'Ca2+' : 0.990,  
            'Sc3+' : 0.732,  
            'Ti1+' : 0.960,  
            'Ti2+' : 0.940,  
            'Ti3+' : 0.760,  
            'Ti4+' : 0.680,  
            'V2+'  : 0.880,  
            'V3+'  : 0.740,  
            'V4+'  : 0.630,  
            'V5+'  : 0.590,  
            'Cr1+' : 0.810,  
            'Cr2+' : 0.890,  
            'Cr3+' : 0.630,  
            'Cr6+' : 0.520,  
            'Mn2+' : 0.800,  
            'Mn3+' : 0.660,  
            'Mn4+' : 0.600,  
            'Mn7+' : 0.460,  
            'Fe2+' : 0.740,  
            'Fe3+' : 0.640,  
            'Co2+' : 0.720,  
            'Co3+' : 0.630,  
            'Ni2+' : 0.690,  
            'Cu1+' : 0.960,  
            'Cu2+' : 0.720,  
            'Zn1+' : 0.880,  
            'Zn2+' : 0.740,  
            'Ga1+' : 0.810,  
            'Ga3+' : 0.620,  
            'Ge4-' : 2.720, 
            'Ge2+' : 0.730,  
            'Ge4+' : 0.530,  
            'As3-' : 2.220, 
            'As3+' : 0.580,  
            'As5+' : 0.460,  
            'Se2-' : 1.980,
            'Se1-' : 2.320,
            'Se1+' : 0.660,  
            'Se4+' : 0.500,  
            'Se6+' : 0.420,  
            'Br1-' : 1.960, 
            'Br5+' : 0.470,  
            'Br7+' : 0.390,  
            'Rb1+' : 1.470, 
            'Sr2+' : 1.120, 
            'Y3+'  : 0.893,  
            'Zr1+' : 1.090, 
            'Zr4+' : 0.790,  
            'Nb1+' : 1.000, 
            'Nb4+' : 0.740,  
            'Nb5+' : 0.690,  
            'Mo1+' : 0.930,  
            'Mo4+' : 0.700,  
            'Mo6+' : 0.620,  
            'Tc7+' : 0.979,  
            'Ru4+' : 0.670,  
            'Rh3+' : 0.680,  
            'Pd2+' : 0.800,  
            'Pd4+' : 0.650,  
            'Ag1+' : 1.260, 
            'Ag2+' : 0.890,  
            'Cd1+' : 1.140, 
            'Cd2+' : 0.970,  
            'In3+' : 0.810,  
            'Sn4-' : 2.940, 
            'Sn1-' : 3.700, 
            'Sn2+' : 0.930,  
            'Sn4+' : 0.710,  
            'Sb3-' : 2.450, 
            'Sb3+' : 0.760,  
            'Sb5+' : 0.620,  
            'Te2-' : 2.110, 
            'Te1-' : 2.500, 
            'Te1+' : 0.820,  
            'Te4+' : 0.700,  
            'Te6+' : 0.560,  
            'I1-'  : 2.200,
            'I5+'  : 0.620,  
            'I7+'  : 0.500,  
            'Cs1+' : 1.670, 
            'Ba1+' : 1.530, 
            'Ba2+' : 1.340, 
            'La1+' : 1.390, 
            'La3+' : 1.016, 
            'Ce1+' : 1.270, 
            'Ce3+' : 1.034, 
            'Ce4+' : 0.920,  
            'Pr3+' : 1.013, 
            'Pr4+' : 0.900,  
            'Nd3+' : 0.995,  
            'Pm3+' : 0.979,  
            'Sm3+' : 0.964,  
            'Eu2+' : 1.090, 
            'Eu3+' : 0.950,  
            'Gd3+' : 0.938,  
            'Tb3+' : 0.923,  
            'Tb4+' : 0.840,  
            'Dy3+' : 0.908,  
            'Ho3+' : 0.894,  
            'Er3+' : 0.881,  
            'Tm3+' : 0.870,  
            'Yb2+' : 0.930,  
            'Yb3+' : 0.858,  
            'Lu3+' : 0.850,  
            'Hf4+' : 0.780,  
            'Ta5+' : 0.680,  
            'W4+'  : 0.700,  
            'W6+'  : 0.620,  
            'Re4+' : 0.720,  
            'Re7+' : 0.560,  
            'Os4+' : 0.880,  
            'Os6+' : 0.690,  
            'Ir4+' : 0.680,  
            'Pt2+' : 0.800,  
            'Pt4+' : 0.650,  
            'Au1+' : 1.370, 
            'Au3+' : 0.850,  
            'Hg1+' : 1.270, 
            'Hg2+' : 1.100, 
            'Tl1+' : 1.470, 
            'Tl3+' : 0.950,  
            'Pb2+' : 1.200, 
            'Pb4+' : 0.840,  
            'Bi1+' : 0.980,  
            'Bi3+' : 0.960,  
            'Bi5+' : 0.740,  
            'Po6+' : 0.670,  
            'At7+' : 0.620,  
            'Fr1+' : 1.800, 
            'Ra2+' : 1.430, 
            'Ac3+' : 1.180, 
            'Th4+' : 1.020, 
            'Pa3+' : 1.130, 
            'Pa4+' : 0.980,  
            'Pa5+' : 0.890,  
            'U4+'  : 0.970,  
            'U6+'  : 0.800,  
            'Np3+' : 1.100, 
            'Np4+' : 0.950,  
            'Np7+' : 0.710,  
            'Pu3+' : 1.080, 
            'Pu4+' : 0.930,  
            'Am3+' : 1.070, 
            'Am4+' : 0.920
            }

        # EMTO element configurations (Couldn't think of any way to generate these on the fly...)
        self.emtoelements ={
            "Va":
            "Iz=   0 Norb=  0 Ion=  0 Config= 1s0 \n\
n      1\n\
Kappa -1\n\
Occup  0\n\
Valen  1\n",
            "Em":
            "Iz=   0 Norb=  0 Ion=  0 Config= 1s0 \n\
n      1\n\
Kappa -1\n\
Occup  0\n\
Valen  1\n",
            "H":
            "Iz=   1 Norb=  1 Ion=  0 Config= 1s1\n\
n      1\n\
Kappa -1\n\
Occup  1\n\
Valen  1\n",
            "D":
            "Iz=   1 Norb=  1 Ion=  0 Config= 1s1\n\
n      1\n\
Kappa -1\n\
Occup  1\n\
Valen  1\n",
            "He":
            "Iz=   2 Norb=  1 Ion=  0 Config= 1s2\n\
n      1\n\
Kappa -1\n\
Occup  2\n\
Valen  1\n",
            "Li":
            "Iz=   3 Norb=  2 Ion=  0 Config= 2s1\n\
n      1  2\n\
Kappa -1 -1\n\
Occup  2  1\n\
Valen  0  1\n",
            "Be":
            "Iz=   4 Norb=  2 Ion=  0 Config= 2s2\n\
n      1  2\n\
Kappa -1 -1\n\
Occup  2  2\n\
Valen  0  1\n",
            "B":
            "Iz=   5 Norb=  3 Ion=  0 Config= 2s1_2p1\n\
n      1  2  2\n\
Kappa -1 -1  1\n\
Occup  2  2  1\n\
Valen  0  1  1\n",
            "C":
            "Iz=   6 Norb=  3 Ion=  0 Config= 2s2 2p2\n\
n      1  2  2\n\
Kappa -1 -1  1\n\
Occup  2  2  2\n\
Valen  0  1  1\n",
            "N":
            "Iz=   7 Norb=  4 Ion=  0 Config= 2p3\n\
n      1  2  2  2\n\
Kappa -1 -1  1 -2\n\
Occup  2  2  2  1\n\
Valen  0  0  1  1\n",
            "O":
            "Iz=   8 Norb=  4 Ion=  0 Config= 2s2_2p4\n\
n      1  2  2  2\n\
Kappa -1 -1  1 -2\n\
Occup  2  2  2  2\n\
Valen  0  1  1  1\n",
            "O-2":
            "Iz=   8 Norb=  4 Ion= -2 Config= 2p6\n\
n      1  2  2  2\n\
Kappa -1 -1  1 -2\n\
Occup  2  2  2  4\n\
Valen  0  0  1  1\n",
            "F":
            "Iz=   9 Norb=  4 Ion=  0 Config= 2s2_2p5\n\
n      1  2  2  2\n\
Kappa -1 -1  1 -2\n\
Occup  2  2  2  3\n\
Valen  0  1  1  1\n",
            "Ne":
            "Iz=  10 Norb=  4 Ion=  0 Config= 2s2_2p6\n\
n      1  2  2  2\n\
Kappa -1 -1  1 -2\n\
Occup  2  2  2  4\n\
Valen  0  1  1  1\n",
            "Na":
            "Iz=  11 Norb=  5 Ion=  0 Config= 3s1\n\
n      1  2  2  2  3\n\
Kappa -1 -1  1 -2 -1\n\
Occup  2  2  2  4  1\n\
Valen  0  0  0  0  1\n",
            "Mg":
            "Iz=  12 Norb=  5 Ion=  0 Config= 3s2\n\
n      1  2  2  2  3\n\
Kappa -1 -1  1 -2 -1\n\
Occup  2  2  2  4  2\n\
Valen  0  0  0  0  1\n",
            "Al":
            "Iz=  13 Norb=  6 Ion=  0 Config= 3s2_3p1\n\
n      1  2  2  2  3  3\n\
Kappa -1 -1  1 -2 -1  1\n\
Occup  2  2  2  4  2  1\n\
Valen  0  0  0  0  1  1\n",
            "Si":
            "Iz=  14 Norb=  6 Ion=  0 Config= 3s2_3p2\n\
n      1  2  2  2  3  3\n\
Kappa -1 -1  1 -2 -1  1\n\
Occup  2  2  2  4  2  2\n\
Valen  0  0  0  0  1  1\n",
            "P":
            "Iz=  15 Norb=  7 Ion=  0 Config= 3s2_3p3\n\
n      1  2  2  2  3  3  3\n\
Kappa -1 -1  1 -2 -1  1 -2\n\
Occup  2  2  2  4  2  2  1\n\
Valen  0  0  0  0  1  1  1\n",
            "S":
            "Iz=  16 Norb=  7 Ion=  0 Config= 3s2_3p4\n\
n      1  2  2  2  3  3  3\n\
Kappa -1 -1  1 -2 -1  1 -2\n\
Occup  2  2  2  4  2  2  2\n\
Valen  0  0  0  0  1  1  1\n",
            "Cl":
            "Iz=  17 Norb=  7 Ion=  0 Config= 3s2_3p5\n\
n      1  2  2  2  3  3  3\n\
Kappa -1 -1  1 -2 -1  1 -2\n\
Occup  2  2  2  4  2  2  3\n\
Valen  0  0  0  0  1  1  1\n",
            "Ar":
            "Iz=  18 Norb=  7 Ion=  0 Config= 3s2_3p6\n\
n      1  2  2  2  3  3  3\n\
Kappa -1 -1  1 -2 -1  1 -2\n\
Occup  2  2  2  4  2  2  4\n\
Valen  0  0  0  0  1  1  1\n",
            "K":
            "Iz=  19 Norb=  8 Ion=  0 Config 4s1\n\
n      1  2  2  2  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  1\n\
Valen  0  0  0  0  0  0  0  1\n",
            "Ca":
            "Iz=  20 Norb=  8 Ion=  0 Config= 4s2\n\
n      1  2  2  2  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  2\n\
Valen  0  0  0  0  0  0  0  1\n",
            "Sc":
            "Iz=  21 Norb=  9 Ion=  0 Config= 3d1_4s2\n\
n      1  2  2  2  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  1  1\n",
            "Ti":
            "Iz=  22 Norb=  9 Ion=  0 Config= 3d2_4s2\n\
n      1  2  2  2  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  2  2\n\
Valen  0  0  0  0  0  0  0  1  1\n",
            "V":
            "Iz=  23 Norb=  9 Ion=  0 Config= 3d3_4s2\n\
n      1  2  2  2  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  3  2\n\
Valen  0  0  0  0  0  0  0  1  1\n",
            "Cr":
            "Iz=  24 Norb=  9 Ion=  0 Config= 3d4_4s2\n\
n      1  2  2  2  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  2\n\
Valen  0  0  0  0  0  0  0  1  1\n",
            "Mn":
            "Iz=  25 Norb= 10 Ion=  0 Config= 3d5_4s2\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  1  2\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Fe":
            "Iz=  26 Norb= 10 Ion=  0 Config= 3d7_4s1\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  3  1\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Co":
            "Iz=  27 Norb= 10 Ion=  0 Config= 3d7_4s2\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  3  2\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Ni":
            "Iz=  28 Norb= 10 Ion=  0 Config= 3d8_4s2\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  4  2\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Cu":
            "Iz=  29 Norb= 10 Ion=  0 Config= 3d10_4s1\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  1\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Zn":
            "Iz=  30 Norb= 10 Ion=  0 Config= 3d10_4s2\n\
n      1  2  2  2  3  3  3  3  3  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2\n\
Valen  0  0  0  0  0  0  0  1  1  1\n",
            "Ga":
            "Iz=  31 Norb= 11 Ion=  0 Config= 3d10_4s2_4p1\n\
n      1  2  2  2  3  3  3  3  3  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  1\n\
Valen  0  0  0  0  0  0  0  1  1  1  1\n",
            "Ge":
            "Iz=  32 Norb= 11 Ion=  0 Config= 4s2_4p2\n\
n      1  2  2  2  3  3  3  3  3  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  1  1\n",
            "As":
            "Iz=  33 Norb= 12 Ion=  0 Config= 3d10_4s2_4p3\n\
n      1  2  2  2  3  3  3  3  3  4  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  1\n\
Valen  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Se":
            "Iz=  34 Norb= 12 Ion=  0 Config= 3d10_4s2_4p4\n\
n      1  2  2  2  3  3  3  3  3  4  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  2\n\
Valen  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Br":
            "Iz=  35 Norb= 12 Ion=  0 Config= 3d10_4s2_4p5\n\
n      1  2  2  2  3  3  3  3  3  4  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  3\n\
Valen  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Kr":
            "Iz=  36 Norb= 12 Ion=  0 Config= 3d10_4s2_4p6\n\
n      1  2  2  2  3  3  3  3  3  4  4  4\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4\n\
Valen  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Rb":
            "Iz=  37 Norb= 13 Ion=  0 Config= 5s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "Sr":
            "Iz=  38 Norb= 13 Ion=  0 Config= 5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "Y":
            "Iz=  39 Norb= 14 Ion=  0 Config= 4d1_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Zr":
            "Iz=  40 Norb= 14 Ion=  0 Config= 4d2_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Nb":
            "Iz=  41 Norb= 14 Ion=  0 Config= 4d3_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  3  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Mo":
            "Iz=  42 Norb= 14 Ion=  0 Config= 4d4_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Tc":
            "Iz=  43 Norb= 15 Ion=  0 Config= 4d5_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Ru":
            "Iz=  44 Norb= 15 Ion=  0 Config= 4d6_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Rh":
            "Iz=  45 Norb= 15 Ion=  0 Config= 4d7_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  3  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Pd":
            "Iz=  46 Norb= 15 Ion=  0 Config= 4d8_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Ag":
            "Iz=  47 Norb= 15 Ion=  0 Config= 4d10_5s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Cd":
            "Iz=  48 Norb= 15 Ion=  0 Config= 4d10_5s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "In":
            "Iz=  49 Norb= 16 Ion=  0 Config= 4d10_5s2_5p1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1\n",
            "Sn":
            "Iz=  50 Norb= 16 Ion=  0 Config= 4d10_5s2_5p2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1\n",
            "Sb":
            "Iz=  51 Norb= 17 Ion=  0 Config= 4d10_5s2_5p3\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Te":
            "Iz=  52 Norb= 17 Ion=  0 Config= 4d10_5s2_5p4\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "I":
            "Iz=  53 Norb= 17 Ion=  0 Config= 4d10_5s2_5p5\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  3\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Xe":
            "Iz=  54 Norb= 17 Ion=  0 Config= 4d10_5s2_5p6\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  4\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Cs":
            "Iz=  55 Norb= 18 Ion=  0 Config= 6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  4  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "Ba":
            "Iz=  56 Norb= 18 Ion=  0 Config= 6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "La":
            "Iz=  57 Norb= 19 Ion=  0 Config= 5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Ce":
            "Iz=  58 Norb= 20 Ion=  0 Config= 4f1_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  1  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "Pr":
            "Iz=  59 Norb= 20 Ion=  0 Config= 4f2_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  2  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Nd":
            "Iz=  60 Norb= 20 Ion=  0 Config= 4f3_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  3  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Pm":
            "Iz=  61 Norb= 20 Ion=  0 Config= 4f4_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  4  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Sm":
            "Iz=  62 Norb= 20 Ion=  0 Config= 4f5_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  5  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Eu":
            "Iz=  63 Norb= 21 Ion=  0 Config= 4f7_5d1_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  1  2  2  4  1  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Gd":
            "Iz=  64 Norb= 21 Ion=  0 Config= 4f7_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  1  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Tb":
            "Iz=  65 Norb= 21 Ion=  0 Config= 4f8_5d2_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  2  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Dy":
            "Iz=  66 Norb= 21 Ion=  0 Config= 4f9_5d1_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  3  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Ho":
            "Iz=  67 Norb= 21 Ion=  0 Config= 4f10_5d1_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  4  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Er":
            "Iz=  68 Norb= 21 Ion=  0 Config= 4f11_5d1_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  5  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Tm":
            "Iz=  69 Norb= 21 Ion=  0 Config= 4f12_5d1_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  6  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Yb":
            "Iz=  70 Norb= 21 Ion=  0 Config= 4f14_5d1_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  1  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Lu":
            "Iz=  71 Norb= 21 Ion=  0 Config= 5d1_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Hf":
            "Iz=  72 Norb= 21 Ion=  0 Config= 5d2_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Ta":
            "Iz=  73 Norb= 21 Ion=  0 Config= 5d3_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  3  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "W":
            "Iz=  74 Norb= 21 Ion=  0 Config= 5d4_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Re":
            "Iz=  75 Norb= 22 Ion=  0 Config= 5d5_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  1  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Os":
            "Iz=  76 Norb= 22 Ion=  0 Config= 5d6_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Ir":
            "Iz=  77 Norb= 22 Ion=  0 Config= 5d7_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  3  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Pt":
            "Iz=  78 Norb= 22 Ion=  0 Config= 5d8_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Au":
            "Iz=  79 Norb= 22 Ion=  0 Config= 5d10_6s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Hg":
            "Iz=  80 Norb= 22 Ion=  0 Config= 5d10_6s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1\n",
            "Tl":
            "Iz=  81 Norb= 23 Ion=  0 Config= 5d10_6s2_6p1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1\n",
            "Pb":
            "Iz=  82 Norb= 23 Ion=  0 Config= 6s2_6p2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1\n",
            "Bi":
            "Iz=  83 Norb= 24 Ion=  0 Config= 5d10_6s2_6p3\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Po":
            "Iz=  84 Norb= 24 Ion=  0 Config= 5d10_6s2_6p4\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "At":
            "Iz=  85 Norb= 24 Ion=  0 Config= 5d10_6s2_6p5\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  3\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Rn":
            "Iz=  86 Norb= 24 Ion=  0 Config= 5d10_6s2_6p6\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  4\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1\n",
            "Fr":
            "Iz=  87 Norb= 25 Ion=  0 Config= 7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  4  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "Ra":
            "Iz=  88 Norb= 25 Ion=  0 Config= 7s2\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  4  2\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1\n",
            "Ac":
            "Iz=  89 Norb= 26 Ion=  0 Config= 6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Th":
            "Iz=  90 Norb= 26 Ion=  0 Config= 6d3_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  4  3  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1\n",
            "Pa":
            "Iz=  91 Norb= 27 Ion=  0 Config= 5f1_6d3_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  1  2  2  4  3  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "U":
            "Iz=  92 Norb= 27 Ion=  0 Config= 5f2_6d3_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  2  2  2  4  3  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "Np":
            "Iz=  93 Norb= 27 Ion=  0 Config= 5f4_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  4  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "Pu":
            "Iz=  94 Norb= 27 Ion=  0 Config= 5f5_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  5  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "Am":
            "Iz=  95 Norb= 27 Ion=  0 Config= 5f6_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  6  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  1\n",
            "Cm":
            "Iz=  96 Norb= 28 Ion=  0 Config= 5f7_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  6  1  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  0  0  0  1  1\n",
            "Bk":
            "Iz=  97 Norb= 28 Ion=  0 Config= 5f8_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  6  2  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  0  0  0  1  1\n",
            "Cf":
            "Iz=  98 Norb= 28 Ion=  0 Config= 5f9_6d2_7s1\n\
n      1  2  2  2  3  3  3  3  3  4  4  4  4  4  4  4  5  5  5  5  5  5  5  6  6  6  6  7\n\
Kappa -1 -1  1 -2 -1  1 -2  2 -3 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -3  3 -4 -1  1 -2  2 -1\n\
Occup  2  2  2  4  2  2  4  4  6  2  2  4  4  6  6  8  2  2  4  4  6  6  3  2  2  4  2  1\n\
Valen  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  0  0  0  1  1\n",
            }

