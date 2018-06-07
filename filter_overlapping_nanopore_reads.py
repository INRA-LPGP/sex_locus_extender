

def filter_single_file(file_path, n_base_pairs, min_alignment_length=0.9, min_percent_id=75):

    results = []

    input_file = open(file_path)

    for line in input_file:
        fields = line.rstrip('\n').split('\t')
        if len(fields) > 2:
            alignment_length = int(fields[3])
            percent_id = float(fields[2])
            # print(str(alignment_length), min_alignment_length * n_base_pairs, str(percent_id), min_percent_id)
            if alignment_length > min_alignment_length * n_base_pairs and percent_id > min_percent_id and alignment_length != n_base_pairs and percent_id != 100:
                results.append(fields[1])

    return results


def filter_overlapping_nanopore_reads(sequence_file_path, n_base_pairs):

    head_file_path = sequence_file_path.replace('.fasta', '') + '_head' + '.tsv'
    tail_file_path = sequence_file_path.replace('.fasta', '') + '_tail' + '.tsv'

    head_reads_names = filter_single_file(head_file_path, n_base_pairs)
    tail_reads_names = filter_single_file(tail_file_path, n_base_pairs)

    return set(head_reads_names + tail_reads_names)
