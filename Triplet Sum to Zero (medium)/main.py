class Solution:
  def search_triplets(self, arr):
      arr.sort()  # [-3, -2, -1, 0, 1, 1, 2]
      triples=[]
      left=0
      right= len(arr) -1
      i =0
      while i < right:
          value= self.finding_the_two_sum(arr,- arr[i],i)

          if value == 0:
              i = i+1
          else:
              i = i + 1
              list_of_three=[arr[i],value[0],value[1]]
              triples.append(list_of_three)


      return triples






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
              return arr[left], arr[right]


      return 0




def main():
  sol = Solution()
  print(sol.search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(sol.search_triplets([-5, 2, -1, -2, 3]))


main()