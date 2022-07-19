# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


d = 0.001
accur = 0
while d < 1:
    d *= 10
    accur += 1

def get_pi(accur: int) -> float:
    result = 0
    for k in range(accur):
        result += (16**(-k)) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8* k +6)))
    return result

print(round(get_pi(accur), accur))