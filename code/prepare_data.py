from pyphylogenomics import NGS
import sys

ionfile = sys.argv[1].strip()
index_length = 0;
NGS.prepare_data(ionfile, index_length);
