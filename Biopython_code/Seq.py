# Import the Seq object from Biopython for working with sequences
from Bio.Seq import Seq

# Define a function to translate DNA into a protein sequence
def translate_dna_to_protein(dna_sequence):
    
    # Create a Seq object and perform translation
    protein_sequence = Seq(dna_sequence).translate()

    print(f"Protein Sequence: {protein_sequence}")

    return protein_sequence 

# Example DNA sequence 
dna_sequence = "ATGCTGATCTGCGGCTGCATGATGCATCGCTACGATAGCATGCCGAT"

# Call the function and store the result
protein_sequence = translate_dna_to_protein(dna_sequence)
