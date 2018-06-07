import os


def blast_file_on_db(query_file_path, database_path):

    output_file_path = query_file_path.rstrip('.fasta') + '.tsv'

    cmd = ('blastn -num_alignments 10 -outfmt 6 -num_threads 3 ' +
           '-db ' + database_path + ' ' +
           '-query ' + query_file_path + ' ' +
           '-out ' + output_file_path)

    os.system(cmd)


def blast_files_on_db(sequence_file_path, database_path):

    head_file_path = sequence_file_path.replace('.fasta', '') + '_head' + '.fasta'
    tail_file_path = sequence_file_path.replace('.fasta', '') + '_tail' + '.fasta'

    blast_file_on_db(head_file_path, database_path)
    blast_file_on_db(tail_file_path, database_path)
