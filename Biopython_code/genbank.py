# Import the Entrez module from Biopython for accessing NCBI
from Bio import Entrez

# Always set your email before using Entrez (required by NCBI)
Entrez.email = "yashhon47@gmail.com"

# Define the search term
query = "CRISPR"  # Note: Corrected spelling from "CRISPER" to "CRISPR"

# Use Entrez.esearch to search PubMed with the query
handle = Entrez.esearch(db="pubmed", term=query, retmax=10)

# Parse the search results
record = Entrez.read(handle)
handle.close()

# Print the list of PubMed IDs (PMIDs) found
print("PubMed IDs:", record["IdList"])
