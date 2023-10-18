def linearsearchproduct(product_list, target_product):
  indices = []
  for i in range(len(product_list)):
      if product_list[i] == target_product:
          indices.append(i)
  return indices

products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linearsearchproduct(products, target)
print(f"Indices of '{target}' in the list: {result}")