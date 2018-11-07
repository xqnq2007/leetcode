# coding:utf-8

#762
import math
import copy
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        
        for i in range(L, R+1):
            binnumstr = bin(i).replace('0b', '')
            zhishunum = self.get1num(binnumstr)
            if self.iszhishu(zhishunum):
            	print('primenum:',zhishunum)
                res += 1
        
        return res
    
    def get1num(self, stra):
        res = 0
        for w in list(stra):
            if w == '1':
                res += 1
        return res
    
    def iszhishu(self,numa):
    	if numa == 1:
    		return False
        if numa == 2:
            return True
        sqrta = int(math.sqrt(numa))
        for i in range(2, sqrta+1):
            if numa % i == 0:
                return False
        return True

#s = Solution()
#print(s.countPrimeSetBits(244, 269))

#771

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for w in S:
            if w in J:
                res += 1
        return res

    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        dandiaomark = True
        if len(A) <= 2:
            return True
        num0 = A[0]
        num1 = A[0]
        idx1 = 0
        lena = len(A)
        for i, num in enumerate(A):
            if num == num0:
                continue
            else:
                num1 = num
                idx1 = i
                break
        if num0 > num1:
            dandiaomark = False
        if i == lena - 1:
            return True
        for j in range(i, lena-1):
            if A[j] < A[j+1] and not dandiaomark:
                return False
            if A[j] > A[j+1] and dandiaomark:
                return False
        return True

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        lightnums = []
        lightnumslist = []
        rawlist = [0] * 10
        #print(rawlist)
        if num == 0:
            return ["0:00"]
        self.getarrangelist(num, lightnumslist, rawlist)
        #print(lightnumslist)
        res = self.maketimelist(lightnumslist)
        res_sort = sorted(res, reverse=False)
        return list(set(res))
    
    def getarrangelist(self, num, lightnumslist, rawlist):
        if num == 0:
            lightnumslist.append(rawlist)
            return
        for i, w in enumerate(rawlist):            
            curnum = num
            curlist = copy.deepcopy(rawlist)            
            if w == 0:
                curnum -= 1
                curlist[i] = 1                
                
                self.getarrangelist(curnum, lightnumslist, curlist)
                
    def maketimelist(self, lightnumslist):
        res = []
        for nums in lightnumslist:
            hour = 8 * nums[0] + 4 * nums[1] + 2 * nums[2] + 1 * nums[3]
            minute = 32 * nums[4] + 16 * nums[5] + 8 * nums[6] + 4 * nums[7] + 2 * nums[8] + 1 * nums[9]
            if hour >= 12 or minute >= 60 :
                continue
            
            if minute < 10:
                curtime = str(hour) + ':0' + str(minute)
            else:
                curtime = str(hour) + ':' + str(minute)
            res.append(curtime)
        return res

    def readBinaryWatch2(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from itertools import combinations
        ref = [1,2,4,8,16,32,64,128,256,512]
        st = set()
        for x in combinations(ref, num):
            top = sum(i for i in x if i <= 8)
            bottom = sum(i//16 for i in x if i >= 16)
            if top < 12 and bottom < 60:
                st.add((top, bottom))
        
        result = []
        for hour, minute in st:
            result.append(str(hour) + ':' + str(minute).rjust(2, '0'))
        return sorted(result)

#s = Solution()
#print(s.numJewelsInStones('aA', 'aAAbbbb'))
s = Solution()
A = [1, 2, 2, 3]
res = s.readBinaryWatch2(2)
print(res, len(res))

# tmplist_output = ["10:24","9:24","6:48","2:37","10:48","10:40","9:33","10:12","6:24","0:54","3:09","3:33","3:17","4:11","1:14","1:28","9:03","5:40","6:03","4:50","8:37","8:42","4:07","6:09","1:52","8:28","0:45","4:22","4:56","5:48","9:12","7:01","6:17","2:42","10:36","1:50","9:40","1:13","5:03","2:25","5:12","4:19","8:14","4:14","8:21","8:50","1:19","1:26","5:05","2:11","0:60","2:21","2:41","10:17","1:25","5:33","3:36","9:20","9:36","10:18","8:56","4:42","9:18","3:24","7:04","0:46","3:40","2:44","8:41","0:27","5:36","6:40","3:18","9:10","4:49","1:07","0:43","0:39","8:25","8:49","1:56","11:02","2:52","0:23","8:26","6:06","8:35","0:53","1:44","8:11","4:28","6:18","2:14","2:50","2:35","4:21","8:22","7:02","3:03","10:20","8:44","7:32","4:37","10:10","11:01","8:19","1:42","5:10","5:06","0:29","9:06","9:05","4:38","2:28","3:12","1:49","7:08","4:52","6:36","3:34","5:09","0:51","6:05","3:05","11:04","10:03","6:33","2:56","2:19","4:41","10:06","5:17","8:52","7:16","2:49","0:58","0:57","8:13","4:13","11:16","2:07","3:10","2:38","1:35","4:25","1:21","5:18","6:20","4:44","11:08","1:41","5:20","1:38","9:34","6:12","11:32","5:24","4:35","1:37","0:15","3:20","2:22","8:07","4:26","10:09","10:33","3:06","2:13","5:34","8:38","6:10","9:48","6:34","9:17","10:05","9:09","0:30","2:26","3:48","1:22","1:11","10:34"]
# tmplist_expected = ["0:15","0:23","0:27","0:29","0:30","0:39","0:43","0:45","0:46","0:51","0:53","0:54","0:57","0:58","1:07","1:11","1:13","1:14","1:19","1:21","1:22","1:25","1:26","1:28","1:35","1:37","1:38","1:41","1:42","1:44","1:49","1:50","1:52","1:56","2:07","2:11","2:13","2:14","2:19","2:21","2:22","2:25","2:26","2:28","2:35","2:37","2:38","2:41","2:42","2:44","2:49","2:50","2:52","2:56","3:03","3:05","3:06","3:09","3:10","3:12","3:17","3:18","3:20","3:24","3:33","3:34","3:36","3:40","3:48","4:07","4:11","4:13","4:14","4:19","4:21","4:22","4:25","4:26","4:28","4:35","4:37","4:38","4:41","4:42","4:44","4:49","4:50","4:52","4:56","5:03","5:05","5:06","5:09","5:10","5:12","5:17","5:18","5:20","5:24","5:33","5:34","5:36","5:40","5:48","6:03","6:05","6:06","6:09","6:10","6:12","6:17","6:18","6:20","6:24","6:33","6:34","6:36","6:40","6:48","7:01","7:02","7:04","7:08","7:16","7:32","8:07","8:11","8:13","8:14","8:19","8:21","8:22","8:25","8:26","8:28","8:35","8:37","8:38","8:41","8:42","8:44","8:49","8:50","8:52","8:56","9:03","9:05","9:06","9:09","9:10","9:12","9:17","9:18","9:20","9:24","9:33","9:34","9:36","9:40","9:48","10:03","10:05","10:06","10:09","10:10","10:12","10:17","10:18","10:20","10:24","10:33","10:34","10:36","10:40","10:48","11:01","11:02","11:04","11:08","11:16","11:32"]
# print(len(tmplist_output), len(tmplist_expected))
# print(list(set(tmplist_output)-set(tmplist_expected)))
tmp = {'a', 'a', 'b', 'b'}
print(tmp)

from itertools import combinations
test_data = ['a', 'a', 'a', 'b']
for i in combinations(test_data, 2):
    print i
