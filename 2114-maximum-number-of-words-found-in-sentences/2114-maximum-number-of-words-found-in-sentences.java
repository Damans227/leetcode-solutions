class Solution {
    public int mostWordsFound(String[] sentences) {
      int max = 0;
        // The string split() method breaks a given string around matches of the given regular expression. 
        // After splitting against the given regular expression, this method returns a char array.
        for (String s: sentences) {
            max = Math.max(max, s.split(" ").length);
        }
        return max;
        
    }
}