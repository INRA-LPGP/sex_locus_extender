

def create_head_and_tail_files(sequence_file_path, n_base_pairs):

    sequence_file = open(sequence_file_path)
    header = sequence_file.readline().rstrip('\n')
    sequence = ''.join(line.rstrip('\n') for line in sequence_file)

    head_file_path = sequence_file_path.replace('.fasta', '') + '_head' + '.fasta'
    tail_file_path = sequence_file_path.replace('.fasta', '') + '_tail' + '.fasta'

    head_header = header + '_head'
    tail_header = header + '_tail'

    head_file = open(head_file_path, 'w')
    tail_file = open(tail_file_path, 'w')

    head_file.write(head_header + '\n' + sequence[0:n_base_pairs])
    tail_file.write(tail_header + '\n' + sequence[-n_base_pairs:])
