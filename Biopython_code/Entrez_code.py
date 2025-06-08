# Import Entrez module from Biopython for accessing NCBI databases
from Bio import Entrez

# Define a function to fetch nucleotide sequence from NCBI using an accession ID
def fetch_sequence(accession_id):
    Entrez.email = "pranotidhondge21@gmail.com"

    # Use Entrez.efetch to get the record in GenBank format
    handle = Entrez.efetch(
        db="nucleotide",         
        id=accession_id,         
        rettype="gb",            
        retmode="text"           
    )

    # Read and print the GenBank sequence data
    sequence_data = handle.read()
    print(sequence_data)

# Accession ID of the target sequence (change this as needed)
accession_id = "NC_000852"

fetch_sequence(accession_id)
