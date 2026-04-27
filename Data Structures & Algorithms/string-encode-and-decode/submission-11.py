class Solution:

    def encode(self, strs: List[str]) -> str:
        for index,string in enumerate(strs):
            if(string == ""):
                print(f"Reached the case, before the string is {string}")
                strs[index] = f"\"\""
                print(f"Now the string is {strs[index]}")

        print(strs)

        ans_string = '||||||||'.join(strs)
        print(ans_string)
        return ans_string

    def decode(self, s: str) -> List[str]:
            if(s == ""):
                ans_list = []
                return ans_list
                
            ans_list = s.split("||||||||")

            for index,string in enumerate(ans_list):
                if(string == f"\"\""):
                    ans_list[index] = ""
            return ans_list
