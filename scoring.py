def berechne_score(kurs_30, kurs_7, volumen):

    score = kurs_30 * 0.7 + kurs_7 * 0.3 + (volumen / 20000000)

    return score
