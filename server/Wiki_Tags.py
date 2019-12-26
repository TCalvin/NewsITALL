import wikipedia


def get_related_tags(term):
    wikipedia.set_lang('en')
    results = wikipedia.search(term)
    to_Return = list()
    for result in results:
        to_Return.append(result)
    return to_Return


"""
print(get_related_tags("Donald Trump"))
"""