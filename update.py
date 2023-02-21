# Open the debug console with Ctrl+: (which is Ctrl+Shift+; on US keyboards)
# (Don't have the browser window open when you do.)
# Run it with Ctrl+Enter
# Remove the # from the last line to actually save the changes
import re
# as per recommendation from @freylis, compile once only
dic = {}
def cleanhtml(raw_html):
  CLEANR = re.compile('<.*?>')
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

srcField = '英语单词'
tgtField = 'vocab'
noteType = "UVBasic-English"

# Get the model, and then the list of notes of that type
theModel = mw.col.models.by_name(noteType)
theNotes = mw.col.models.nids(theModel)

# Run through the list of notes
for nid in theNotes:
  # Get the note contents
  note = mw.col.get_note(nid)
  # Search the source field for the regexp
  if note[tgtField] != '':
    continue
  wordplain = cleanhtml(note[srcField])
  if wordplain not in dic.keys():
    continue
  note[srcField] = wordplain
  note[tgtField] = dic[wordplain]
  note.flush()

#   m = re.search(s, note[srcField])
#   # If there's a match...
#   if (m):
#     #... show what it found
#     print(m.group(0))
#     #... add it to the target field (comment out if just clearing unwanted content)...
#     note[tgtField] = m.group(0)
#     #... and remove it from the source field
#     note[srcField] = re.sub(s, '', note[srcField])
#     # save the changes
#     #note.flush()