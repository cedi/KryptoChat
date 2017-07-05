def int2word(n):
    # break the number into groups of 3 digits using slicing
    # each group representing hundred, thousand, million, billion, ...

    n3 = []

    # create numeric string
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k

        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))

    # break each group of 3 digits into
    # ones, tens/twenties, hundreds
    # and form a string
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        #print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + "hundred " + nw
    return nw

############# globals ################
ones = ["", "eins ", "zwei ", "drei ", "vier ", "fünf ",
        "sechs ", "sieben ", "acht ", "neun "]

tens = ["zehn ", "elf ", "zwölf ", "dreizehn ",  "vierzehn ",
        "fünfzehn ", "sechszehn ", "siebzehn ", "achtzehn ", "neunzehn "]

twenties = ["", "", "zwanzig ", "dreisig ", "vierzig ",
            "fünfzig ", "sechzig ", "siebzig ", "achtzig ", "neunzig "]

thousands = ["", "tausend ", "million ",  "billion ",  "trillion ",
             "quatrillion ",  "quintillion ",  "sextillion ",  "septillion ",
             "octillion ", "nonillion ",  "decillion ",  "undecillion ",
             "duodecillion ",  "tredecillion ", "quattuordecillion ",
             "quindecillion", "sexdecillion ", "septendecillion ",
             "octodecillion ", "novemdecillion ", "vigintillion "]
