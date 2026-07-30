import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    result = []
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            result.append(char)

    text = ''.join(result)

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))