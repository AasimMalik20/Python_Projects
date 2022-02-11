def find_buy_sell_stock_prices(array):
  if array == None or len(array) < 2:
    return None

  current_buy = array[0]
  global_sell = array[1]
  global_profit = global_sell - current_buy

  current_profit = 0

  for i in range(1, len(array)):
    current_profit = array[i] - current_buy

    if current_profit > global_profit:
      global_profit = current_profit
      global_sell = array[i]

    if current_buy > array[i]:
      current_buy = array[i];

  result = global_sell - global_profit, global_sell                 
   
  return result

array = [1, 2, 3, 4, 3, 2, 1, 2, 5]  
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))

array = [8, 6, 5, 4, 3, 2, 1]
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))