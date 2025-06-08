# Import the Entrez module from Biopython for accessing NCBI
from Bio import Entrez

Entrez.email = "pranotidhondge21@gmail.com"

# Define the search term
query = "CRISPR" 

# Use Entrez.esearch to search PubMed with the query
handle = Entrez.esearch(db="pubmed", term=query, retmax=10)

# Parse the search results
record = Entrez.read(handle)
handle.close()

# Print the list of PubMed IDs (PMIDs) found
print("PubMed IDs:", record["IdList"])
