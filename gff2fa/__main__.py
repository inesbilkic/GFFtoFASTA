#!/usr/bin/env python3

'''
Author: Mark Schultz
Github: schultzm
email: dr.mark.schultz@gmail.com
YYYYMMDD: 20171114

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


def main():
    '''
    The main routine.
    '''
    import argparse
    parser = argparse.ArgumentParser(description = "Convert GFF to mfasta")
    subparsers = parser.add_subparsers(title='Sub-commands help:',
                                      help='', metavar='',
                                      dest='subparser_name')
    convert = subparsers.add_parser('convert',
                                    help='Convert GFF to mfasta to stdout.',
                                    description='Convert GFF to mfasta. ')
    convert.add_argument('infile', help = 'GFF infile.')
    version = subparsers.add_parser('version', help='Print version.')
    args = parser.parse_args()

    import os
    if not args.subparser_name:
        os.system('gff2fa -h')
    elif args.subparser_name == 'version':
        from gff2fa.version.version import version
        version()
    else:
        if args.subparser_name == 'convert':
            parse_gff(args.infile)

def parse_gff(infile):
    '''
    Parameters:
        infile: gff format infile
    If gff is successfully parsed, return multi-fasta seq record to stdout 
    '''
    from BCBio import GFF
    gff=GFF.parse(infile)
    for seq_record in gff:
        print(seq_record.format('fasta'))

if __name__ == '__main__':
    main()
