class Solution {
    public int[] decompressRLElist(int[] nums) {
        
        List<Integer> result = new ArrayList<Integer>();   
        
        for(int i = 0; i<nums.length; i+=2){
            int freq=i;
            int val=freq+1;
            
            while(nums[freq]>0){
                result.add(nums[val]);
                nums[freq]--;
            }
            
        }
        
       int[] arr = new int[result.size()];
        
        for(int j=0; j<result.size();j++){
            arr[j]=result.get(j);
        }
           
        return arr;
    }
}