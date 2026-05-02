## How to use it

Open the notebook in Jupyter Notebook / JupyterLab

Place your input files in the same directory:

 - primers.fasta 

 - raw_reads.fasta 

Run cells top to bottom

Use:

```python


assemble_primers("primers.fasta")
trim_fasta("raw_reads.fasta", "trimmed_reads.fasta")

```


