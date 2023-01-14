import os
from nanoid import generate
import frontmatter

path = 'www/content/vulnerabilities/'

for filename in os.listdir(path):
    if filename.endswith('.md') and not filename.startswith('_index'):
        file_path = os.path.join(path, filename)

        with open(file_path, 'r') as file:
            content = file.readlines()

        file_uuid = 'question-' + generate()

        content.insert(1, 'uuid: '+ file_uuid + '\n')

        with open(file_path, 'w') as file:
            file.writelines(content)

        os.rename(file_path, os.path.join(path, file_uuid + '.md'))