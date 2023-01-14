import os
from nanoid import generate
import frontmatter

goodPracticesPath = 'www/content/good-practices/'
vulnerabilitiesPath = 'www/content/vulnerabilities/'
definitionsPath = 'www/content/definitions/'

for def_filename in os.listdir(definitionsPath):
    if def_filename.endswith('.md') and not def_filename.startswith('_index'):
        def_file_path = os.path.join(definitionsPath, def_filename)

        print(def_file_path)
        def_md_file = frontmatter.load(def_file_path)
        print(def_md_file['uuid'])

        for vulne_filename in os.listdir(vulnerabilitiesPath):
            if vulne_filename.endswith('.md') and not vulne_filename.startswith('_index'):
                vulne_file_path = os.path.join(vulnerabilitiesPath, vulne_filename)

                print(vulne_file_path)
                vulne_md_file = frontmatter.load(vulne_file_path)
                if 'definitions' in vulne_md_file:
                    print(vulne_md_file['definitions'])

                    for i in range(len(vulne_md_file['definitions'])):

                        if vulne_md_file['definitions'][i] == def_md_file['title']:
                            vulne_md_file['definitions'][i] = def_md_file['uuid']

                with open(vulne_file_path, 'w') as file:
                    file.writelines(frontmatter.dumps(vulne_md_file))