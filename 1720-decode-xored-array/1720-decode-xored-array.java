class Solution {
    public int[] decode(int[] encoded, int first) {
        
        int[] arr = new int[encoded.length+1];
        arr[0]=first;
        
        for(int i=0; i<arr.length-1;i++){
            arr[i+1] = encoded[i]^arr[i]; 
            //Carrot symbol, is XOR Operator. Refer: https://www.baeldung.com/java-xor-operator
        }
        
        return arr;
        
    }
}