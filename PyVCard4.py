"""
PyVCard creates a vCard file with some user defined variables
Copyright (C) 2019  Matheus Henrique Mendes
"""


class VCard:

    def __init__(self, path_name):
        """
        path_name: The path and name of vcard file
        company: The company from an person

        name_num: tuples of name, number
        """
        self.path_name = path_name + '/contatos.vcf'
        self.name_num = []
        self.company = ''

    def create_vcard(self):
        """
        Create the vCard file in your selected path
        """
        vcard_text = ''
        for i, data in enumerate(self.name_num):
            if i == 1:
                vcard_text += 'BEGIN:VCARD\nVERSION:4.0\n\n'
            else:
                vcard_text += '\nBEGIN:VCARD\nVERSION:4.0\n\n'

            vcard_text += f'FN:{data[0]}\n'
            vcard_text += f'ORG:{self.company}\n'
            vcard_text += f'TEL;TYPE=work:{str(data[1])}\n\n'

            vcard_text += 'END:VCARD'
        with open(self.path_name, 'w') as v_file:
            v_file.write(vcard_text)
