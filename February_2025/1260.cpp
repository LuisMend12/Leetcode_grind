class Solution {
    public:
        vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
            int m = grid.size(), n = grid[0].size();
            int total = m * n;
            k = k % total;
    
            vector<int> flatGrid;
            for (const auto& row : grid)
                for (int num : row) flatGrid.push_back(num);
            
            vector<int> shifted(total);
            for (int i = 0; i < total; i++) {
                shifted[(i + k) % total] = flatGrid[i];
            }
    
            vector<vector<int>> result(m, vector<int>(n));
            for (int i = 0; i < total; i++) result[i / n][i % n] = shifted[i];
    
            return result;
        }
    };