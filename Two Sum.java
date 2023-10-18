import java.util.HashMap;

class Two_Sum {

    public static void main(String[] args) {

        Two_Sum out = new Two_Sum();
        Solution s = out.new Solution();

        int[] a = {2, 7, 11, 15};
        int target = 9;

        int[] result = s.twoSum(a, target);

        for (int each : result) {
            System.out.println(each);
        }
    }

    // time: O(N)
    // space: O(N)
    public class Solution {

        public int[] twoSum(int[] nums, int target) {

            // set up hashmap: remaining to original. thread-unsafe but for here is ok
            HashMap<Integer, Integer> hm = new HashMap<>();

            for (int i = 0; i < nums.length; i++) {

                // if key in hm, result found.
                // so that only one pass
                if (hm.containsKey(nums[i])) {
                    int otherIndex = hm.get(nums[i]);

                    return new int[]{Math.min(i, otherIndex) + 1, Math.max(i, otherIndex) + 1};
                }
                // put new record into hashmap
                else {
                    hm.put(target - nums[i], i);
                }
            }

            return null;
        }

    }
}

############

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0;; ++i) {
            int x = nums[i];
            int y = target - x;
            if (m.containsKey(y)) {
                return new int[] {m.get(y), i};
            }
            m.put(x, i);
        }
    }
}
