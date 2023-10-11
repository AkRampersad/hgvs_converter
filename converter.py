from Bio import Entrez, SeqIO


def obtain_chromosome(transcript_id):
    Entrez.email = "akashjrampersad@gmail.com"

    handle = Entrez.efetch(db='nucleotide', id=transcript_id, rettype="gb", retmode='text')
    record = SeqIO.read(handle,'genbank')

    for feature in record.features:
        if "chromosome" in feature.qualifiers:
            chromosome = feature.qualifiers["chromosome"][0]
            return chromosome

    return None
print(obtain_chromosome("NM_001005405.2"))


