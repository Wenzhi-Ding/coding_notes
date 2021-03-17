import numpy as np
import scipy.optimize as solver
import matplotlib.pyplot as plt

# 样例数据
ret = np.array([65, 80, 35])
sd = np.array([12.247, 13.784, 10.488])
corr = np.array([[1, 0.61, -0.21], [0.61, 1, 0.235], [-0.21, 0.235, 1]])

class Portfolio:
    
    def __init__(self, ret, sd, corr):
        # 后续允许多种输入的初始化，先实现几种矩阵都给好的
        self.ret = ret
        self.sd = sd
        self.corr = corr


    def port_var(self, wgt):
        return np.dot(np.dot(wgt * self.sd, self.corr), wgt * self.sd)


    def port_sd(self, wgt):
        return np.sqrt(self.port_var(wgt))


    def port_ret(self, wgt):
        return np.dot(wgt, self.ret)


    def min_var(self, er=0, short=False, gmv=False):
        # gmv: Global Minimum Variance
        n = len(self.sd)
        x0 = np.array([1 / n] * n)
        bounds = np.array([(-1, 1)] * n) if short else np.array([(0, 1)] * n)
        constraints = [
            {'type': 'eq', 'fun': lambda wgt: sum(wgt) - 1}, 
            ] if gmv else [
            {'type': 'eq', 'fun': lambda wgt: sum(wgt) - 1}, 
            {'type': 'eq', 'fun': lambda wgt: self.port_ret(wgt) - er}
            ]
        outcome = solver.minimize(self.port_sd, x0=x0, constraints=constraints, bounds=bounds)
        return outcome.fun, np.dot(outcome.x, self.ret), outcome.x


    def efficient_frontier(self, short=False, bins=100):
        # 允许卖空的结果看起来很奇怪，要检查一下
        _ret = np.append(self.ret, self.ret * -1) if short else self.ret
        lo = min(_ret)
        hi = max(_ret)
        step = (hi - lo) / bins
        x = np.arange(lo, hi, step)
        outcomes = [self.min_var(i, short=short)[0] for i in x]  # 应该可以转numpy
        return x, outcomes


    def efficient_frontier_plot(self, short=False, bins=100, sml=False, rf=0, gmv=False):
        rets, sds = self.efficient_frontier(short=short, bins=bins)
        x_scale = max(sds) - min(sds)
        y_scale = max(rets) - min(rets)
        plt.plot(sds, rets)
        plt.xlabel('Std. Dev.')
        plt.ylabel('Expected Returns')
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['left'].set_position(('data', 0))

        if sml:
            sr, ret, sd = self.sharpe_ratio(rf, rets, sds)
            x = np.arange(0, max(sds), max(sds) / bins)
            y = x * sr + rf
            plt.plot(x, y, zorder=5)
            plt.scatter([sd], [ret], c='brown', zorder=6)
            plt.text(sd + x_scale / 20, ret - y_scale / 20, f"Var={sd:.2f}\nE(R)={ret:.2f}", fontsize=8, zorder=6)

        if gmv:
            x, y, _ = self.min_var(gmv=True)
            plt.scatter([x], [y], c='navy', zorder=10)
            plt.text(x + x_scale / 20, y - y_scale / 20, f'GMV={x:.2f}\nE(R)={y:.2f}', fontsize=8)

        plt.show()
    

    def sharpe_ratio(self, rf, rets, sds):
        sr, res_ret, res_sd = -np.inf, np.nan, np.nan
        # 用最后两点的斜率倒推最大无风险利率
        max_rf = rets[-1] - (rets[-1] - rets[-2]) / (sds[-1] - sds[-2]) * sds[-1]
        if rf > max_rf:
            raise ValueError("Cannot estimate Sharpe ratio due to high risk-free rates.")

        for ret, sd in zip(rets, sds):
            sl = (ret - rf) / sd
            if sl > sr:
                sr, res_ret, res_sd = sl, ret, sd
        return sr, res_ret, res_sd
            
    

p = Portfolio(ret=ret, sd=sd, corr=corr)
# print(p.min_var(gmv=True))
p.efficient_frontier_plot(short=False, sml=True, rf=20, gmv=True)