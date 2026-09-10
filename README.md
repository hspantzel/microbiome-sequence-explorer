# Microbiome Sequence Explorer

A beginner-friendly Python project for exploring DNA sequence composition and k-mer patterns in FASTA files.

I created this project to practice applying Python to biological sequence data and to begin building familiarity with bioinformatics workflows.

## What it does

The program reads one or more DNA sequences from a FASTA file and reports:

- Sequence length
- A, C, G, and T nucleotide counts
- GC content
- Most common k-mers
- Results for multiple sequences in a single FASTA file

## Why these measurements matter

**GC content** is the percentage of nucleotides in a DNA sequence that are guanine (G) or cytosine (C). Sequence composition can vary across organisms and genomic regions.

**K-mers** are short sequences of length `k`. Counting k-mers is a common building block in bioinformatics and can be useful for comparing sequences, identifying patterns, and analyzing genomic or metagenomic data.

## Example

The repository includes `sample.fasta`, containing synthetic DNA sequences for demonstration.

Run:

```bash
python sequence_explorer.py sample.fasta
```

The default k-mer length is 3.

You can choose another value using `-k`:

```bash
python sequence_explorer.py sample.fasta -k 4
```

## Files

- `sequence_explorer.py` — Python program for FASTA sequence analysis
- `sample.fasta` — synthetic example DNA sequences
- `README.md` — project documentation

## Requirements

- Python 3
- No external Python packages are required

## What I learned

This project helped me practice:

- Reading biological data stored in FASTA format
- Breaking a larger analysis into reusable Python functions
- Using dictionaries and `collections.Counter`
- Calculating summary statistics from sequence data
- Working with overlapping k-mers
- Building a command-line interface with `argparse`
- Writing reproducible documentation for a small computational project

## Future improvements

Possible extensions include:

- Comparing k-mer profiles across multiple sequences
- Adding sequence validation and error handling
- Plotting nucleotide and k-mer frequencies
- Calculating sequence similarity
- Analyzing real public genomic or microbiome datasets
- Exporting results to CSV for downstream analysis

## Data note

The sequences in `sample.fasta` are synthetic and are included only to demonstrate how the program works.

## Author

**Heidi Spantzel**  
Incoming undergraduate at the University of California, San Diego  
Interests: computational biology, machine learning, biomedical AI, and cybersecurity
