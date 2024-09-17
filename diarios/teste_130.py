def uncommon_from_sentences(s1, s2):
    set_words = set()
    dup_set = set()

    # Split sentences into words
    words1 = s1.split()
    words2 = s2.split()

    # Process words from the first sentence
    for word in words1:
        if word not in dup_set:
            if word in set_words:
                set_words.remove(word)
                dup_set.add(word)
            else:
                set_words.add(word)

    # Process words from the second sentence
    for word in words2:
        if word not in dup_set:
            if word in set_words:
                set_words.remove(word)
                dup_set.add(word)
            else:
                set_words.add(word)

    return list(set_words)