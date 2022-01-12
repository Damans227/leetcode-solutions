class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth=0;
        
        for(int[] arr : accounts){
            int sum=0;
            for(int i : arr){
                sum += i;
            }
            
             maxWealth = Math.max(maxWealth, sum);
        }
        
        return maxWealth;
    }
}