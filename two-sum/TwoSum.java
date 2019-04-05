import java.util.HashMap;
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> h1=new HashMap<>(); 
        for(int i=0; i<nums.length; i++){
            if(h1.containsKey(target - nums[i])){
                return new int[] {h1.get(target - nums[i]) , i}; 
            }
            h1.put(nums[i], i);
            
        }
        return null;
    }
}

