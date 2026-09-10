from collections import Counter
import argparse


def read_fasta(filename):
    """Read sequences from a FASTA file."""
    sequences = {}
    current_name = None
    current_sequence = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_name is not None:
                    sequences[current_name] = "".join(current_sequence)

                current_name = line[1:]
                current_sequence = []
            else:
                current_sequence.append(line.upper())

    if current_name is not None:
        sequences[current_name] = "".join(current_sequence)

    return sequences


def nucleotide_counts(sequence):
    """Count A, C, G, and T nucleotides."""
    counts = Counter(sequence)

    return {
        "A": counts.get("A", 0),
        "C": counts.get("C", 0),
        "G": counts.get("G", 0),
        "T": counts.get("T", 0),
    }


def gc_content(sequence):
    """Calculate the percentage of bases that are G or C."""
    if len(sequence) == 0:
        return 0.0

    gc_bases = sequence.count("G") + sequence.count("C")
    return (gc_bases / len(sequence)) * 100


def kmer_counts(sequence, k=3):
    """Count overlapping k-mers in a DNA sequence."""
    kmers = [
        sequence[i:i + k]
        for i in range(len(sequence) - k + 1)
    ]

    return Counter(kmers)


def analyze_sequence(name, sequence, k):
    print(f"\nSequence: {name}")
    print(f"Length: {len(sequence)} bases")
    print(f"GC content: {gc_content(sequence):.2f}%")

    counts = nucleotide_counts(sequence)

    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"  {nucleotide}: {count}")

    kmers = kmer_counts(sequence, k)

    print(f"Top {k}-mers:")
    for kmer, count in kmers.most_common(5):
        print(f"  {kmer}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Explore DNA sequences stored in FASTA format."
    )

    parser.add_argument(
        "fasta_file",
        help="Path to a FASTA file"
    )

    parser.add_argument(
        "-k",
        type=int,
        default=3,
        help="Length of k-mers to analyze (default: 3)"
    )

    args = parser.parse_args()

    sequences = read_fasta(args.fasta_file)

    print(f"Loaded {len(sequences)} sequence(s).")

    for name, sequence in sequences.items():
        analyze_sequence(name, sequence, args.k)


if __name__ == "__main__":
    main()
