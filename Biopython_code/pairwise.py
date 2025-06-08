# Import Biopython's pairwise2 module and format_alignment for displaying results
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Define two DNA sequences to be aligned
seq1 = "ATGGCATTCCGGAATGCCG"
seq2 = "ATGGACATCATTGGCTGAA"

# Perform global alignment using match=1, mismatch=0 (globalxx scoring)
alignments = pairwise2.align.globalxx(seq1, seq2)

for alignment in alignments:
    print(format_alignment(*alignment))
