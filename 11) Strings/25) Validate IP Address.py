# https://leetcode.com/problems/validate-ip-address/
# https://practice.geeksforgeeks.org/problems/validate-an-ip-address/1

class Solution:
    def validIPv4(self, ip):
        ip = ip.split('.')
        n = len(ip)
        if n != 4:
            return False
        
        for i in range(n):
            # checking for digit in string
            x_len = len(ip[i])
            if ip[i] == '':
                return False
            
            for j in range(x_len):
                if not ip[i][j].isdigit():
                    return False
                
            int_ip_value = int(ip[i])
            # str(int_ip_value) != ip[i] that means it has leading zeros which is not valid
            if int_ip_value > 255 or str(int_ip_value) != ip[i]:
                return False
        return True
    
    def validIPv6(self, ip):
        ip = ip.split(':')
        n = len(ip)
        if n != 8:
            return False
        
        for i in range(n):
            if ip[i] == '':
                return False
            x_len = len(ip[i])
            if x_len > 4:
                return False
            
            for j in range(x_len):
                # it should be digit or char should be between a and f
                if not ip[i][j].isdigit() and (ord(ip[i][j].lower()) < 97 or ord(ip[i][j].lower()) > 102):
                    return False
        return True
        
        
    def validIPAddress(self, IP: str) -> str:
        if self.validIPv4(IP):
            return "IPv4"
    
        if self.validIPv6(IP):
            return "IPv6"
        return "Neither"