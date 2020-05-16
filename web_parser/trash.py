'''
normalization
'''
# project_text = unicodedata.normalize("NFKD", project_text)
# print(project_title, "\n\nDescription:\n", project_text, end='\n\n')
#

'''
 unused for parser
 '''
# span3 = soup.find('div', {'class': 'span3 well'})
# # Author
# print(span3.contents[3].contents[0], span3.contents[5].contents[1], url + span3.contents[5].attrs['href'], sep=' ')
# # Rating
# print(span3.contents[8].contents[1].text, span3.contents[8].contents[5].contents[0].strip(), sep=' ')
# # Type
# print(span3.contents[13].contents[0], span3.contents[14].strip(), sep=' ')
# # State
# print(span3.contents[17].contents[0], span3.contents[18].strip(), sep=' ')
# # Date (mismatch)
# if span3.contents[21].contents[0].startswith('Создан'):
#     print(span3.contents[21].contents[0], span3.contents[22].strip(), sep=' ')
# else:
#     print(span3.contents[25].contents[0], span3.contents[26].strip(), sep=' ')

# # Status
# print(tags_status.contents[1].contents[0])
# # Tags
# tags = [tag.contents[0] for tag in tags_status.contents[5:-1] if tag.contents[0] != ', ']
# # print(tags)
# except Exception:
# try:
#     # print(soup.title.text)
#     span9 = soup.find('div', {'class': 'well text-big'})
#     # print(span9.text.strip())
#
# except Exception:
#     print('Empty description')
# return False


'''
Database coding
'''
# cursor.execute('SET NAMES utf8mb4')
# cursor.execute("SET CHARACTER SET utf8mb4")
# cursor.execute("SET character_set_connection=utf8mb4")


'''
save to file
'''

# with open('test.html', 'w') as output_file:
#     output_file.write(response.text)
