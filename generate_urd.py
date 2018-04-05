import urd.urd
import optparse
import os


parser = optparse.OptionParser()
usage = "usage: %prog [options] arg"

parser.add_option("--input-file", dest="input_file", metavar="FILE")
parser.add_option("--output-file", dest="output_file", metavar="FILE")


(options, args) = parser.parse_args()

urd_instance = urd.urd.Urd()

trace_lines = open(options.input_file, 'r').readlines()
output_file = open(options.output_file, 'w')

for line in trace_lines:
    parts = line.split()
    output_file.write(str(parts[0]) + " ")
    output_file.write(str(parts[1]) + " ")
    output_file.write(str(urd_instance.access(parts[0])))
    output_file.write("\n")

output_file.close()