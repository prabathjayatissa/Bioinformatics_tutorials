# Bioinformatics Python Pipelines

This document provides an overview of the two Jupyter Notebooks designed for basic bioinformatics sequence analysis using **Biopython**.

## 1. DNA → Protein BLAST Pipeline

This notebook automates the process of taking a raw DNA sequence, querying it against the NCBI nucleotide database (BLASTn), translating it into a protein sequence, and then querying the resulting protein against the NCBI non-redundant protein database (BLASTp).

### Features
* **BLASTn (Nucleotide BLAST):** Searches the `nt` database to identify the origin or related sequences of the input DNA.
* **DNA Translation:** Safely pads the DNA sequence to a multiple of 3 (avoiding Biopython warnings) and translates it into an amino acid sequence.
* **BLASTp (Protein BLAST):** Searches the `nr` database to find homologous proteins.
* **Parsed Results:** Extracts and displays readable metrics for the top 5 hits, such as Length, Score, E-value, and Percent Identity.

### Dependencies
* `biopython` 
  * `Bio.Blast.NCBIWWW`
  * `Bio.Blast.NCBIXML`
  * `Bio.Seq.Seq`

---

## 2. Sequence Analysis & Alignment Pipeline

This notebook focuses on comparing two user-provided DNA sequences. It calculates foundational sequence statistics and performs a formal global sequence alignment to visualize and score their similarity.

### Features
* **Sequence Analytics:** Calculates the total length and **GC content** (percentage of Guanine and Cytosine) for each sequence using Biopython's modern `gc_fraction` utility.
* **Global Pairwise Alignment:** Uses Biopython's `PairwiseAligner` to globally align the two sequences.
* **Custom Scoring Matrix:** Applies a precise scoring mechanism:
  * Match: +2.0
  * Mismatch: -1.0
  * Gap Open: -0.5
  * Gap Extend: -0.1
* **Visual Output:** Prints the final alignment score and a visual representation of the best sequence match (showing gaps and matches).

### Dependencies
* `biopython`
  * `Bio.Seq.Seq`
  * `Bio.SeqUtils.gc_fraction`
  * `Bio.Align`

---

### Setup Instructions

To run these notebooks locally, ensure you have Biopython installed in your Python environment:
   








