def SortInc3(A, B, C):
    # Ro'yxatga olib tartiblaymiz
    sorted_list = sorted([A, B, C])
    return sorted_list[0], sorted_list[1], sorted_list[2]

# Sinov
A1, B1, C1 = 10, 5, 8
A1, B1, C1 = SortInc3(A1, B1, C1)
print(f"Tartiblangan: {A1}, {B1}, {C1}")