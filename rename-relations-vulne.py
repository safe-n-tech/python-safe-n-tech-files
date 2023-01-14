import os
from nanoid import generate
import frontmatter

goodPracticesPath = 'www/content/good-practices/'
vulnerabilitiesPath = 'www/content/vulnerabilities/'

for gp_filename in os.listdir(goodPracticesPath):
    if gp_filename.endswith('.md') and not gp_filename.startswith('_index'):
        gp_file_path = os.path.join(goodPracticesPath, gp_filename)

        print(gp_file_path)
        gp_md_file = frontmatter.load(gp_file_path)
        print(gp_md_file['uuid'])

        for vulne_filename in os.listdir(vulnerabilitiesPath):
            if vulne_filename.endswith('.md') and not vulne_filename.startswith('_index'):
                vulne_file_path = os.path.join(vulnerabilitiesPath, vulne_filename)

                print(vulne_file_path)
                vulne_md_file = frontmatter.load(vulne_file_path)
                if 'goodPractices' in vulne_md_file:
                    print(vulne_md_file['goodPractices'])

                    for i in range(len(vulne_md_file['goodPractices'])):

                        if vulne_md_file['goodPractices'][i] == gp_md_file['title']:
                            vulne_md_file['goodPractices'][i] = gp_md_file['uuid']

                with open(vulne_file_path, 'w') as file:
                    file.writelines(frontmatter.dumps(vulne_md_file))