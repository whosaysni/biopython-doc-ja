import pykf
import sys

infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

outfile.write(pykf.tosjis(infile.read(),pykf.EUC).replace("EUC-JP", "shift_jis"))

infile.close()
outfile.close()


