import numpy as np

# import the sequence
def filter_nuc(letter):
    #extract the sequences by filtering to keep Nucleotides and ">" only
    nuc = ['A', 'T', 'G', 'C', '>']
    return True if letter in nuc else False


# CHANGE__ the import directory is necessary to import a FASTA file
file_import_directory = r"IMPORT_DIRECTORY"

# import the FASTA file and read through
seq_orig = open(file_import_directory, "r")
seq = seq_orig.read()
seq_id = seq # for ID extraction
assert ">" in seq, "should be a valid FASTA file" # assert the imported file is a FASTA file

# extract the sequences as 'seq'
filtered_seq = filter(filter_nuc, seq)
new_seq = tuple(filtered_seq)
seq = ' '.join(new_seq)
seq = seq.replace(" ", "")
seq = seq.split('>')

# save the sequences into different variables
non,seq_a,seq_b = seq


# create two matrices, one principal matrix of sequences lenght + 1
pr_matrix = np.zeros((len(seq_a)+1,len(seq_b)+1))
# one benchmark matrix of sequences lenght
benchmark_matrix = np.zeros((len(seq_a), len(seq_b)))

# set the scores necessary to fill the matrix
match = 1
mismatch = -1
gap = -2

# compute the benchmark matrix using set scores
for i in range(len(seq_a)):
    for j in range(len(seq_b)):
        if seq_a[i] == seq_b[j]:
            benchmark_matrix[i][j] = match
        else:
            benchmark_matrix[i][j] = mismatch


# Needleman_Wunsch algorithm to compute the principal matrix
for i in range(len(seq_a)+1):
    pr_matrix[i][0] = i * gap
for j in range(len(seq_b)+1):
    pr_matrix[0][j] = j * gap


for i in range(1, len(seq_a)+1):
    for j in range(1, len(seq_b)+1):
        pr_matrix[i][j] = max(pr_matrix[i-1][j-1]+benchmark_matrix[i-1][j-1],
                                pr_matrix[i-1][j]+gap,
                                pr_matrix[i][j-1]+gap)

# create variables for output storage
seq_a_out = ""
seq_b_out = ""

# set separate variables with sequences lenghts (necessary for the next loop)
len_seq_a = len(seq_a)
len_seq_b = len(seq_b)

# iterate through the matrix to compute match, mismatch or gap
while(len_seq_a > 0 and len_seq_b > 0):
    if (len_seq_a >0 and len_seq_b > 0 and pr_matrix[len_seq_a][len_seq_b] == pr_matrix[len_seq_a-1][len_seq_b-1] + benchmark_matrix[len_seq_a-1][len_seq_b-1]):
        seq_a_out = seq_a[len_seq_a-1] + seq_a_out
        seq_b_out = seq_b[len_seq_b-1] + seq_b_out

        len_seq_a = len_seq_a - 1
        len_seq_b = len_seq_b - 1

    elif(len_seq_a > 0 and pr_matrix[len_seq_a][len_seq_b] == pr_matrix[len_seq_a-1][len_seq_b] + gap):
        seq_a_out = seq_a[len_seq_a-1] + seq_a_out
        seq_b_out = "-" + seq_b_out

        len_seq_a = len_seq_a - 1
    else:
        seq_a_out = "-" + seq_a_out
        seq_b_out = seq_b[len_seq_b-1] + seq_b_out

        len_seq_b = len_seq_b - 1


# compute the outpout
print(seq_a_out)
print(seq_b_out)
