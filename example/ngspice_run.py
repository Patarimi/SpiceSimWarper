from pywes.wrapper.ngspice import NGSpice
from asyncio import run
import matplotlib.pyplot as plt

run(NGSpice.run(f"./test/schem_test.net", f"./test/"))
out = NGSpice.results

print(out.keys())

for k in ["v(in)", "v(out)"]:
    plt.plot(out["time"], out[k], label=k)
plt.legend()
plt.show()
