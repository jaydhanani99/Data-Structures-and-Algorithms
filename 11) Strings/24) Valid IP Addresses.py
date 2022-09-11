# https://www.interviewbit.com/old/problems/valid-ip-addresses/
# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def isValidIp(self, ip):
        ip = ip.split('.')
        n = len(ip)
        if n != 4:
            return False
        
        for i in range(n):
            int_ip_value = int(ip[i])
            # str(int_ip_value) != ip[i] that means it has leading zeros which is not valid
            if int_ip_value > 255 or str(int_ip_value) != ip[i]:
                return False
        return True
    
    def restoreIpAddresses(self, string: str) -> List[str]:
        # The idea is we would generate all the possible IP addresses by placing 3 "." (dots) at different position and check the corresponding IP is valid or not if valid we would add it to our output array
        output = []
        n = len(string)
        if n > 12:
            return []
        # Start placing the "." from 1st Index of string
        for i in range(1, n):
            # we would place second "." at i+1th position
            for j in range(i+1, n):
                # we would place third "." at j+1th position
                for k in range(j+1, n):
                    current_ip = ''.join([string[:i], '.', string[i:j], '.', string[j:k], '.', string[k:]])
                    if self.isValidIp(current_ip):
                        output.append(current_ip)
        return output
