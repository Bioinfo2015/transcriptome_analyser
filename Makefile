analysis: Bombyx_exons.fas data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq data/modified/wrk_ionfile_blastn_out.csv output/_re*fastq output/gene*assembled.fasta data/modified/wrk_ionfile_blast_out_filtered.csv

Bombyx_exons.fas: silkgenome.fa silkcds.fa OrthoDB6_Arthropoda_tabtext
	python code/search_genes_from_Bmori.py
	
#SRR1021599.fastq: SRR1021599.sra
	# convert sra file to fastq
	#~/bin/sra/fastq-dump SRR1021599.sra

data/modified/wrk_ionfile.fasta data/modified/wrk_ionfile.fastq: SRR1021599.fastq  code/prepare_data.py
	python code/prepare_data.py $<

data/modified/wrk_ionfile_blastn_out.csv: code/blast_against_illumina_reads.py  Bombyx_exons.fas data/modified/wrk_ionfile.fasta
	python code/blast_against_illumina_reads.py data/modified/wrk_ionfile.fasta Bombyx_exons.fas

data/modified/wrk_ionfile_blast_out_filtered.csv: data/modified/wrk_ionfile_blastn_out.csv
	# use only hits that have more than 100bp in alignment length
	cat data/modified/wrk_ionfile_blastn_out.csv |  awk -F , '{ if( $$4 > 100) { print $$0}}' > data/modified/wrk_ionfile_blast_out_filtered.csv

output/_re%csv output/_re%fastq output/gene%fastq: data/modified/wrk_ionfile_blast_out_filtered.csv data/modified/wrk_ionfile.fastq
	python code/parse_blast_results.py data/modified/wrk_ionfile_blast_out_filtered.csv

reads_per_bin.txt: output/gene_BGIBMGA0*fastq 
	ls output/gene_BGIBMGA0* | xargs grep -c '^@' | awk -F ':' '{print $$(NF)}' > reads_per_bin.txt

# assembly, use parallel!
output/gene%assembled.fasta: output/gene_BGIBMGA0%fastq code/assembly.py
	ls output/gene_BGIBMGA0*.fastq | xargs -I {} python code/assembly.py {} 200


