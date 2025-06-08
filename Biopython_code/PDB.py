# Import PDBList class from Biopython's PDB module
from Bio.PDB import PDBList

# Define a function to fetch and download a PDB structure by its ID
def fetch_pdb_structure(pdb_id):
   
    pdbl = PDBList()

    # Retrieve the PDB file in .pdb format
    pdbl.retrieve_pdb_file(pdb_id, file_format="pdb", pdir=".")

    print(f"Structure {pdb_id.upper()} downloaded successfully.")

# Example PDB ID (you can replace this with any valid PDB ID)
pdb_id = "1A8O"
fetch_pdb_structure(pdb_id)
