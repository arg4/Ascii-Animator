import re, pyperclip

input_string = pyperclip.paste()
output_string = ''
c = 1
r = 1

unicode_regex = re.compile(r'&[^&;]+;|\n|&\#\d+')
result = unicode_regex.findall(input_string)

for item in result:
    #print(input_string[i])
    rs = 'r'+str(r)
    cs = 'c'+str(c)
    if (item == '\n'):
        output_string += item
        r = r + 1
        c = 1
    else:
        output_string += ('<span class="'+rs+' '+cs+'">'+item+'</span>')
        c = c + 1

print(output_string)

pyperclip.copy(output_string)
