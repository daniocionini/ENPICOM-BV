
def filter_nuc(letter):
    #extract the sequences by filtering to keep Nucleotides and ">" only
    nuc = ['A', 'T', 'G', 'C', '>']
    return True if letter in nuc else False


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
seq = seq.split('>')

#exclude repeated sequences
seq = [i for i in seq if seq.count(i) ==1]


def comparison(inp):
    #sort the list into a dictionary for easier comparison between sequences
    dict = {}
    n = 0
    i = len(inp)
    while n < i:
        dict[inp[n]] = []
        for letter in inp[n]:
            dict[inp[n]].append(letter)
        n += 1

    #assign sequences to a variable
    one = dict[inp[1]]
    two = dict[inp[2]]
    thr = dict[inp[3]]
    fou = dict[inp[4]]
    fiv = dict[inp[5]]
    six = dict[inp[6]]
    sev = dict[inp[7]]

    #first comparison iteration loop
    d = 0
    for (nn,mm) in zip(one, two):
        if nn != mm: #compute the comparison
            d += 1
    if d == 1:
        #if the principal variable confirms that there is a Hamming Distance of 1
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][2])

    d = 0
    for (nn,mm) in zip(one, thr):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][3])

    d = 0
    for (nn,mm) in zip(one, fou):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][4])

    d = 0
    for (nn,mm) in zip(one, fiv):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][5])

    d = 0
    for (nn,mm) in zip(one, six):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][6])

    d = 0
    for (nn,mm) in zip(one, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][1], '->',[key for key in dict.keys()][7])


    #second comparison iteration loop
    d = 0
    for (nn,mm) in zip(two, thr):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][2], '->',[key for key in dict.keys()][3])

    d = 0
    for (nn,mm) in zip(two, fou):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][2], '->',[key for key in dict.keys()][4])

    d = 0
    for (nn,mm) in zip(two, fiv):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][2], '->',[key for key in dict.keys()][5])

    d = 0
    for (nn,mm) in zip(two, six):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][2], '->',[key for key in dict.keys()][6])

    d = 0
    for (nn,mm) in zip(two, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][2], '->',[key for key in dict.keys()][7])

    #third comparison iteration loop
    d = 0
    for (nn,mm) in zip(thr, fou):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][3], '->',[key for key in dict.keys()][4])

    d = 0
    for (nn,mm) in zip(thr, fiv):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][3], '->',[key for key in dict.keys()][5])

    d = 0
    for (nn,mm) in zip(thr, six):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][3], '->',[key for key in dict.keys()][6])

    d = 0
    for (nn,mm) in zip(thr, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][3], '->',[key for key in dict.keys()][7])

    #fourth comparison iteration loop
    d = 0
    for (nn,mm) in zip(fou, fiv):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][4], '->',[key for key in dict.keys()][5])

    d = 0
    for (nn,mm) in zip(fou, six):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][4], '->',[key for key in dict.keys()][6])

    d = 0
    for (nn,mm) in zip(fou, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][4], '->',[key for key in dict.keys()][7])

    #fifth comparison iteration loop
    d = 0
    for (nn,mm) in zip(fiv, six):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][5], '->',[key for key in dict.keys()][6])

    d = 0
    for (nn,mm) in zip(fiv, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][5], '->',[key for key in dict.keys()][7])

    #sixth comparison iteration loop
    d = 0
    for (nn,mm) in zip(six, sev):
        if nn != mm:
            d += 1
    if d == 1:
        print([key for key in dict.keys()][6], '->',[key for key in dict.keys()][7])

    return





#compute the function for comparison of sequences within the created list
comparison(seq)
