import sys
from create_head_and_tail_files import create_head_and_tail_files
from blast_files_on_db import blast_files_on_db
from filter_overlapping_nanopore_reads import filter_overlapping_nanopore_reads
from extract_overlapping_nanopore_reads import extract_overlapping_nanopore_reads

# Input query sequence fasta file
sequence_file_path = sys.argv[1]

# Size of head and tail sequences
n_base_pairs = int(sys.argv[2])

# Database path
database_path = sys.argv[3]

# Output dir
output_dir = sys.argv[4]

create_head_and_tail_files(sequence_file_path, n_base_pairs)

blast_files_on_db(sequence_file_path, database_path)

nanopore_reads_names = filter_overlapping_nanopore_reads(sequence_file_path, n_base_pairs)

print(nanopore_reads_names)

extract_overlapping_nanopore_reads(nanopore_reads_names, database_path, output_dir)
