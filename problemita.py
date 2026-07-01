def segment_encoded_sequence(
        sequence: list[int],
        max_length: int,
        n_overlap: int
) -> list[list[int]]:
    """Segment a long encoded sequence into overlapping subsequences of maximum
    length.

    Divides the input sequence into chunks of max_length tokens with specified
    overlap between consecutive segments. The final segment may be shorter than
    max_length if insufficient tokens remain.

    Args:
        sequence: List of token indices to segment.
        max_length: Maximum length for each subsequence.
        n_overlap: Number of tokens to overlap between consecutive segments.

    Returns:
        List of subsequences, each with at most max_length token indices. All
        segments except possibly the last will have exactly max_length tokens.
    """
    subsequences = []
    lenght = len(sequence)
    for index in range(lenght):
      for subindex in range(0, max_length):
        subsequences.append(sequence[max_length - n_overlap])

    return subsequences



def segment_encoded_sequence(
        sequence: list[int],
        max_length: int,
        n_overlap: int
) -> list[list[int]]:
    """Segment a long encoded sequence into overlapping subsequences of maximum
    length.

    Divides the input sequence into chunks of max_length tokens with specified
    overlap between consecutive segments. The final segment may be shorter than
    max_length if insufficient tokens remain.

    Args:
        sequence: List of token indices to segment.
        max_length: Maximum length for each subsequence.
        n_overlap: Number of tokens to overlap between consecutive segments.

    Returns:
        List of subsequences, each with at most max_length token indices. All
        segments except possibly the last will have exactly max_length tokens.
    """
    subsequences = []

    # Add your code here to:
    #
    # 1. Repeatedly take a segment of (up to) `max_length` from the sequence.
    #
    # 2. Ensure that is an overlap of n_overlap between consecutive
    #    subsequences.
    #
    #    This means that for each valid index `i` in `subsequences`, the
    #    elements in `subsequences[i][:n_overlap]` are the same as those in
    #    `subsequences[i+1][-n_overlap:]`.
    #
    # 3. Handle the case when the final segment may be shorter than max_length.
    #
    #    The final subsequence, subsequences[-1], can be up to max_length in
    #    length but can be shorter. All other subsequences must have exactly
    #    max_length elements.
    step = max_length - n_overlap
    
    for i in range(0, len(sequence), step):
        segment = sequence[i:i + max_length]
        subsequences.append(segment)

    return subsequences

list(text)
"".join(tokens)