<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script"></script>

<h1><p align="center"># Fitness Landscape of Functions #</p></h1>

## Ackley Function

$$f(\textbf{x}) = f(x_1, ..., x_n)= -a\cdot exp(-b\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-exp(\frac{1}{d}\sum_{i=1}^{n}cos(cx_i))+ a + exp(1)$$
$$a=20,\ b=0.2,\ c=2\pi$$
$$x_i\in[-32,32]$$

<p float="left" align="center"><img src="./image/f1_3D.svg" width=400><img src="./image/f1_2D.svg" width=400></p>



## Ackley N.2 Function

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}}$$
$$x,y\in[-32,32]$$

<p float="left" align="center"><img src="./image/f2_3D.svg" width=400><img src="./image/f2_2D.svg" width=400></p>



## Ackley N.3 Function

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}} + 5e^{cos(3x) + sin(3y)}$$
$$x,y\in[-32,32]$$

<p float="left" align="center"><img src="./image/f3_3D.svg" width=400><img src="./image/f3_2D.svg" width=400></p>



## Adjiman Function

$$f(x, y)=cos(x)sin(y) - \frac{x}{y^2+1}$$
$$x\in[-1,2],\ y\in[-1,1]$$

<p float="left" align="center"><img src="./image/f4_3D.svg" width=400><img src="./image/f4_2D.svg" width=400></p>



## Alpine N.1 Function

$$f(\mathbf x)=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i sin(x_i) + 0.1x_i|$$
$$x_i\in[0,10]$$

<p float="left" align="center"><img src="./image/f5_3D.svg" width=400><img src="./image/f5_2D.svg" width=400></p>



## Alpine N.2 Function

$$f(\mathbf x)=f(x_1, ..., x_n) = \prod_{i=1}^{n}\sqrt{x_i}sin(x_i)$$
$$x_i\in[0,10]$$

<p float="left" align="center"><img src="./image/f6_3D.svg" width=400><img src="./image/f6_2D.svg" width=400></p>



## Bartelsconn Function

$$f(x,y)=|x^2 + y^2 + xy| + |sin(x)| + |cos(y)|$$
$$x,y\in[-500,500]$$

<p float="left" align="center"><img src="./image/f7_3D.svg" width=400><img src="./image/f7_2D.svg" width=400></p>



## Beale Function

$$f(x, y) = (1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$$
$$x,y\in[-4.5,4.5]$$

<p float="left" align="center"><img src="./image/f8_3D.svg" width=400><img src="./image/f8_2D.svg" width=400></p>



## Bird Function

$$f(x, y) = sin(x)e^{(1-cos(y))^2}+cos(y)e^{(1-sin(x))^2}+(x-y)^2$$
$$x_i\in[-2\pi,2\pi]$$

<p float="left" align="center"><img src="./image/f9_3D.svg" width=400><img src="./image/f9_2D.svg" width=400></p>



## Bohachevsky N.1 Function

$$f(x, y) = x^2 + 2y^2 -0.3cos(3\pi x)-0.4cos(4\pi y)+0.7$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f10_3D.svg" width=400><img src="./image/f10_2D.svg" width=400></p>



## Bohachevsky N.2 Function

$$f(x, y)=x^2 + 2y^2 -0.3cos(3\pi x)cos(4\pi y)+0.3$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f11_3D.svg" width=400><img src="./image/f11_2D.svg" width=400></p>



## Booth Function

$$f(x,y)=(x+2y-7)^2+(2x+y-5)^2$$
$$x,y\in[-10,10]$$

<p float="left" align="center"><img src="./image/f12_3D.svg" width=400><img src="./image/f12_2D.svg" width=400></p>



## Brent Function

$$f(x, y) = (x + 10)^2 + (y + 10)^2 + e^{-x^2 - y^2}$$
$$x,y\in[-20,0]$$

<p float="left" align="center"><img src="./image/f13_3D.svg" width=400><img src="./image/f13_2D.svg" width=400></p>



## Brown Function

$$f(\textbf{x}) = \sum_{i=1}^{n-1}(x_i^2)^{(x_{i+1}^{2}+1)}+(x_{i+1}^2)^{(x_{i}^{2}+1)}$$
$$x_i\in[-1,4]$$

<p float="left" align="center"><img src="./image/f14_3D.svg" width=400><img src="./image/f14_2D.svg" width=400></p>



## Bukin N.6 Function

$$f(x,y)=100\sqrt{|y-0.01x^2|}+0.01|x+10|$$
$$x\in[-15,-5],\ y\in[-3,3]$$

<p float="left" align="center"><img src="./image/f15_3D.svg" width=400><img src="./image/f15_2D.svg" width=400></p>



## Cross-in-Tray Function

$$f(x,y)=-0.0001(|sin(x)sin(y)exp(|100-\frac{\sqrt{x^2+y^2}}{\pi}|)|+1)^{0.1}$$
$$x,y\in[-10,10]$$

<p float="left" align="center"><img src="./image/f16_3D.svg" width=400><img src="./image/f16_2D.svg" width=400></p>



## Deckkers-Aarts Function

$$f(x, y) = 10^5x^2 + y^2 -(x^2 + y^2)^2 + 10^{-5}(x^2 + y^2)^4$$
$$x_i\in[-20,20]$$

<p float="left" align="center"><img src="./image/f17_3D.svg" width=400><img src="./image/f17_2D.svg" width=400></p>



## Dropwave Function

$$f(x, y) = - \frac{1 + cos(12\sqrt{x^{2} + y^{2}})}{(0.5(x^{2} + y^{2}) + 2)}$$
$$x,y\in[-5.2,5.2]$$

<p float="left" align="center"><img src="./image/f18_3D.svg" width=400><img src="./image/f18_2D.svg" width=400></p>



## Easom Function

$$f(x,y)=−cos(x_1)cos(x_2) exp(−(x − \pi)^2−(y − \pi)^2)$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f19_3D.svg" width=400><img src="./image/f19_2D.svg" width=400></p>



## Egg Crate Function

$$f(x,y)=x^2 + y^2 + 25(sin^2(x) + sin^2(y))$$
$$x,y\in[-5,5]$$

<p float="left" align="center"><img src="./image/f20_3D.svg" width=400><img src="./image/f20_2D.svg" width=400></p>



## Eggholder Function

$$f(x,y)=-(y+47)sin(\sqrt{|y+\frac{x}{2}+47|})-xsin(\sqrt{|x-(y+47)|})$$
$$x,y\in[-512,512]$$

<p float="left" align="center"><img src="./image/f21_3D.svg" width=400><img src="./image/f21_2D.svg" width=400></p>



## Exponential Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=-exp(-0.5\sum_{i=1}^n{x_i^2})$$
$$x_i\in[-1,1]$$

<p float="left" align="center"><img src="./image/f22_3D.svg" width=400><img src="./image/f22_2D.svg" width=400></p>



## Goldstein-Price Function

$$f(x,y)=[1 + (x + y + 1)^2(19 − 14x+3x^2− 14y + 6xy + 3y^2)][30 + (2x − 3y)^2(18 − 32x + 12x^2 + 4y − 36xy + 27y^2)]$$
$$x,y\in[-2,2]$$

<p float="left" align="center"><img src="./image/f23_3D.svg" width=400><img src="./image/f23_2D.svg" width=400></p>



## Gramacy & Lee Function

$$f(x) = \frac{sin(10\pi x)}{2x} + (x-1)^4$$
$$x\in[-0.5,2.5]$$

<!-- <p float="left" align="center"><img src="./image/f24_3D.svg" width=400><img src="./image/f24_2D.svg" width=400></p> -->



## Griewank Function

$$f(\textbf{x}) = f(x_1, ..., x_n) = 1 + \sum_{i=1}^{n} \frac{x_i^{2}}{4000} - \prod_{i=1}^{n}cos(\frac{x_i}{\sqrt{i}})$$
$$x_i\in[-600,600]$$

<p float="left" align="center"><img src="./image/f25_3D.svg" width=400><img src="./image/f25_2D.svg" width=400></p>



## Happy Cat Function

$$f(\textbf{x})=\left[\left(||\textbf{x}||^2 - n\right)^2\right]^\alpha + \frac{1}{n}\left(\frac{1}{2}||\textbf{x}||^2+\sum_{i=1}^{n}x_i\right)+\frac{1}{2}$$
$$\alpha=0.5$$
$$x_i\in[-2,2]$$

<p float="left" align="center"><img src="./image/f26_3D.svg" width=400><img src="./image/f26_2D.svg" width=400></p>



## Himmelblau Function

$$f(x, y) = (x^{2} + y - 11)^{2} + (x + y^{2} - 7)^{2}$$
$$x,y\in[-6,6]$$

<p float="left" align="center"><img src="./image/f27_3D.svg" width=400><img src="./image/f27_2D.svg" width=400></p>



## Holder-Table Function

$$f(x,y)=-|sin(x)cos(y)exp(|1-\frac{\sqrt{x^2+y^2}}{\pi}|)|$$
$$x,y\in[-10,10]$$

<p float="left" align="center"><img src="./image/f28_3D.svg" width=400><img src="./image/f28_2D.svg" width=400></p>



## Keane Function

$$f(x,y)=-\frac{\sin^2(x-y)\sin^2(x+y)}{\sqrt{x^2+y^2}}$$
$$x,y\in[0,10]$$

<p float="left" align="center"><img src="./image/f29_3D.svg" width=400><img src="./image/f29_2D.svg" width=400></p>



## Leon Function

$$f(x, y) = 100(y − x^{3})^2 + (1 − x)^2$$
$$x,y\in[0,10]$$

<p float="left" align="center"><img src="./image/f30_3D.svg" width=400><img src="./image/f30_2D.svg" width=400></p>



## Levi N.13 Function

$$f(x, y) = sin^2(3\pi x)+(x-1)^2(1+sin^2(3\pi y))+(y-1)^2(1+sin^2(2\pi y))$$
$$x,y\in[-10,10]$$

<p float="left" align="center"><img src="./image/f31_3D.svg" width=400><img src="./image/f31_2D.svg" width=400></p>



## Matyas Function

$$f(x, y)=0.26(x^2+y^2) -0.48xy$$
$$x,y\in[-10,10]$$

<p float="left" align="center"><img src="./image/f32_3D.svg" width=400><img src="./image/f32_2D.svg" width=400></p>



## McCormick Function

$$f(x, y)=sin(x + y) + (x - y) ^2 - 1.5x + 2.5 y + 1$$
$$x\in[-1.5,4],\ y\in[-3,3]$$

<p float="left" align="center"><img src="./image/f33_3D.svg" width=400><img src="./image/f33_2D.svg" width=400></p>



## Periodic Function

$$f(\mathbf{x})=f(x_1 ... x_n)=1 + \sum_{i=1}^{n}{sin^2(x_i)}-0.1e^{(\sum_{i=1}^{n}x_i^2)}$$
$$x_i\in[-10,10]$$

<p float="left" align="center"><img src="./image/f34_3D.svg" width=400><img src="./image/f34_2D.svg" width=400></p>



## Picheny Function

$$f(x,y)=\frac{1}{2.427}[log([1 + (\bar{x} + \bar{y} + 1)^2(19 − 14\bar{x}+3\bar{x}^2− 14\bar{y} + 6\bar{x}\bar{y} + 3\bar{y}^2)][30 + (2\bar{x} − 3\bar{y})^2(18 − 32\bar{x} + 12\bar{x}^2 + 4\bar{y} − 36\bar{x}\bar{y} + 27\bar{y}^2)])-8.693]$$
$$\bar{x}=4x-2,\ \bar{y}=4y-2$$
$$x,y\in[0,1]$$

<p float="left" align="center"><img src="./image/f35_3D.svg" width=400><img src="./image/f35_2D.svg" width=400></p>



## Powell Sum Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|^{i+1}$$
$$x_i\in[-1,1]$$

<p float="left" align="center"><img src="./image/f36_3D.svg" width=400><img src="./image/f36_2D.svg" width=400></p>



## Qing Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}(x^2-i)^2$$
$$x_i\in[-500,500]$$

<p float="left" align="center"><img src="./image/f37_3D.svg" width=400><img src="./image/f37_2D.svg" width=400></p>



## Quartic Function

$$f(\mathbf{x})=f(x_1,...,x_n)=\sum_{i=1}^{n}ix_i^4+\text{random}[0,1)$$
$$x_i\in[-1.28,1.28]$$

<p float="left" align="center"><img src="./image/f38_3D.svg" width=400><img src="./image/f38_2D.svg" width=400></p>



## Rastrigin Function

$$f(x, y)=10n + \sum_{i=1}^{n}(x_i^2 - 10cos(2\pi x_i))$$
$$x_i\in[-5.12,5.12]$$

<p float="left" align="center"><img src="./image/f39_3D.svg" width=400><img src="./image/f39_2D.svg" width=400></p>



## Ridge Function

$$f(\textbf{x}) = x_1 + d\left(\sum_{i=2}^{n}x_i^2\right)^\alpha$$
$$\alpha=0.5,\ d=1$$
$$x_i\in[-5,5]$$

<p float="left" align="center"><img src="./image/f40_3D.svg" width=400><img src="./image/f40_2D.svg" width=400></p>



## Rosenbrock Function

$$f(x, y)=\sum_{i=1}^{n}[b (x_{i+1} - x_i^2)^ 2 + (a - x_i)^2]$$
$$x,y\in[-5,10]$$

<p float="left" align="center"><img src="./image/f41_3D.svg" width=400><img src="./image/f41_2D.svg" width=400></p>



## Salomon Function

$$f(\mathbf x)=f(x_1, ..., x_n)=1-cos(2\pi\sqrt{\sum_{i=1}^{D}x_i^2})+0.1\sqrt{\sum_{i=1}^{D}x_i^2}$$
$$x_i\in[-100,100]$$

<p float="left" align="center"><img src="./image/f42_3D.svg" width=400><img src="./image/f42_2D.svg" width=400></p>



## Schaffer N.1 Function

$$f(x, y)=0.5 + \frac{sin^2(x^2+y^2)^2-0.5}{(1+0.001(x^2+y^2))^2}$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f43_3D.svg" width=400><img src="./image/f43_2D.svg" width=400></p>



## Schaffer N.2 Function

$$f(x, y)=0.5 + \frac{sin^2(x^2-y^2)-0.5}{(1+0.001(x^2+y^2))^2}$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f44_3D.svg" width=400><img src="./image/f44_2D.svg" width=400></p>



## Schaffer N.3 Function

$$f(x, y)=0.5 + \frac{sin^2(cos(|x^2-y^2|))-0.5}{(1+0.001(x^2+y^2))^2}$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f45_3D.svg" width=400><img src="./image/f45_2D.svg" width=400></p>



## Schaffer N.4 Function

$$f(x, y)=0.5 + \frac{cos^2(sin(|x^2-y^2|))-0.5}{(1+0.001(x^2+y^2))^2}$$
$$x,y\in[-100,100]$$

<p float="left" align="center"><img src="./image/f46_3D.svg" width=400><img src="./image/f46_2D.svg" width=400></p>



## Schwefel 2.20 Function

$$f(\mathbf x)=f(x_1, ..., x_n)=\sum_{i=1}^n |x_i|$$
$$x_i\in[-100,100]$$

<p float="left" align="center"><img src="./image/f47_3D.svg" width=400><img src="./image/f47_2D.svg" width=400></p>



## Schwefel 2.21 Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\max_{i=1,...,n}|x_i| $$
$$x_i\in[-100,100]$$

<p float="left" align="center"><img src="./image/f48_3D.svg" width=400><img src="./image/f48_2D.svg" width=400></p>



## Schwefel 2.22 Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|+\prod_{i=1}^{n}|x_i|$$
$$x_i\in[-100,100]$$

<p float="left" align="center"><img src="./image/f49_3D.svg" width=400><img src="./image/f49_2D.svg" width=400></p>



## Schwefel 2.23 Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}x_i^{10}$$
$$x_i\in[-10,10]$$

<p float="left" align="center"><img src="./image/f50_3D.svg" width=400><img src="./image/f50_2D.svg" width=400></p>



## Schwefel Function

$$f(\textbf{x}) = f(x_1, x_2, ..., x_n) = 418.9829d -{\sum_{i=1}^{n} x_i sin(\sqrt{|x_i|})}$$
$$x_i\in[-500,500]$$

<p float="left" align="center"><img src="./image/f51_3D.svg" width=400><img src="./image/f51_2D.svg" width=400></p>



## Sphere Function

$$f(\textbf{x}) = f(x_1, x_2, ..., x_n) = {\sum_{i=1}^{n} x_i^{2}}$$
$$x_i\in[-5.12,5.12]$$

<p float="left" align="center"><img src="./image/f52_3D.svg" width=400><img src="./image/f52_2D.svg" width=400></p>



## Styblinski-Tang Function

$$f(\textbf{x}) = f(x_1, ..., x_n)= \frac{1}{2}\sum_{i=1}^{n} (x_i^4 -16x_i^2+5x_i)$$
$$x_i\in[-5,5]$$

<p float="left" align="center"><img src="./image/f53_3D.svg" width=400><img src="./image/f53_2D.svg" width=400></p>



## Sum Squares Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}{ix_i^2}$$
$$x_i\in[-10,10]$$

<p float="left" align="center"><img src="./image/f54_3D.svg" width=400><img src="./image/f54_2D.svg" width=400></p>



## Three-Hump Camel Function

$$f(x,y)=2x^2-1.05x^4+\frac{x^6}{6}+xy+y^2$$
$$x,y\in[-5,5]$$

<p float="left" align="center"><img src="./image/f55_3D.svg" width=400><img src="./image/f55_2D.svg" width=400></p>



## Wolfe Function

$$f(x, y, z) = \frac{4}{3}(x^2 + y^2 - xy)^{0.75} + z$$
$$x,y,z\in[0,2]$$

<!-- <p float="left" align="center"><img src="./image/f56_3D.svg" width=400><img src="./image/f56_2D.svg" width=400></p> -->



## Xin-She Yang N.1 Function

$$f(\mathbf x)=f(x_1, ...,x_n)=\sum_{i=1}^{n}\epsilon_i|x_i|^i$$
$$x_i\in[-5,5]$$

<p float="left" align="center"><img src="./image/f57_3D.svg" width=400><img src="./image/f57_2D.svg" width=400></p>



## Xin-She Yang N.2 Function

$$f(\mathbf{x})=f(x_1, ..., x_n)=(\sum_{i=1}^{n}|x_i|)exp(-\sum_{i=1}^{n}sin(x_i^2))$$
$$x_i\in[-2\pi,2\pi]$$

<p float="left" align="center"><img src="./image/f58_3D.svg" width=400><img src="./image/f58_2D.svg" width=400></p>



## Xin-She Yang N.3 Function

$$f(\mathbf x)=f(x_1, ..., x_n) =exp(-\sum_{i=1}^{n}(x_i / \beta)^{2m}) - 2exp(-\sum_{i=1}^{n}x_i^2) \prod_{i=1}^{n}cos^ 2(x_i) $$
$$\beta=15,\ m=5$$
$$x_i\in[-2\pi,2\pi]$$

<p float="left" align="center"><img src="./image/f59_3D.svg" width=400><img src="./image/f59_2D.svg" width=400></p>



## Xin-She Yang N.4 Function

$$f(\mathbf x)=f(x_1, ..., x_n)=\left(\sum_{i=1}^{n}sin^2(x_i)-e^{-\sum_{i=1}^{n}x_i^2}\right)e^{-\sum_{i=1}^{n}{sin^2\sqrt{|x_i|}}}$$
$$x_i\in[-10,10]$$

<p float="left" align="center"><img src="./image/f60_3D.svg" width=400><img src="./image/f60_2D.svg" width=400></p>



## Zakharov Function

$$f(\textbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^n x_i^{2}+(\sum_{i=1}^n 0.5ix_i)^2 + (\sum_{i=1}^n 0.5ix_i)^4$$
$$x_i\in[-5,10]$$

<p float="left" align="center"><img src="./image/f61_3D.svg" width=400><img src="./image/f61_2D.svg" width=400></p>