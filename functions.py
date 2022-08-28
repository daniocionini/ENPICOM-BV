#extract the sequences
def filter_nuc(letter):
    #filter to keep Nucleotides and ">" only
    nuc = ['A', 'T', 'G', 'C', '>']
    return True if letter in nuc else False
  
  
  
  
#count the nucleotides by base
def nucleotide_count(seq):
    nucl_list = []
    a = seq.count('A')
    nucl_list.append('A:')
    nucl_list.append(a)
    u = seq.count('U')
    nucl_list.append('U:')
    nucl_list.append(u)
    g = seq.count('G')
    nucl_list.append('G:')
    nucl_list.append(g)
    c = seq.count('C')
    nucl_list.append('C:')
    nucl_list.append(c)
    return nucl_list
  
  
  
  
#compute maximum matching
def maximum_matching(nuc):
    if a <= u in nuc:    
        match_au = a
    if a >= u in nuc:
        match_au = u
    if g <= c in nuc:    
        match_gc = g
    if g >= c in nuc:
        match_gc = c
    result = match_au + match_gc
    return result
