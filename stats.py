def count_words(booktext):
    wordlist = booktext.split()
    wordcount = len(wordlist)
    return(wordcount)

def count_letters(booktext):
    lettercount = {}
    booktext = booktext.lower()
    for char in booktext:
        if char not in lettercount:
            lettercount[char] = 1
        else:
            lettercount[char] += 1
    return(lettercount)

def sort_letters(unsorted):
    list_dict = []
    for char in unsorted:
        if char.isalpha():
            chardict = {}
            if char not in chardict:
                count = unsorted[char] 
                chardict = {"letter":char, "num":count}
            list_dict.append(chardict)
            results = sorted(list_dict, key = lambda d: d['num'], reverse = True)
    return(results)