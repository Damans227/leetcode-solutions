class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        
        int[] arr = new int[nums.length];
        
            for(int i=0; i<=nums.length-1; i++){
                
                int countHighest=0;
                
                int check = nums[i];
                
                for(int j=0; j<=nums.length-1; j++){
                
                if(j!=i && nums[j] < nums[i]){
                    countHighest += 1; 
                }    
                    
                }  
                
                arr[i] = countHighest;       
            }
        
        return arr;
        
    }
}
