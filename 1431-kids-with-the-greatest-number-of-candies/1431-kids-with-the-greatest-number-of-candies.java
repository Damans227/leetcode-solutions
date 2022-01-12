class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        List<Boolean> result = new ArrayList<Boolean>();
        
        int maxCandy = 0;
        for(int i : candies){
            maxCandy= Math.max(maxCandy, i);
        }
        
        for(int j : candies){
            if((j+extraCandies) >= maxCandy){
                result.add(true);
            }
            else{
                result.add(false);
            }
        }
        return result;
        
    }
}