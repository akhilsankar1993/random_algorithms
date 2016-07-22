# """Count words."""
#
# def count_words(s, n):
#     """Return the n most frequently occuring words in s."""
#
#     # TODO: Count the number of occurences of each word in s
#
#     # TODO: Sort the occurences in descending order (alphabetically in case of ties)
#
#     # TODO: Return the top n words as a list of tuples (<word>, <count>)
#     return top_n
#
#
# def test_run():
#     """Test count_words() with some inputs."""
#     print count_words("cat bat mat cat bat cat", 3)
#     print count_words("betty bought a bit of butter but the butter was bitter", 3)
#
#
# if __name__ == '__main__':
#     test_run()


def word_count(s, n=None):

    words = s.split(" ")
    word_count_array = []

    for word in words:
        if not word in map(lambda word_hash: word_hash["word"], word_count_array):
            word_count_array.append({"word": word, "count": words.count(word)})

    #key takes in one value and returns one value, before sort
    descending_word_count = sorted(
                                    word_count_array,
                                    key=lambda word_hash: word_hash["count"],
                                    reverse=True)

    # for i in xrange(0, n):



    print descending_word_count

word_count("betty bought a bit of butter but the bit of butter was bitter")
