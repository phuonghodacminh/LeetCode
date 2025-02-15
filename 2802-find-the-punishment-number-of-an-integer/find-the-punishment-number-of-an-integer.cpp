class Solution {
public:
    int punishmentNumber(int n) {
        // int arr[] = {1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,909,918,945,964,990,991,999,1000};
        // for (int i = 1; i < 29; i++){
        //     arr[i] = arr[i - 1] + arr[i] * arr[i];
        //     cout << arr[i] << endl;
        // }
        // return 0;
        if (n < 9) return 1;
        else if(n < 10) return 82;
        else if(n < 36) return 182;
        else if(n < 45) return 1478;
        else if(n < 55) return 3503;
        else if(n < 82) return 6528;
        else if(n < 91) return 13252;
        else if(n < 99) return 21533;
        else if(n < 100) return 31334;
        else if(n < 235) return 41334;
        else if(n < 297) return 96559;
        else if(n < 369) return 184768;
        else if(n < 370) return 320929;
        else if(n < 379) return 457829;
        else if(n < 414) return 601470;
        else if(n < 657) return 772866;
        else if(n < 675) return 1204515;
        else if(n < 703) return 1660140;
        else if(n < 756) return 2154349;
        else if(n < 792) return 2725885;
        else if(n < 909) return 3353149;
        else if(n < 918) return 4179430;
        else if(n < 945) return 5022154;
        else if(n < 964) return 5915179;
        else if(n < 990) return 6844475;
        else if(n < 991) return 7824575;
        else if(n < 999) return 8806656;
        else if(n < 1000) return 9804657;
        else return 10804657;
    }
};