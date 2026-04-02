class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """
        kamus ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 100          
        }
        jumlah = 0
        indeksAkhir = 0
        indeksAwal = -1
        panjangList = len(s) - 1

        while s[indeksAkhir] < panjangList or s[indeksAwal] < panjangList:
            if kamus[s[indeksAkhir]] > kamus[s[indeksAkhir + 1]]:
                jumlah += kamus[s[indeksAkhir]]
                indeksAkhir += 1
            else:
                temp = kamus[s[indeksAkhir + 1]] - kamus[s[indeksAkhir]]
                jumlah += temp
                indeksAkhir += 2

        # for indeksAwal in s:
        #     indeksAkhir = indeksAwal + 1
        #     if kamus[s[indeksAkhir]] < kamus[s[indeksAwal]]:
        #         jumlah = kamus[s[indeksAwal]]
        #     else:

                