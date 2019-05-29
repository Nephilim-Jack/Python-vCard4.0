"""
PyVCard creates a vCard file with some user defined variables
    Copyright (C) 2019  Matheus Henrique Mendes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

class VCard:
    
    def __init__(self, path_name):
        """
        path_name: The path and name of vcard file
        full_name: Full name of an person
        email: Email from an person
        company: The company from an person
        
        tel_type_num: tuples of type, number
        the type must be: work or home
        """
        self.path_name = path_name
        self.full_name = ''
        self.tel_type_num = []
        self.email = ''
        self.company = ''
    
    def create_vcard(self):
        """
        Create the vCard file in your selected path
        """
        vcard_text = 'BEGIN:VCARD\n\nVERSION:4.0\n\n'
        if self.full_name:
            vcard_text += f'FN:{self.full_name}\n\n'
        else:
            vcard_text += 'FN:NULL\n\n'
        if self.company:
            vcard_text += f'ORG:{self.company}\n\n'
        
        for type_name, number in self.tel_type_num:
            if type(type_name) == str:
                if type_name.lower() == 'work' or type_name.lower() == 'home':
                    vcard_text += f'TEL;TYPE={type_name.lower()},voice;VALUE=uri:tel:{str(number)}\n\n'
                else:
                    vcard_text += f'TEL;TYPE=home,voice;VALUE=uri:tel:{str(number)}\n\n'
            else:
                vcard_text += 'TEL;TYPE=home,voice;VALUE=uri:tel:00000000000000\n\n'
        if self.email:
            vcard_text += f'EMAIL:{self.email}\n\n'
        vcard_text += 'END:VCARD'
        
        with open(self.path_name, 'w') as v_file:
            v_file.write(vcard_text)
