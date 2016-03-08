"""
Source code for QA object class
disabled pylint R0903: Class is small but necessary
"""
# pylint: disable=R0903


class QA(object):
    """
    Question/Answer object class to support interface.
    """
    def __init__(self, question, answer):
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
