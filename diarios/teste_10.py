def deckRevealedIncreasing(deck):
    from collections import deque

    deck.sort()

    n = len(deck)
    result = [0] * n
    indices = deque(range(n))

    for card in deck:
        idx = indices.popleft()
        result[idx] = card
        if indices:
            indices.append(indices.popleft())

    return result


print(deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
