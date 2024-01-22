class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        
        res = ""

        for ch in path + '/':
            if ch == '/':
                if res == "..":
                    if st:
                        st.pop()
                
                elif res != "" and res != ".":
                    st.append(res)
                res = ""
            else:
                res += ch
        
        return "/" + "/".join(st)