import os


def extract_overlapping_nanopore_reads(nanopore_reads_names, database_path, output_dir):

    for nanopore_read_name in nanopore_reads_names:
        output_file_path = os.path.join(output_dir, nanopore_read_name + '.fasta')
        cmd = 'samtools faidx ' + database_path + ' ' + nanopore_read_name + ' > ' + output_file_path
        os.system(cmd)
