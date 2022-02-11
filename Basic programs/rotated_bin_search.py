def binary_search(arr, start, end, key):
  # assuming all the keys are unique.
  
  if (start > end):
    return -1;

  mid = int(start + (end - start) / 2)

  if arr[mid] == key:
    return mid
    
  if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
    return binary_search(arr, start, mid - 1, key)
  
  elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]: 
    return binary_search(arr, mid + 1, end, key)

  elif arr[end] <= arr[mid]:
    return binary_search(arr, mid + 1, end, key)

  elif arr[start] >= arr[mid]:
    return binary_search(arr, start, mid - 1, key)

  return -1;

def binary_search_rotated(arr, key):
  return binary_search(arr, 0, len(arr)-1, key)

v1 = [6, 7, 1, 2, 3, 4, 5];
  
print("Key(3) found at: " + str(binary_search_rotated(v1, 3)))
print("Key(6) found at: " + str(binary_search_rotated(v1, 6)))
  
v2 = [4, 5, 6, 1, 2, 3];
  
print("Key(3) found at: " + str(binary_search_rotated(v2, 3)))
print("Key(6) found at: " + str(binary_search_rotated(v2, 6)))   