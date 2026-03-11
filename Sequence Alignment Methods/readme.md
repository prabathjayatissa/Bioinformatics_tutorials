# DNA Sequence Assembly Using Overlap Detection

This repository demonstrates a simple Python implementation of **DNA sequence assembly** using an **overlap-based approach**. The goal is to reconstruct a longer DNA sequence from several shorter fragments by detecting overlapping regions between them.

This approach is conceptually similar to the **primer walking method** used in sequencing projects.

---

# Concept

DNA sequencing technologies often produce **short fragments of sequences** rather than the complete DNA molecule. These fragments usually share **overlapping regions** with each other.

By identifying these overlaps, we can merge fragments together and rebuild the original longer sequence.

The program in this repository performs the following tasks:

1. Compares the end of one DNA fragment with the beginning of the next.
2. Detects overlapping regions between sequences.
3. Merges sequences while keeping only **one copy of the overlapping region**.
4. Repeats the process until a final assembled DNA sequence is created.

---


# Python Implementation

```python
def find_overlap(seq1, seq2, min_overlap=10):
    for i in range(len(seq1)):
        overlap = seq1[i:]
        if seq2.startswith(overlap) and len(overlap) >= min_overlap:
            return overlap
    return ""

def assemble_sequences(seqs):
    assembled = seqs[0]

    for seq in seqs[1:]:
        overlap = find_overlap(assembled, seq)
        if overlap:
            assembled += seq[len(overlap):]
        else:
            assembled += seq

    return assembled

sequences = [
"ATGCTAGCTAGGCTAACCGTACGATCGTACGTTAGCTAGCTA",
"CGTACGTTAGCTAGCTAGGATCCGATCGATCGTTACGATCGA",
"ATCCGATCGATCGTTACGATCGATGCTAGCTAGGCTAGCTAA",
"GATGCTAGCTAGGCTAGCTAATCGGATCGATCGATCGTTAGC",
"TCGGATCGATCGATCGTTAGCTAGCTAGCTAACCGTACGTTA"
]

result = assemble_sequences(sequences)

print("Final DNA:")
print(result)
```

---

# How the Algorithm Works

## 1. Finding Overlapping Regions

The function `find_overlap()` checks whether the **end of the first sequence** overlaps with the **beginning of the second sequence**.

It:

* Iterates through positions in the first sequence
* Extracts possible overlapping substrings
* Checks if the second sequence starts with that substring
* Ensures the overlap is at least the specified **minimum overlap length**

Default minimum overlap length:

```
min_overlap = 10
```

This helps prevent very short accidental matches.

---

## 2. Assembling the Sequences

The function `assemble_sequences()` performs the actual assembly process.

Steps:

1. Start with the first sequence.
2. Compare it with the next sequence.
3. If an overlap is found:

   * Append only the **non-overlapping portion** of the next sequence.
4. If no overlap is found:

   * Append the full sequence.
5. Continue until all fragments are processed.

---

# Example Input

```
5 DNA fragments
```

Each fragment represents a piece of a longer DNA molecule.

---

# Example Output

```
Final DNA:
<assembled DNA sequence>
```

The resulting string represents the **merged DNA sequence** constructed from the overlapping fragments.

---

# Requirements

* Python 3.x
* No external libraries required

---

# Limitations

This example demonstrates a **basic educational implementation** and has several simplifications:

* Sequences are assumed to be in the correct order
* Only forward overlaps are considered
* No mismatch handling is implemented
* No reverse complement detection

In real genome assembly pipelines, more advanced algorithms such as:

* **De Bruijn graphs**
* **Overlap-layout-consensus methods**

are used.

---

# Educational Purpose

This code is intended for:

* learning basic **bioinformatics concepts**
* understanding **sequence assembly**
* practicing **algorithm design in Python**

---

# Adapter Trimming Based on Sequencing Device

This repository demonstrates a simple Python implementation for **adapter trimming in DNA sequencing reads** based on the sequencing device used. Adapter trimming is an important preprocessing step in bioinformatics pipelines because sequencing platforms often add short artificial sequences (adapters) to DNA fragments during library preparation.

These adapter sequences are **not part of the original DNA** and must be removed before downstream analysis such as alignment, assembly, or variant detection.

---

## Concept

Different sequencing technologies attach **different adapter sequences** to DNA fragments. By identifying the sequencing device used to generate a read, we can determine which adapter sequence should be removed.

In this example, three sequencing platforms are considered:

* **Illumina**
* **Nanopore**
* **PacBio**

Each device has its own adapter sequence that appears at the **beginning of the read**.

The algorithm checks whether a read begins with the corresponding adapter and removes it if present.

---

## Adapter Sequences

| Device   | Adapter Sequence |
| -------- | ---------------- |
| Illumina | AGATCGGAAGAGC    |
| Nanopore | TTTCTGTTGGTGCTG  |
| PacBio   | ATCTCTCTCAACA    |

---

## Python Implementation

The following Python script performs adapter trimming based on the sequencing device.

```python
adapters = {
    "Illumina": "AGATCGGAAGAGC",
    "Nanopore": "TTTCTGTTGGTGCTG",
    "PacBio": "ATCTCTCTCAACA"
}

def trim_adapter(sequence, adapter):
    if sequence.startswith(adapter):
        return sequence[len(adapter):]
    return sequence

reads = [
("Illumina","AGATCGGAAGAGCATGCTAGCTAGCTAACGTTAGCTAGCTAGCTA"),
("Nanopore","TTTCTGTTGGTGCTGATGCTAGCTAGGCTAACCGTACGTTAGC"),
("PacBio","ATCTCTCTCAACAGATCGATCGATCGTTAGCTAGCTAACCGTA")
]

for device, seq in reads:
    cleaned = trim_adapter(seq, adapters[device])
    print(device, "clean sequence:")
    print(cleaned)
```

---

## How the Script Works

1. A dictionary stores adapter sequences for each sequencing platform.
2. The `trim_adapter()` function checks whether a sequence starts with the adapter.
3. If the adapter is present, it removes the adapter portion from the sequence.
4. The cleaned sequence is returned.
5. The script processes multiple reads and prints the trimmed results.

---

## Example Output

```
Illumina clean sequence:
ATGCTAGCTAGCTAACGTTAGCTAGCTAGCTA

Nanopore clean sequence:
ATGCTAGCTAGGCTAACCGTACGTTAGC

PacBio clean sequence:
GATCGATCGATCGTTAGCTAGCTAACCGTA
```

---

## Requirements

* Python 3.x
* No external libraries required

---

## Applications

Adapter trimming is commonly used in:

* Next Generation Sequencing (NGS) preprocessing
* Genome assembly pipelines
* Variant analysis workflows
* Bioinformatics data cleaning

---

## Author

Dr. Prabath Jayathissa

---

## License

This project is provided for **educational and research purposes**.


Dr. Prabath Jayathissa
