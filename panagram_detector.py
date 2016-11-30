from string import letters, punctuation


class PanagramDetector(object):

    def findMissingLetters(self, sentence):
        result = ''.join(sorted(list(set(letters[:26]) ^ set(sentence.lower()))))
        for p in punctuation:
            result = result.replace(p, '')
        return result.strip()

if __name__ == '__main__':
    # Default
    print 'Default: {}'.format(
        PangramDetector().findMissingLetters(
            sentence='The quick brown fox jumps over the lazy dog'
        )
    )

    # Example 1
    print 'Example 1: {}'.format(
        PangramDetector().findMissingLetters(
            sentence='The slow purple oryx meanders past the quiescent canine'
        )
    )

    # Example 2
    print 'Example 2: {}'.format(
        PangramDetector().findMissingLetters(
            sentence='We hates Bagginses!'
        )
    )

    # Example 3
    print 'Example 3: {}'.format(
        PangramDetector().findMissingLetters(
            sentence=''
        )
    )
