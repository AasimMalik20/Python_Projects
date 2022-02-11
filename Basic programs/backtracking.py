def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1
        
def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            st.add(v[j])
      sets.append(st)
      
def main():
    v = [8,13,3]
    subsets = []
    get_all_subsets(v, subsets);
    print("Total: " + str(len(subsets)))
    for i in range(0, len(subsets)):
        print( end = "")
        print(subsets[i], end = "")
    print("Total: " + str(len(subsets)))   

main()