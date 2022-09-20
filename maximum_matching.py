def filter_nuc(letter):
    #this function is used to filter out the unimportant data to keep Nucleotides and ">" only from the RNA sequence
    nuc = ['A', 'U', 'G', 'C', '>']
    return True if letter in nuc else False


def nuc_class(seq):
    # this function calculates the number of identical nucleotides on the RNA sequence
    a = 0
    u = 0
    g = 0
    c = 0
    for i in seq:
        if i == "A":
            a += 1
        if i == "U":
            u += 1
        if i == "G":
            g += 1
        if i == "C":
            c += 1
    return a, u, g, c #the output is the number of A, U, G and C nucleotides respectively


def max_match(x):
    # this function computes the maximal matchings of the RNA sequence
    a,u,g,c = nuc_class(x) #precedent function is computed first
    #the matchings of nucleotide pairs are computed using the precedent function's output
    if a <= u:
        au = a
    if a > u:
        au = u
    if g <= c:
        gc = g
    if g > c:
        gc = c
    #the global total matching of the RNA sequence is computed by adding A-U and G-C pairs
    total_matching = au + gc
    print(total_matching)


    

# CHANGE__ the import directory is necessary to import a FASTA file
file_import_directory = "IMPORT_DIRECTORY"

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

# compute the maximal matching for the imported RNA sequence
max_match(seq)
