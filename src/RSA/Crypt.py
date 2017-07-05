from binascii import hexlify


def encrypt(RSA, exponent, plainText):

    cipperText = str()

    # Zeichen für Zeichen
    for plainChar in plainText:
        # Als Binärdaten encodieren
        encodedChar = plainChar.encode()

        # In Hexadezimal-Zahl umwandeln
        hexChar = hexlify(encodedChar)

        # Hex-Wert in int-Wert darstellen
        plainChar = int(hexChar, 16)

        # Verschlüsselungsvorgang
        cipperChar = plainChar ** exponent % RSA

        # Zahl wieder in Hex umwandeln
        cipperChar = hex(cipperChar)

        # das "0x" vom Hex abschneiden
        cipperChar = cipperChar[2:]

        # und nun noch anhängen
        cipperText = "{}:{}".format(cipperText, cipperChar)

    # letzter zuvieler Doppelpunkt abschneiden und String zurückgeben
    return cipperText[1:]


def decrypt(RSA, exponent, cipperText):

    plainText = str()

    # String an den Doppelpunkten wieder aufsplitten
    cipperArray = cipperText.split(":")

    # Zeichen für Zeichen
    for cipperChar in cipperArray:
        # Aus dem Hex-String wieder eine Zahl machen
        cipperChar = int(cipperChar, 16)

        # Entschlüsseln
        plainChar = cipperChar ** exponent % RSA

        # und wieder ein Zeichen daraus machen
        plainChar = chr(plainChar)

        # un nun noch anhängen
        plainText = "{}{}".format(plainText, plainChar)

    return plainText
