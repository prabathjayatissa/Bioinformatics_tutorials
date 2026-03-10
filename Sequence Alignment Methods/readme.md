

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
5. The script processes mu
