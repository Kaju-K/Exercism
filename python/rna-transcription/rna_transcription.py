def to_rna(dna_strand):
    transcription = str.maketrans("ACTG", "UGAC")
    dna_strand = dna_strand.translate(transcription)
    return dna_strand
