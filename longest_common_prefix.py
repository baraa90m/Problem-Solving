
class LongestCommonPrefix:
    """
    This class finds the longest common prefix
    string amongst an array of strings.
    """

    def __init__(self, strs: list[str]):
        self.strs = strs
        self.longest_common_prefix = ""

    def longestCommonPrefix(self) -> str:

        if not self.strs:
            return "The list is empty."
        shortest_string = min(self.strs, key=len)
        for i in range(len(shortest_string)):
            prefix = shortest_string[:i+1]
            if all(s.startswith(prefix) for s in self.strs):
                self.longest_common_prefix = prefix
            else:
                break
        if self.longest_common_prefix:
            return f"The longest common prefix is '{self.longest_common_prefix}'."
        else:
            return "The words in the given list have no common list."

obj = LongestCommonPrefix(["flower", "flight", "flow"])
result = obj.longestCommonPrefix()
print(result)