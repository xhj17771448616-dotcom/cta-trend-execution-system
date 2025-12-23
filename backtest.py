import pandas as pd
import numpy as np

# =========================
# 1. 生成示例行情数据
# =========================
np.random.seed(42)

dates = pd.date_range(start="2020-01-01", end="2023-12-31", freq="B")
price = 100 + np.cumsum(np.random.randn(len(dates)))

data = pd.DataFrame({
    "date": dates,
    "close": price
})
data.set_index("date", inplace=True)

# =========================
# 2. 计算交易信号（均线策略）
# =========================
short_window = 20
long_window = 60

data["ma_short"] = data["close"].rolling(short_window).mean()
data["ma_long"] = data["close"].rolling(long_window).mean()

data["signal"] = 0
data.loc[data["ma_short"] > data["ma_long"], "signal"] = 1
data.loc[data["ma_short"] < data["ma_long"], "signal"] = -1

# =========================
# 3. 计算策略收益
# =========================
data["return"] = data["close"].pct_change()
data["strategy_return"] = data["signal"].shift(1) * data["return"]

# =========================
# 4. 加入简单滑点与手续费
# =========================
slippage = 0.0005
commission = 0.0002

data["cost"] = np.abs(data["signal"].diff()) * (slippage + commission)
data["net_return"] = data["strategy_return"] - data["cost"]

# =========================
# 5. 绩效统计
# =========================
cum_return = (1 + data["net_return"]).cumprod()
annual_return = cum_return.iloc[-1] ** (252 / len(cum_return)) - 1
max_drawdown = (cum_return / cum_return.cummax() - 1).min()

print("Annual Return:", round(annual_return, 2))
print("Max Drawdown:", round(max_drawdown, 2))
