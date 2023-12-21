class Solution:

  triples = []
  def search_triplets(self, arr):
      arr.sort()  # [-3, -2, -1, 0, 1, 1, 2]

      left=0
      right= len(arr) -1
      i =0
      while i < right:

          value= self.finding_the_two_sum(arr,- arr[i],i)
          i = i+1


      return self.triples






  def finding_the_two_sum(self,arr ,target ,start_of_left):
      left = start_of_left+1
      right= len(arr)-1
      while(left<right):
          sum= arr[left]+ arr[right]

          if sum < target:
              left =left+1

          elif sum > target :
               right= right-1

          else:
              list =[arr[start_of_left], arr[left], arr[right]]
              self.triples.append(list)
              left= left+1
              right=right-1


      return 0




def main():
  sol = Solution()
  print(sol.search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  sol.triples=[]
  print(sol.search_triplets([-5, 2, -1, -2, 3]))


main()