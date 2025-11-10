import os
import sys
import glob

usage="""
    Create a samplesheet with information about the samples for a given project before running the nf-core/rnaseq analysis pipeline
    For detailed sescription, please see: https://nf-co.re/rnaseq/usage#samplesheet-input

Usage:
        create_rnaseq_samplesheet.py <ProjectID> <Strandedness>
    eg. create_rnaseq_samplesheet.py P001 auto >P001.csv

Output:

        CSV lines print to ScreenOut 

"""

if len(sys.argv) < 3:
        sys.exit(usage)

project = sys.argv[1]
strandedness = sys.argv[2]	#forward/reverse/unstranded/auto
data_path=os.path.join('/proj/ngi2016003/nobackup/NGI/DATA',project)
header="sample,fastq_1,fastq_2,strandedness"
sampleList=os.listdir(data_path)
sampleList.sort()
print(header)
for sample in sampleList:
	path_pattern = os.path.join(data_path, sample, '*/*/*R1*.gz')
	paths = glob.glob(path_pattern)

	for counter, R1 in enumerate(paths, 1):
		index=str(counter)
		R2 = R1.replace('_R1_','_R2_')
		print(sample + ',' + R1 + ',' + R2 + ',' + strandedness)
