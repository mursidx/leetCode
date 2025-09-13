class Solution:
    def minCost(self, n, m, x, y):
        # Sort costs in descending order
        x.sort(reverse=True)
        y.sort(reverse=True)
        
        i, j = 0, 0
        h_segments, v_segments = 1, 1
        cost = 0
        
        # Greedy selection
        while i < len(x) and j < len(y):
            if x[i] > y[j]:
                cost += x[i] * h_segments
                v_segments += 1
                i += 1
            else:
                cost += y[j] * v_segments
                h_segments += 1
                j += 1
        
        # Remaining cuts in x
        while i < len(x):
            cost += x[i] * h_segments
            v_segments += 1
            i += 1
        
        # Remaining cuts in y
        while j < len(y):
            cost += y[j] * v_segments
            h_segments += 1
            j += 1
        
        return cost
