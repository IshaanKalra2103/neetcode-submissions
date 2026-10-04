class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the # after the length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Move past #
            j += 1

            # Take exactly `length` characters
            result.append(s[j:j + length])

            # Move to the next encoded string
            i = j + length

        return result
                    
