class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = defaultdict(int)
        for n in nums:
            count_hash[n] += 1
        sorted_count_hash = sorted(count_hash.items(), reverse=True, key=lambda x : x[1])
        final_k_elem = []
        for x in range(k):
            final_k_elem.append(sorted_count_hash[x][0])
        return final_k_elem
