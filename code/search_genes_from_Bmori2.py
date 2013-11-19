import sys

def copies_per_gene(in_file):
    '''
    \* *Internal function* \*

    Creates a dictionary with the number of copies per gene and per species.
    
    The dictionary has as keys tuples=(species_name, gene_name) and
    values=integer that represent the number of copies of that gene
    in the species.
    '''

    dictio = {}

    global genes, species

    in_file = open(in_file, "rb");
    in_file.next() # skip header
    for line in in_file:
        line = line.split('\t')
        specie = line[4]
        gene = line[3]
        o_id = line[1]
        if (specie,gene,o_id) not in dictio:
            dictio[(specie,gene,o_id)] = 1
        else:
            dictio[(specie,gene,o_id)] += 1

    in_file.close()

    return dictio


    
def single_copy_genes(in_file, species_name):
    '''
    Returns a list of single-copy genes for a species given by user.

    The species name should be in the same format as stated in the input 
    file *in_file*.
    '''

    print "\n";
    print "Looking for single-copy genes for species "+ str(species_name) +":";
    
    dictio = copies_per_gene(in_file)

    ids = dict()
    for key in dictio:
        if species_name in key and dictio[key] == 1:
            ortho_id = key[2]
            gene = key[1]

            if ortho_id not in ids:
                ids[ ortho_id ] = [ gene ]
            else:
                ids[ ortho_id ].append(gene)
        else:
            pass

    genes = list()
    for k, v in ids.iteritems():
        # we want only single copy genes
        if len(v) < 2:
            genes.append(v[0])
    print "Found " + str(len(genes)) + " genes.";
    return genes;

print len(single_copy_genes(sys.argv[1].strip(), sys.argv[2].strip()))
