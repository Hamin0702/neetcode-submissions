class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        counter = 0
        while counter < len(s):
            number = ""
            number_pos = counter
            while s[number_pos] != "#":
                number += s[number_pos]
                number_pos += 1
            number = int(number)

            string_start_pos = number_pos + 1
            substring = s[string_start_pos: string_start_pos + number]
            decoded_list.append(substring)

            counter = string_start_pos + number

        return decoded_list
