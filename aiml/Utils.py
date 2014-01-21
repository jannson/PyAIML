#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LangSupport import splitChinese

"""This file contains assorted general utility functions used by other
modules in the PyAIML package.

"""

# TODO: andelf, add chinese sentence support
def sentences(s):
    """Split the string s into a list of sentences."""
    try: s+""
    except: raise TypeError, "s must be a string"
    s = u"".join(splitChinese(s))
    pos = 0
    sentenceList = []
    l = len(s)
    while pos < l:
        try: p = s.index('.', pos)
        except: p = l+1
        try: q = s.index('?', pos)
        except: q = l+1
        try: e = s.index('!', pos)
        except: e = l+1
        try: f = s.index('~', pos)
        except: f = l+1
        end = min(p,q,e,f)
        sentenceList.append( s[pos:end].strip() )
        pos = end+1
    # If no sentences were found, return a one-item list containing
    # the entire input string.
    if len(sentenceList) == 0: sentenceList.append(s)
    return sentenceList

# Self test
if __name__ == "__main__":
    # sentences
    sents = sentences("First.  Second, still?  Third and Final!  Well, not really")
    print sents
    sents = sentences(u'2005年我们出去玩2，然后聘情况！知道道理5abc如何走。')
    for s in sents:
        print s, ' / ',
    #assert(len(sents) == 4)
