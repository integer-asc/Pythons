from kbbi import KBBI

WORD = "tembok"
WORD = WORD.lower() #im gay

kata = KBBI(WORD)
ser = kata.serialisasi()

#UGLY CODE BEGINS
try:
    StopLoop = False
    for Item in ser["entri"][0]["makna"]:
        if StopLoop:
            break
        if Item["kelas"]:
            for Item2 in Item["kelas"]:
                if Item2["deskripsi"] and "benda" in Item2["deskripsi"]:
                    print("Kata Benda")
                    StopLoop = True
    if not StopLoop:
        print("Bukan Kata Benda")
except KeyError:
    print("Key Error")
except IndexError:
    print("Index Error")
#UGLY CODE ENDS
