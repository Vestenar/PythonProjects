def htmlEndTagByStartTag(startTag):
    print(startTag[1:-1])
    a = "</" + startTag.split()[0][1:]
    if startTag.split()[0][-1] != '>':
        a += ">"
    return a

'''
def htmlEndTagByStartTag(startTag):
    return "</" + startTag[1:startTag.find(" ")] + ">" # если пробела нет, то будет [1:-1]
    
'''
print(htmlEndTagByStartTag("<i>"))
'''
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

Given the starting HTML tag, find the appropriate end tag which your editor should propose.

If you are not familiar with HTML, consult with this note.

Example

    For startTag = "<button type='button' disabled>", the output should be
    htmlEndTagByStartTag(startTag) = "</button>";
    For startTag = "<i>", the output should be
    htmlEndTagByStartTag(startTag) = "</i>".

'''
