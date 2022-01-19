class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=" " #Initialize an empty string to be used as a seperator for the join method
        sList=s.split(" ")
        truncatedList = sList[:k] #Truncate the list upto k cahracters via slicing
        return res.join(truncatedList) #use join() method to convert list to a string
