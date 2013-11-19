from pyphylogenomics import NGS
import sys
import re
import subprocess


fastq_file = sys.argv[1].strip()
min_number_reads = sys.argv[2].strip()

cmd = "grep -c '^@' " + fastq_file
p = subprocess.check_output(cmd, shell=True)

if int(p.strip()) > int(min_number_reads):
    index_length = 1
    min_quality = 20
    percentage = 90
    min_length = 60

    NGS.assembly(fastq_file, index_length, min_quality, percentage, min_length)
