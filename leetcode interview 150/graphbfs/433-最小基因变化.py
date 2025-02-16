from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = {startGene} if startGene in bank else set()
        q = deque([startGene])
        count = 0
        
        def check(gene1: str, gene2: str) -> bool:
            n, m = len(gene1), len(gene2)
            if n != m: return False
            flag = False
            for i in range(n):
                if gene1[i] != gene2[i]:
                    if flag:
                        return False
                    else:
                        flag = True
            return flag  
        
        while q:
            count += 1
            nxt = []
            while q: 
                startGene = q.popleft()
                for gene in bank:
                    if gene not in visited and check(startGene, gene):
                        if gene == endGene: 
                            return count
                        else: 
                            visited.add(gene)
                            nxt.append(gene)
            q.extend(nxt)
        
        return -1
    
if __name__ == "__main__":
    # startGene, endGene = "AACCGGTT", "AACCGGTA"
    # bank = ["AACCGGTA"]
    startGene, endGene = "AAAAAAAA", "CCCCCCCC"
    bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
    print(Solution().minMutation(startGene, endGene, bank))