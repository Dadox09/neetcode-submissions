class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #i've an array composed by numbers. if some of this numbers appears more then 1 -> true, false otherwise
        #checking all items in array once after the other will be O(n) in the worst case, where n is the array lenght
        #even if we order the array with a log n method and then we search iterativly we have same complexity time, maybe. 
        #required O(n) so start with iterative once item after the other
        return len(set(nums)) < len(nums)

