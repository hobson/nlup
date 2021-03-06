# Copyright (C) 2015 Kyle Gorman
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# util.py: tools for NLP feature extraction (mostly)


from re import sub


NUMBER_WORDS = frozenset("""
    zero one two three four five six seven eight nine ten eleven twelve
    thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
    thirty fourty fifty sixty seventy eighty ninety hundred thousand million
    billion trillion quadrillion
    zeros ones twos threes fours fives sixs sevens eights nines tens elevens
    twelves thirteens fourteens fifteens sixteens seventeens eighteens
    nineteens twenties thirties fourties fifties sixties seventies eighties
    nineties hundreds thousands millions billions trillions quadrillions
    """.upper().split())


def isnumberlike(token):
    """True iff `token` str matches a relatively broad definition of numberhood"""
    # remove /[.,/]/
    token = sub(r"[.,/]", "", token)
    # generic digit
    if token.isdigit():
        return True
    # number words
    if all(part in NUMBER_WORDS for part in token.split("-")):
        return True
    return False


def case_feature(token):
    """
    Returns zero or one case features for the `token` string
    """
    if token.islower():
        return "*lowercase*"
    if token.isupper():
        return "*uppercase*"
    if token.istitle():
        return "*titlecase*"
    return
