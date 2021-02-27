from random import choice, choices


class Answer:
    POSITIVE = [
        'oh ya',
        'yep',
        'of course',
        'well, I guess anything is possible...',
        'definitely',
        'ya!',
        'there\'s a good chance of it',
    ]

    NEGATIVE = [
        'nope',
        'probably not',
        'not a chance',
        'not likely...',
        'ha!',
        'did hell freeze over?',
        'no',
        'you\'re kidding, right?',
    ]

    @staticmethod
    def negative():
        """ Always returns an answer with a negative sentiment. """
        return choice(Answer.NEGATIVE)

    @staticmethod
    def positive():
        """ Always returns an answer with a positive  sentiment. """
        return choice(Answer.POSITIVE)

    # TODO: Change this to take weights for positive and negative sentiments when the will-they-win endpoint is changed.
    @staticmethod
    def any():
        """ Returns a random answer with any sentiment. """
        all_answers = Answer.POSITIVE + Answer.NEGATIVE
        return choices(all_answers)[0]
