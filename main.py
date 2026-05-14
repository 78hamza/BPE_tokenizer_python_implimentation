from bpe_tokenizer import BPE


def main():
    # ==========================================
    # STEP 1 — CREATE A TRAINING CORPUS
    # ==========================================

    corpus = {
        "low": 5,
        "lower": 2,
        "newest": 6,
        "widest": 3
    }

    # ==========================================
    # STEP 2 — CREATE THE TOKENIZER
    # ==========================================

    bpe = BPE(corpus)

    # ==========================================
    # STEP 3 — TRAIN BPE
    # ==========================================

    merges, vocab = bpe.train_bpe(num_merges=10)

    # ==========================================
    # STEP 4 — PRINT FINAL RESULTS
    # ==========================================

    print("========== FINAL MERGES ==========")
    print(merges)

    print("\n========== FINAL VOCAB ==========")
    for token, freq in vocab.items():
        print(token, ":", freq)

    # ==========================================
    # STEP 5 — ENCODE A NEW WORD
    # ==========================================

    word = "lowest"

    tokens = bpe.encode_pbe(word, merges)

    print("\n========== ENCODING ==========")
    print("Word:", word)
    print("Tokens:", tokens)

    # ==========================================
    # STEP 6 — DECODE TOKENS
    # ==========================================

    decoded = bpe.decode_bpe(tokens)

    print("\n========== DECODING ==========")
    print("Decoded word:", decoded)


if __name__ == "__main__":
    main()
