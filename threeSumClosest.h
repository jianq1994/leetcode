class Solution{
public:
    int threeSumClosest(vector<int>& nums, int target){
        sort(nums.begin(),nums.end());
        int res = nums[0] + nums[1] + nums[2];
        int sum = 0;
        int size = nums.size()
        for(int i=0;i<size-1;i++){
            int j = i + 1, k = size - 1;
            while(j<k){
                sum = nums[i] + nums[j] + nums[k];
                if(abs(sum-target)<abs(res-target)) res = sum;
                if(sum<target) j++;
                else if(sum>target) k--;
                else return target;
            }
        }
        return res;
    }
};