import os
import sys
import glob
import argparse

class CustomParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        help_text = """

Description:
Generate an RNA-seq sample sheet for a given project before running the nf-core/rnaseq analysis pipeline.
The resulting CSV is printed to the screen (stdout). To save the CSV to a file, use shell redirection.

USAGE:
  create_rnaseq_samplesheet.py <ProjectID> <Strandedness> > <output.csv>

Examples:
  create_rnaseq_samplesheet.py P001 auto > P001.csv           # Create a sample sheet in the current folder
  create_rnaseq_samplesheet.py P001 auto > /path/to/P001.csv  # Create a sample sheet and save to a specific location

Arguments:
  ProjectID      Identifier for your RNA-seq project (e.g., P001)
  Strandedness   Library strandedness (forward/reverse/unstranded/auto, use 'auto' to auto-detect)

Optional arguments:
  -h, --help     Show this help message and exit
"""
        print(help_text)

def main():
    parser = CustomParser(add_help=False)  # disable default help
    parser.add_argument("ProjectID", help="Identifier for your RNA-seq project (e.g., P001)")
    parser.add_argument("Strandedness", help="Library strandedness (use 'auto' to auto-detect)")
    parser.add_argument("-h", "--help", action="help", help="show this help message and exit")

    args = parser.parse_args()

    # Generate CSV content
    csv_content = f"# Sample sheet for project {args.ProjectID}\nStrandedness,{args.Strandedness}\n"
    print(csv_content)

if __name__ == "__main__":
    main()

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
