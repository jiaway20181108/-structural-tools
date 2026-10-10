# 梁端弯矩计算器
# 功能：输入梁的跨度和荷载，计算弯矩

print("=" * 40)
print("    梁端弯矩计算器 v1.0")
print("=" * 40)
num_beam=int(input("n\请输入要计算几根梁："))
all_M_max=[]

# 获取用户输入
for i in range (num_beam):
    print(f"\---第{i+1}根梁---")
    span = float(input("\n请输入梁的跨度 L (m): "))
    if span<=0:
        print("跨度不能小于0")
        exit()
    load_q = float(input("请输入均布荷载 q (kN/m): "))
    load_P = float(input("请输入集中荷载 P (kN), 没有则输入0: "))
    a = float(input("集中荷载距左支座的距离 a (m), 没有集中荷载则输入0: "))
    b = span - a
    # 计算弯矩
    # 均布荷载产生的跨中弯矩: M = qL²/8
    M_q = load_q * span ** 2 / 8

    # 集中荷载产生的跨中弯矩: M = PL/4
    M_P = load_P * a*b / span

    # 取大值
    M_max = max(M_q + M_P, M_q)

    # 均布荷载和集中荷载的总荷载
    Q=load_q * span+load_P
    #将每一根梁的最大弯矩填入列表
    all_M_max.append(M_max)
    # 输出结果
    print("\n" + "-" * 40)
    print("计算结果：")
    print(f"  均布荷载弯矩: M_q = {M_q:.2f} kN·m")
    print(f"  集中荷载弯矩: M_P = {M_P:.2f} kN·m")
    print(f"  跨中最大弯矩: M_max = {M_max:.2f} kN·m")
    print(f"  总荷载: Q={Q:.2f}kN")
    print("-" * 40)
print("汇总结果：")
for i,m in enumerate(all_M_max):
        print(f"  第{i+1}根梁:M_max={m:.2f}kN·m")