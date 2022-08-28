# import necessary libraries
from functions import *

# import the file
print('Paste input file directory including file-name to import')
file_import_directory = input()#HERE THE DIRECTORY


# read the file and assert it is a valid FASTA
seq_orig = open(file_import_directory, "r")
seq = seq_orig.read()
assert ">" in seq, "should be a valid FASTA file" # assert the imported file is a FASTA file


# extract the sequences
filtered_seq = filter(filter_nuc, seq)
new_seq = tuple(filtered_seq)
seq = ' '.join(new_seq)
seq = seq.replace(" ", "")
seq = seq.replace('>', '')
print(seq)


# count nucleotides by base
nucl_list = nucleotide_count(rna_seq)
print(nucl_list)


# compute Maximum Matching
result = maximum_matching(nucl_list)    
print(result)    
    
