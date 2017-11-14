'''
Uses python3.
Email: dr.mark.schultz@gmail.com
Github: schultzm

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

from setuptools import setup, find_packages
import gff2fa
import os


LONG_DESCRIPTION = 'Convert GFF files to multi-fasta. Write to stdout.'

if os.path.exists('README'):
    LONG_DESCRIPTION = open('README').read()

setup(


    name = gff2fa.__name__,
    version = gff2fa.__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gff2fa = gff2fa.__main__:main'
        ]
    },

    description = gff2fa.__description__,
    long_description=LONG_DESCRIPTION,
    classifiers = ['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU Affero General ' +
                   'Public License v3 or later (AGPLv3+)',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Topic :: Scientific/Engineering :: Medical Science Apps.',
                   'Intended Audience :: Science/Research'],
    keywords = ['GFF',
                'gff',
                'fasta',
                'multi-fasta',
                'mfasta'],
    download_url = gff2fa.__install__,
    author = gff2fa.__author__,
    author_email = gff2fa.__author_email__,
    license = gff2fa.__license__,
    include_package_data = True,
    install_requires = ['bcbio-gff>=0.6.4',
                        'biopython>=1.70'],
    )