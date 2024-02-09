# asked user for input, then replaced text with emoticon and assigned to var
emoticon = (
    input("what do your want to convert? ")
    .replace((":)"), ("🙂"))
    .replace((":("), ("🙁"))
)

# output
print(emoticon)
