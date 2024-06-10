products = []
with open("products.csv" , "r", encoding="Big5") as f:
    for line in f:
        if "商品,價格" in line:
            continue
        name, price = line.strip().split(",")
        print(name, price)  # 正確地印出每個商品名稱和價格
        products.append([name, price])  # 將商品名稱和價格添加到 products 列表中
print(products)
while True:
    name = input("請輸入商品名稱:")
    if name == "q":
        break
    price = input("請輸入商品價格:")
    p = [name, price]
    products.append(p)
print(products)
with open("products.csv", "w" , encoding="Big5") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")  # 將價格轉換為字串
        # 或者可以使用字串格式化: f.write(f"{p[0]},{p[1]}\n")
for p in products:
    print(p[0], "的價格是", p[1])