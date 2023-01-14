import os
from nanoid import generate
import frontmatter

goodPracticesPath = 'www/content/good-practices/'
questionsPath = 'www/content/questions/'

for gp_filename in os.listdir(goodPracticesPath):
    if gp_filename.endswith('.md') and not gp_filename.startswith('_index'):
        gp_file_path = os.path.join(goodPracticesPath, gp_filename)

        print(gp_file_path)
        gp_md_file = frontmatter.load(gp_file_path)
        print(gp_md_file['uuid'])

        for question_filename in os.listdir(questionsPath):
            if question_filename.endswith('.md') and not question_filename.startswith('_index'):
                question_file_path = os.path.join(questionsPath, question_filename)

                print(question_file_path)
                question_md_file = frontmatter.load(question_file_path)
                if 'goodPractices' in question_md_file:
                    print(question_md_file['goodPractices'])

                    for i in range(len(question_md_file['goodPractices'])):

                        if question_md_file['goodPractices'][i] == gp_md_file['title']:
                            question_md_file['goodPractices'][i] = gp_md_file['uuid']

                with open(question_file_path, 'w') as file:
                    file.writelines(frontmatter.dumps(question_md_file))