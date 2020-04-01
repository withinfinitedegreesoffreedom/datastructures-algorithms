class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if secret == "" or guess == "":
            return ""
            
        secret_dict = dict()
        guess_dict = dict()
        A = 0
        B = 0
        for n in range(0, len(secret)):
            if secret[n] in secret_dict:
                secret_dict[secret[n]] += 1
            else:
                secret_dict[secret[n]] = 1
                
        for n in range(0, len(guess)):
            if guess[n] in guess_dict:
                guess_dict[guess[n]] += 1
            else:
                guess_dict[guess[n]] = 1      
            
        for n in range(0, len(secret)):
            if secret[n] == guess[n]:
                A += 1
                secret_dict[secret[n]] -= 1
                guess_dict[guess[n]] -= 1
                
        for key, val in secret_dict.items():
            if key in guess_dict and guess_dict[key] == val:
                B += val
            elif key in guess_dict and guess_dict[key] < val:
                B += guess_dict[key]
            elif key in guess_dict and guess_dict[key] > val:
                B += val
            elif val == 0:
                pass
                                
        return str(A)+"A"+str(B)+"B"

s = Solution()
print(s.getHint("1122", "2211"))