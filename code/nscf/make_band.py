import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from zincblende_struct_makers import make_bulk_GaAs
from kpts_makers import make_diamond_bands
from param_makers import make_scf_param
from bash_makers import make_bash_niagara 

make_diamond_bands('KPTS')
make_bulk_GaAs('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10,calculation = 'bands', ecutwfc = 60, ecutrho = 240, nat = 2, ntyp =2, nbnd = 16)
os.system('cat PARAMS STRUCT KPTS >> band.in')
os.system('dos2unix band.in')

make_bash_niagara('band.sh', qe_inputfile = 'band.in', qe_outputfile = 'band.out', job_name = 'GaAs_bands', time = '00:30:00')
os.system('sbatch band.sh')

os.system('rm -f PARAMS STRUCT KPTS')


