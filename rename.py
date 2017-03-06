# email: barajasg@unican.es

import os
import glob

dirs = glob.glob("*")
for dirname in dirs:
    try:
        dn = float(dirname)
        new_dn = '{0:06.2f}'.format(dn)
        print dirname, "->", new_dn
        os.rename(dirname, new_dn)
    except:
        pass
