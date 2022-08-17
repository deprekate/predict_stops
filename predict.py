import sys

def rev_comp(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G',
            'N':'N',
            'R':'Y','Y':'R','S':'S','W':'W','K':'M','M':'K',
            'B':'V','V':'B','D':'H','H':'D'}
    return "".join([seq_dict[base] for base in reversed(seq)])



seq = ""
with open(sys.argv[1]) as fp:
	for line in fp:
		if not line.startswith(">"):
			seq += line.rstrip()

distances = {'TAG':[], 'TGA':[], 'TAA':[]}


for frame in [0,1,2]:
	last_seen = {'TAG':0, 'TGA':0, 'TAA':0}
	for i in range(frame, len(seq)-2, 3):
		codon = seq[i] + seq[i+1] + seq[i+2]
		if codon in last_seen:
			distances[codon].append(i - last_seen[codon])
			last_seen[codon] = i

seq = rev_comp(seq)

for frame in [0,1,2]:
	last_seen = {'TAG':0, 'TGA':0, 'TAA':0}
	for i in range(frame, len(seq)-2, 3):
		codon = seq[i] + seq[i+1] + seq[i+2]
		if codon in last_seen:
			distances[codon].append(i - last_seen[codon])
			last_seen[codon] = i

for stop in distances:
	for distance in distances[stop]:
		print(stop, distance, sep='\t')
