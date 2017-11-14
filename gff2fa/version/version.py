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

import gff2fa
import sys

def version():
    '''
    Print the version
    '''
    print('Version:', gff2fa.__version__)
    print('Date:', gff2fa.__version_date__)
    print('Author:', gff2fa.__author__)
    print('Email:', gff2fa.__author_email__)
    print('Github:', gff2fa.__github_username__)
    print('Install:', gff2fa.__install__)
    print('🐛', file=sys.stderr)


