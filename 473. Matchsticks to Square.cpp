class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if(nums.size()<4){
            return false;
        }    
        int sum = 0;
        for (int i=0; i<nums.size();i++){
            sum += nums[i];
        }
        if(sum%4){
            return false;
        }
        std::sort(nums.rbegin(), nums.rend());
        int side[4] = {0};
        return generate(0, nums, sum/4, side);
    }
private:
    bool generate(int i, std::vector<int> &nums, int target, int side[]){
        if (i >= nums.size()){
            return side[0]==target && side[1]==target &&
                   side[2]==target && side[3]==target;
        }
        for (int j = 0; j <4; j++){
            if(side[j]+nums[i] > target){
                continue;
            }
            side[j] += nums[i];
            if (generate(i+1, nums, target, side)){
                return true;
            }
            side[j] -= nums[i];
        }
        return false;
    }
};

/************************ Method 2 ************************/
#include <vector>

class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if(nums.size()<4){
            return false;
        }    
        int sum = 0;
        for (int i=0; i<nums.size();i++){
            sum += nums[i];
        }
        if(sum%4){
            return false;
        }
        int target = sum/4;
        std::vector<int> ok_sub;
        std::vector<int> ok_half;
        
        int all = 1<<nums.size();    
        for(int i=0; i < all; i++){
            int sum=0;
            for(int j=0; j < nums.size(); j++){
                if(i & 1<<j){
                sum += nums[j];
                }    
            }
            if(sum==target){
                ok_sub.push_back(i);
            }
        }
        for(int i=0; i < ok_sub.size(); i++){
            for(int j =i+1; j< ok_sub.size(); j++){
                if((ok_sub[i] & ok_sub[j])==0){
                    ok_half.push_back(ok_sub[i]|ok_sub[j]);
                }
            }
        }
        for (int i=0; i < ok_half.size(); i++){
            for(int j=i+1; j<ok_half.size(); j++){
                if((ok_half[i] & ok_half[j])==0){
                    return true;
                }
            }
        }
        return false;    
    }   
};
