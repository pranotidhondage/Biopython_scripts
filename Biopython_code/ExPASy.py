from Bio import ExPASy
from Bio import SwissProt

def fetch_protein(uniprot_id):
    
    # Fetch raw Swiss-Prot record from ExPASy
    handle = ExPASy.get_sprot_raw(uniprot_id)

    # Parse the SwissProt record using Biopython's SwissProt parser
    record = SwissProt.read(handle)

    # Print the description and amino acid sequence
    print(f"Description: {record.description}")
    print(f"Sequence: {record.sequence}")

# Example UniProt accession ID 
uniprot_id = "P12345"

# Call the function to fetch and print protein info
fetch_protein(uniprot_id)
