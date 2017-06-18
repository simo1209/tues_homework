def product_1_to_num(num):
    beggining=1
    for multipier in range(num):
        beggining*=multipier+1
    return beggining

pass

print(product_1_to_num(4))
