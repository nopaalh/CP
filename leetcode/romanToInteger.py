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
            "M" : 1000          
        }
        jumlah = 0
        indeksAkhir = 0
        indeksAwal = 0
        panjangList = len(s)

        while indeksAwal < panjangList:
            if indeksAwal == panjangList - 1:
                jumlah += kamus[s[indeksAwal]]
                break
            
            elif kamus[s[indeksAwal]] >= kamus[s[indeksAwal + 1]]:
                jumlah += kamus[s[indeksAwal]]
                indeksAwal += 1
            else:
                temp = kamus[s[indeksAwal + 1]] - kamus[s[indeksAwal]]
                jumlah += temp
                indeksAwal += 2

        return jumlah

                