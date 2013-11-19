from pyphylogenomics import NGS;
import sys

blast_table = sys.argv[1].strip()
ion_file    = "data/modified/wrk_ionfile.fastq";
NGS.parse_blast_results(blast_table, ion_file);
