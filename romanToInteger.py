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
        depan = 0
        belakang = -1
        panjangList = len(s) - 1

        while s[depan] < panjangList or s[belakang] < panjangList:
            if kamus[s[depan]] > kamus[s[depan + 1]]:
                jumlah += kamus[s[depan]]
                depan += 1
            else:
                temp = kamus[s[depan + 1]] - kamus[s[depan]]
                jumlah += temp
                depan += 2