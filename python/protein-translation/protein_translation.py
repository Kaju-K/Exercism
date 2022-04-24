code = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine",
         "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
         "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine", "UGC": "Cysteine",
         "UGG": "Tryptophan"}

def proteins(strand):
    protein = []
    for i in range(len(strand)//3):
        codons = strand[3*i: 3*i + 3]
        if codons in code:
            protein.append(code.get(codons))
        else:
            break
    return protein
