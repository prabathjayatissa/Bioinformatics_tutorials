# 110 Python Exercises for Introduction to Bioinformatics

This workbook contains **110 exercises** ranging from *Beginner* to *Expert* levels. Each exercise includes a short description, learning objectives, and a starter code snippet (where appropriate).


## Exercise 1: Read a FASTA file and count sequences

- **Level:** Mixed

- **Description:** Parse a FASTA file and return the number of sequences.

- **Learning objectives:** Practice file parsing, FASTA format rules.

- **Hints / Notes:** Handle multi-line sequences and headers.


---

 
## Exercise 2: Compute GC content of a DNA sequence

- **Level:** Mixed

- **Description:** Given a DNA sequence string, compute the GC percentage.

- **Learning objectives:** String counting and simple arithmetic.

- **Hints / Notes:** Ignore ambiguous bases like N.


---


## Exercise 3: Find ORFs in a DNA sequence (simple)

- **Level:** Mixed

- **Description:** Find open reading frames starting with ATG and ending with stop codons in-frame.

- **Learning objectives:** Frame scanning and slicing strings.

- **Hints / Notes:** Report coordinates and sequence.


---


## Exercise 4: Translate DNA to protein

- **Level:** Mixed

- **Description:** Translate coding DNA to amino acid sequence using standard codon table.

- **Learning objectives:** Dictionary mapping and slicing by 3.


---


## Exercise 5: Reverse complement of a DNA sequence

- **Level:** Mixed

- **Description:** Return reverse complement of given DNA sequence.

- **Learning objectives:** String translation and reversing.


---


## Exercise 6: Validate sequence alphabet

- **Level:** Mixed

- **Description:** Check if sequences are valid DNA, RNA, or protein and report invalid characters.

- **Learning objectives:** Sets, membership testing, error reporting.


---


## Exercise 7: Count k-mers in a sequence

- **Level:** Mixed

- **Description:** Count all k-length substrings in a given sequence.

- **Learning objectives:** Sliding window and dict accumulation.


---


## Exercise 8: Most frequent k-mer (with ties)

- **Level:** Mixed

- **Description:** Find k-mers with highest frequency.

- **Learning objectives:** Aggregation, sorting, ties handling.


---


## Exercise 9: Canonical k-mer considering reverse complement

- **Level:** Mixed

- **Description:** Map k-mers to canonical representation to collapse reverse complements.

- **Learning objectives:** Reduce redundancy in k-mer analyses.


---


## Exercise 10: Simple FASTQ parser and basic stats

- **Level:** Mixed

- **Description:** Parse FASTQ to compute number of reads, avg length, and average quality.

- **Learning objectives:** File IO and ASCII quality decoding.


---


## Exercise 11: Trim low-quality ends of reads

- **Level:** Mixed

- **Description:** Trim reads from ends until remaining bases have quality >= threshold.

- **Learning objectives:** Greedy trimming algorithm.


---


## Exercise 12: Simulate point mutations in a sequence

- **Level:** Mixed

- **Description:** Randomly mutate bases at given mutation rate.

- **Learning objectives:** Random choices and seeds for reproducibility.


---


## Exercise 13: Compute Hamming distance

- **Level:** Mixed

- **Description:** Compute Hamming distance between equal-length sequences.

- **Learning objectives:** Pairwise iteration and error handling for unequal lengths.


---


## Exercise 14: Pairwise identity percentage

- **Level:** Mixed

- **Description:** Compute percent identity between two sequences.

- **Learning objectives:** Combine Hamming calculation with percentage.


---


## Exercise 15: GC sliding-window profile

- **Level:** Mixed

- **Description:** Compute GC% across sliding windows and report per-window GC.

- **Learning objectives:** Windowed computations and boundary handling.


---


## Exercise 16: Count codon usage from CDS set

- **Level:** Mixed

- **Description:** Compute codon counts across a set of coding sequences.

- **Learning objectives:** Codon parsing and normalization per amino acid.


---


## Exercise 17: Simple sequence logo information content

- **Level:** Mixed

- **Description:** Compute nucleotide frequencies per column and information content in bits.

- **Learning objectives:** Intro to alignment profiles.


---


## Exercise 18: Merge overlapping intervals (BED-like)

- **Level:** Mixed

- **Description:** Merge a list of genomic intervals into non-overlapping merged intervals.

- **Learning objectives:** Sorting and interval merging logic.


---


## Exercise 19: Index genome by k-mer keys (simple)

- **Level:** Mixed

- **Description:** Map k-mers to their positions in the genome sequence.

- **Learning objectives:** Dictionary of lists and query functions.


---


## Exercise 20: Convert FASTQ qualities between Phred+33 and Phred+64

- **Level:** Mixed

- **Description:** Convert quality encoding between two common offsets.

- **Learning objectives:** ASCII conversion and validation.


---


## Exercise 21: Deduplicate reads by sequence

- **Level:** Mixed

- **Description:** Collapse identical reads and count duplicates.

- **Learning objectives:** Hashing strings and counting.


---


## Exercise 22: Compute read length distribution histogram

- **Level:** Mixed

- **Description:** Return dict mapping read length to counts from FASTQ.

- **Learning objectives:** Summarizing sequencing data.


---


## Exercise 23: Extract subsequences by coordinates

- **Level:** Mixed

- **Description:** Extract substrings given coordinate pairs; support 0-based and 1-based modes.

- **Learning objectives:** Coordinate conventions matter.


---


## Exercise 24: FASTQ to FASTA converter

- **Level:** Mixed

- **Description:** Convert FASTQ files to FASTA by dropping quality lines and formatting headers.

- **Learning objectives:** Streaming file IO.


---


## Exercise 25: Reverse complement FASTA writer

- **Level:** Mixed

- **Description:** Write reverse complements of input FASTA sequences to a new FASTA file.

- **Learning objectives:** File writing and sequence operations.


---


## Exercise 26: Simple random DNA generator

- **Level:** Mixed

- **Description:** Generate random DNA sequences of given length and base frequencies.

- **Learning objectives:** Random sampling with weights.


---


## Exercise 27: Count ambiguous bases and report fraction

- **Level:** Mixed

- **Description:** Report counts and fraction of ambiguous nucleotide codes in sequences.

- **Learning objectives:** Character class summaries.


---


## Exercise 28: Implement basic logging for scripts

- **Level:** Mixed

- **Description:** Add logging to scripts for progress updates and error reporting.

- **Learning objectives:** Use Python's logging module.


---


## Exercise 29: Unit tests for a small function (pytest)

- **Level:** Mixed

- **Description:** Write simple pytest tests for one or two small utility functions.

- **Learning objectives:** Test-driven development basics.


---


## Exercise 30: Package a script with setup.py/pyproject (toy)

- **Level:** Mixed

- **Description:** Create minimal project structure with pyproject.toml or setup.py for distribution.

- **Learning objectives:** Intro to packaging basics.


---


## Exercise 31: Parse GenBank and extract gene features (Biopython)

- **Level:** Mixed

- **Description:** Use Biopython to read GenBank records and extract feature annotations like gene/CDS.

- **Learning objectives:** Practical usage of Bio.SeqIO and SeqFeature.

- **Hints / Notes:** Handle multiple records per file.


---


## Exercise 32: Needleman-Wunsch global alignment (implement)

- **Level:** Mixed

- **Description:** Implement global alignment dynamic programming and traceback.

- **Learning objectives:** DP matrix construction and traceback implementation.


---


## Exercise 33: Smith-Waterman local alignment (implement)

- **Level:** Mixed

- **Description:** Implement local alignment DP and return best local alignment(s).

- **Learning objectives:** Matrix initialization differences from global alignment.


---


## Exercise 34: Build de Bruijn graph from reads

- **Level:** Mixed

- **Description:** Create de Bruijn graph nodes (k-1mers) and edges from k-mer overlaps.

- **Learning objectives:** Graph construction and memory considerations.


---


## Exercise 35: Assemble contigs from de Bruijn graph

- **Level:** Mixed

- **Description:** Walk unambiguous paths in de Bruijn graph to generate contigs.

- **Learning objectives:** Handle tips and bubbles heuristically.


---


## Exercise 36: Sequence clustering by edit distance (greedy)

- **Level:** Mixed

- **Description:** Group highly similar sequences using pairwise edit distances and greedy merging.

- **Learning objectives:** Quadratic approach for small datasets.


---


## Exercise 37: Pairwise alignment using Biopython pairwise2

- **Level:** Mixed

- **Description:** Use Biopython pairwise2 module and compare parameter effects.

- **Learning objectives:** Leverage libraries to benchmark implementations.


---


## Exercise 38: Compute consensus from multiple alignment

- **Level:** Mixed

- **Description:** Determine consensus sequence and per-position support from aligned sequences.

- **Learning objectives:** Majority voting and ambiguity handling.


---


## Exercise 39: Neighbor-Joining tree building

- **Level:** Mixed

- **Description:** Implement NJ algorithm from distance matrix and output Newick format.

- **Learning objectives:** Distance-based phylogeny reconstruction.


---


## Exercise 40: Parse VCF to count variant types and transitions/transversions

- **Level:** Mixed

- **Description:** Parse VCF and summarize SNPs vs indels, transition/transversion ratio.

- **Learning objectives:** VCF parsing and ALT field handling.


---


## Exercise 41: Annotate variants with overlapping genes (BED intersections)

- **Level:** Mixed

- **Description:** Intersect variant positions with gene intervals and annotate accordingly.

- **Learning objectives:** Interval search performance considerations.


---


## Exercise 42: PWM motif scanning

- **Level:** Mixed

- **Description:** Scan sequences using a position weight matrix and threshold for hits.

- **Learning objectives:** Log-odds scoring and p-value approximations optional.


---


## Exercise 43: Compute ROC/AUC for classifier outputs

- **Level:** Mixed

- **Description:** Calculate TPR/FPR and AUC from scores and true labels.

- **Learning objectives:** Use sklearn or implement manually.


---


## Exercise 44: Simulate reads from genome with errors

- **Level:** Mixed

- **Description:** Sample reads from genome and introduce substitution errors per-position probability.

- **Learning objectives:** Generate ground truth mapping coordinates.


---


## Exercise 45: Seed-and-extend read mapper (toy)

- **Level:** Mixed

- **Description:** Index genome by k-mer seeds and extend candidate mappings with alignment.

- **Learning objectives:** Return best mapping per read.


---


## Exercise 46: Median filter for quality scores

- **Level:** Mixed

- **Description:** Apply median filter across quality vectors to smooth noise.

- **Learning objectives:** Signal processing on quality arrays.


---


## Exercise 47: Compute Tajima's D (simplified)

- **Level:** Mixed

- **Description:** Estimate π and θ and compute Tajima's D from aligned sequences.

- **Learning objectives:** Intro to population genetics statistics.


---


## Exercise 48: HMM Viterbi for CpG island detection

- **Level:** Mixed

- **Description:** Implement Viterbi on a two-state HMM to detect high-CpG regions.

- **Learning objectives:** Emission and transition modeling.


---


## Exercise 49: Motif search with IUPAC degeneracy codes

- **Level:** Mixed

- **Description:** Convert degenerate IUPAC codes into regex and find motif matches.

- **Learning objectives:** Regex construction and performance.


---


## Exercise 50: k-mer abundance histogram and peak detection

- **Level:** Mixed

- **Description:** Compute k-mer abundance histogram from reads and locate major peaks.

- **Learning objectives:** Genome size and repeat analysis heuristics.


---


## Exercise 51: Forward algorithm for simple pair-HMM

- **Level:** Mixed

- **Description:** Implement forward algorithm to compute alignment likelihood under pair-HMM.

- **Learning objectives:** Numerical stability and log-space optional.


---


## Exercise 52: Parallelize per-read processing with multiprocessing

- **Level:** Mixed

- **Description:** Use multiprocessing Pool to distribute independent read tasks and collect results.

- **Learning objectives:** Process management and combining outputs.


---


## Exercise 53: Parse SAM CIGAR strings and compute alignment end

- **Level:** Mixed

- **Description:** Interpret CIGAR operations to compute aligned reference span and clipped bases.

- **Learning objectives:** CIGAR parsing grammar.


---


## Exercise 54: Base quality score recalibration (toy)

- **Level:** Mixed

- **Description:** Accumulate empirical error rates and adjust quality scores accordingly.

- **Learning objectives:** Batched stats and recalibration table.


---


## Exercise 55: Variant hard-filter implementation

- **Level:** Mixed

- **Description:** Apply a set of heuristic filters to variants and output PASS/FAIL flags.

- **Learning objectives:** Depth, quality, allele balance rules.


---


## Exercise 56: Single-cell k-means clustering on expression data

- **Level:** Mixed

- **Description:** Scale data, run k-means, and compute silhouette score to evaluate cluster quality.

- **Learning objectives:** Basic single-cell clustering pipeline.


---


## Exercise 57: UPGMA tree building

- **Level:** Mixed

- **Description:** Implement UPGMA hierarchical clustering to build phylogenetic tree.

- **Learning objectives:** Compare to NJ outputs.


---


## Exercise 58: BLAST-like seed-and-extend heuristic (toy)

- **Level:** Mixed

- **Description:** Find exact short seeds then extend locally to score hits similar to BLAST heuristics.

- **Learning objectives:** Seed selection and extension scoring.


---


## Exercise 59: Interval tree implementation for genomic overlaps

- **Level:** Mixed

- **Description:** Build an interval tree for fast overlaps and compare to naive scanning.

- **Learning objectives:** Data structure usage and complexity.


---


## Exercise 60: Coalescent simulator for small samples

- **Level:** Mixed

- **Description:** Simulate simple coalescent trees and output topologies and branch lengths.

- **Learning objectives:** Stochastic simulation fundamentals.


---


## Exercise 61: Permutation test for motif enrichment

- **Level:** Mixed

- **Description:** Compute empirical p-value by permuting regions and counting motif occurrences.

- **Learning objectives:** Non-parametric significance testing.


---


## Exercise 62: Build a CLI genome utility with argparse

- **Level:** Mixed

- **Description:** Implement subcommands for indexing, querying, and reporting basic stats.

- **Learning objectives:** User interface and argument parsing.


---


## Exercise 63: k-mer feature extraction + logistic regression classifier

- **Level:** Mixed

- **Description:** Extract k-mer counts as features and train sklearn logistic regression for classification.

- **Learning objectives:** Feature matrix assembly and model evaluation.


---


## Exercise 64: Read error model (position-dependent) simulation

- **Level:** Mixed

- **Description:** Model error probability that depends on position in read and simulate accordingly.

- **Learning objectives:** Benchmark mapping sensitivity.


---


## Exercise 65: Parse GFF/GTF and build transcript models

- **Level:** Mixed

- **Description:** Read GFF/GTF and collect transcripts with exon lists and CDS boundaries.

- **Learning objectives:** Data structure for genes and isoforms.


---


## Exercise 66: Assess assembly completeness with marker genes (toy BUSCO)

- **Level:** Mixed

- **Description:** Search for marker genes in assembly and create presence/absence summary.

- **Learning objectives:** Homology search basics.


---


## Exercise 67: Read/write gzip compressed FASTA/FASTQ

- **Level:** Mixed

- **Description:** Transparent IO for gzipped sequence files using gzip module or Bio.SeqIO.

- **Learning objectives:** Memory-conscious streaming.


---


## Exercise 68: Minimal REST API for sequence lookup (Flask)

- **Level:** Mixed

- **Description:** Create endpoints to query sequences by ID or coordinate and return JSON.

- **Learning objectives:** Microservice basics.


---


## Exercise 69: Greedy overlap-layout assembler

- **Level:** Mixed

- **Description:** Detect overlaps between reads and greedily merge to form contigs.

- **Learning objectives:** Pairwise overlap detection and consensus.


---


## Exercise 70: Burrows-Wheeler Transform and backward search

- **Level:** Mixed

- **Description:** Compute BWT and implement backward search for exact pattern matching.

- **Learning objectives:** Suffix array/BWT basics.


---


## Exercise 71: Naive suffix array construction and queries

- **Level:** Mixed

- **Description:** Construct suffix array by sorting suffixes and use it for substring queries.

- **Learning objectives:** Indexing strings for fast lookup.


---


## Exercise 72: k-mer spectrum error correction

- **Level:** Mixed

- **Description:** Detect low-abundance k-mers and correct reads by finding paths through high-abundance k-mers.

- **Learning objectives:** Error correction heuristics.


---


## Exercise 73: Accelerate numeric operations with NumPy vectorization

- **Level:** Mixed

- **Description:** Replace Python loops with NumPy operations for heavy computations.

- **Learning objectives:** Benchmark and compare speeds.


---


## Exercise 74: Read-backed variant phasing (toy)

- **Level:** Mixed

- **Description:** Use reads spanning heterozygous sites to build phase blocks.

- **Learning objectives:** Graph-connected components and phasing.


---


## Exercise 75: Bayesian genotype caller from pileup

- **Level:** Mixed

- **Description:** Compute genotype likelihoods and posteriors using priors and likelihood model.

- **Learning objectives:** Probabilistic genotype calling.


---


## Exercise 76: RNA-seq normalization and simple DE test

- **Level:** Mixed

- **Description:** Implement median-of-ratios normalization and perform t-tests/DE on counts.

- **Learning objectives:** Normalization effects on DE.


---


## Exercise 77: Bootstrap support for phylogenies

- **Level:** Mixed

- **Description:** Resample alignment columns to compute bootstrap support values for branches.

- **Learning objectives:** Statistical support for trees.


---


## Exercise 78: Sequence classification with deep learning (CNN)

- **Level:** Mixed

- **Description:** Build and train a convolutional network to classify sequences; use one-hot encoding.

- **Learning objectives:** Keras/TensorFlow model construction.


---


## Exercise 79: Parallel k-mer counting with memory mapping

- **Level:** Mixed

- **Description:** Use memory-mapped arrays to handle large k-mer counters efficiently.

- **Learning objectives:** Systems-level optimization.


---


## Exercise 80: Sparse PCA for single-cell data

- **Level:** Mixed

- **Description:** Use sparse representations and randomized algorithms for PCA on scRNA-seq.

- **Learning objectives:** Dimensionality reduction for sparse data.


---


## Exercise 81: GWAS toy pipeline with multiple testing correction

- **Level:** Mixed

- **Description:** Compute associations and apply Bonferroni/FDR corrections to p-values.

- **Learning objectives:** Multiple testing handling.


---


## Exercise 82: Baum-Welch training of HMM

- **Level:** Mixed

- **Description:** Fit HMM parameters with EM for simple emission/transition models.

- **Learning objectives:** Expectation-Maximization basics.


---


## Exercise 83: Paired-end read merging with quality-aware consensus

- **Level:** Mixed

- **Description:** Merge read pairs based on overlap and compute consensus sequence with quality weighting.

- **Learning objectives:** Merge heuristics and QC.


---


## Exercise 84: Minimizer sketching for sequence comparison

- **Level:** Mixed

- **Description:** Compute minimizers and estimate sequence similarity with Jaccard/containment.

- **Learning objectives:** Sketching algorithms.


---


## Exercise 85: Pangenome presence/absence matrix and clustering

- **Level:** Mixed

- **Description:** Compute gene presence/absence from cluster assignments and cluster genomes.

- **Learning objectives:** Comparative genomics pipelines.


---


## Exercise 86: Design CRISPR guides and score off-targets (toy)

- **Level:** Mixed

- **Description:** Enumerate candidate guides and score by counting near matches allowing mismatches.

- **Learning objectives:** Guide selection heuristics.


---


## Exercise 87: Create CIGAR from alignment operations

- **Level:** Mixed

- **Description:** Convert alignment operations list into SAM CIGAR string with counts and operators.

- **Learning objectives:** SAM format compliance.


---


## Exercise 88: Optimize hot loops with Numba or Cython

- **Level:** Mixed

- **Description:** Use Numba jit to speed up compute-heavy Python functions and benchmark improvements.

- **Learning objectives:** Just-in-time compilation.


---


## Exercise 89: Probabilistic record linkage for sample metadata

- **Level:** Mixed

- **Description:** Link noisy metadata records across datasets probabilistically using similarity scores and EM.

- **Learning objectives:** Data integration techniques.


---


## Exercise 90: Long-read consensus correction from multiple alignments

- **Level:** Mixed

- **Description:** Generate consensus from multiple noisy long reads covering same region.

- **Learning objectives:** Majority voting with error models.


---


## Exercise 91: Variant graph representation (simple GFA)

- **Level:** Mixed

- **Description:** Represent variants as a graph and export to GFA-like format for visualization.

- **Learning objectives:** Graph representation of variation.


---


## Exercise 92: Memory-efficient hierarchical clustering on sparse data

- **Level:** Mixed

- **Description:** Implement clustering using sparse distances or approximate linkage to scale.

- **Learning objectives:** High-dimensional clustering.


---


## Exercise 93: Wright-Fisher simulation with selection and mutation

- **Level:** Mixed

- **Description:** Simulate allele frequency trajectories and summarize fixation probabilities.

- **Learning objectives:** Population genetics simulation.


---


## Exercise 94: Snakemake pipeline skeleton for sequence analysis

- **Level:** Mixed

- **Description:** Design Snakefile with rules for QC, mapping, and variant calling including conda envs.

- **Learning objectives:** Workflow automation and reproducibility.


---


## Exercise 95: EM isoform quantification for RNA-seq

- **Level:** Mixed

- **Description:** Allocate reads probabilistically to isoforms and estimate expression levels with EM.

- **Learning objectives:** Transcript quantification methods.


---


## Exercise 96: Compressed k-mer storage with bitpacking

- **Level:** Mixed

- **Description:** Pack k-mers into binary format and implement membership queries.

- **Learning objectives:** Low-level storage techniques.


---


## Exercise 97: Benchmark alignment scoring schemes on simulated data

- **Level:** Mixed

- **Description:** Run multiple scoring schemes and report sensitivity/precision trade-offs.

- **Learning objectives:** Empirical evaluation of aligner parameters.


---


## Exercise 98: End-to-end mapper with FM-index and banded alignment

- **Level:** Mixed

- **Description:** Implement mapper using FM-index for seeding and banded DP for extension; produce SAM-like output.

- **Learning objectives:** Systems and algorithm integration; performance optimization.


---


## Exercise 99: Distributed k-mer counting with PySpark

- **Level:** Mixed

- **Description:** Implement scalable k-mer counting across cluster using PySpark RDDs/DataFrames.

- **Learning objectives:** Big-data processing patterns.


---


## Exercise 100: Differentiable aligner integrated into neural net

- **Level:** Mixed

- **Description:** Implement soft/differentiable alignment and use as layer in a sequence model.

- **Learning objectives:** Research-level ML + algorithms.


---


## Exercise 101: Full overlap-layout-consensus assembler

- **Level:** Mixed

- **Description:** From raw reads assemble contigs with overlap detection, layout, and consensus stages.

- **Learning objectives:** Large project integrating several algorithms.


---


## Exercise 102: C/C++ optimization with pybind11

- **Level:** Mixed

- **Description:** Profile Python, implement hotspot in C++, and expose via pybind11; provide build instructions.

- **Learning objectives:** Performance engineering and bindings.


---


## Exercise 103: Reference-panel genotype imputation (toy)

- **Level:** Mixed

- **Description:** Implement simplified imputation model using reference haplotypes and impute missing genotypes.

- **Learning objectives:** Statistical genetics and algorithmic complexity.


---


## Exercise 104: Containerized reproducible workflow with CI

- **Level:** Mixed

- **Description:** Create containerized pipelines (Docker) and CI workflows to run tests end-to-end.

- **Learning objectives:** Software engineering for reproducible science.


---


## Exercise 105: Privacy-preserving genomic query demo (toy)

- **Level:** Mixed

- **Description:** Prototype privacy-preserving query using simple MPC or homomorphic operations for demonstration purposes.

- **Learning objectives:** Careful about security claims; educational demo.


---


## Exercise 106: Scalable single-cell multi-omics integration algorithm

- **Level:** Mixed

- **Description:** Integrate multimodal single-cell datasets using matrix factorization/graph alignment methods.

- **Learning objectives:** Research and engineering challenge.


---


## Exercise 107: Software release: tests, packaging, CI, docs

- **Level:** Mixed

- **Description:** Turn a script into a robust package with tests, packaging, docs, and continuous integration configs.

- **Learning objectives:** Prepare code for public release and reuse.


---

