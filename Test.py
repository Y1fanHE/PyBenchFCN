from PyBenchFCN import Tool

for i in range(1, 62):
    Tool.plot(f"f{i}", savepath=f"f{i}_3D.png")
    Tool.plot(f"f{i}", plot_type="contour", savepath=f"f{i}_2D.png")