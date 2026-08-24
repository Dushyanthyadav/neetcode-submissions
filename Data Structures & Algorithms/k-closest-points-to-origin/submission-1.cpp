class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        map<double, vector<vector<int>>> distanceMap;

        for (vector<int> point: points) {
            int x = point[0];
            int y = point[1];
            double distance = sqrt(x*x + y*y);
            distanceMap[distance].push_back({x, y});
        }

        vector<vector<int>> result;
        for (const auto &[dist, point]: distanceMap) {
            for (const auto num: point) {
                result.push_back(num);
                k--;
                if(k<=0) {
                    return result;
                }
            }
        }

        return result;
    }
};
