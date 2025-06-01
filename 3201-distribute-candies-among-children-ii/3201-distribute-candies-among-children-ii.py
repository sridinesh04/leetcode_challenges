class Solution:
  def distributeCandies(self, n: int, limit: int) -> int:
    def ways(n: int) -> int:
      """Returns the number of ways to distribute n candies to 3 children."""
      if n < 0:
        return 0
      return math.comb(n + 2, 2)

    limitPlusOne = limit + 1
    oneChildExceedsLimit = ways(n - limitPlusOne)
    twoChildrenExceedLimit = ways(n - 2 * limitPlusOne)
    threeChildrenExceedLimit = ways(n - 3 * limitPlusOne)
    return (ways(n)
            - 3 * oneChildExceedsLimit
            + 3 * twoChildrenExceedLimit
            - threeChildrenExceedLimit)