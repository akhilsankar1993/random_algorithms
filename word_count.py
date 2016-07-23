"""Count words."""

def count_words(s, n):
    words = s.split(" ")
    word_count_array = []

    for word in words:
        if not word in map(lambda word_hash: word_hash["word"], word_count_array):
            word_count_array.append({"word": word, "count": words.count(word)})

    descending_word_count = sorted(
                                    word_count_array,
                                    key=lambda word_hash: word_hash["count"],
                                    reverse=True)

    max_count = descending_word_count[0]["count"]

    all_sorted_hashes = []
    for count in reversed(range(1, max_count+1)):
        count_group = []
        for word_hash in descending_word_count:
            if word_hash["count"] == count:
                count_group.append(word_hash)
        alphabetized_group = sorted(count_group)
        for word_hash in alphabetized_group:
            converted_tuple = (word_hash["word"], word_hash["count"])
            all_sorted_hashes.append(converted_tuple)

    top_n = all_sorted_hashes[:n]

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
