import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2 * np.pi, 1000)
x_t = np.exp(1j * 2 * t) + np.exp(1j * 3 * t)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, np.real(x_t), label='Real Part')
plt.title('Real Part of x(t) = e^{j2t} + e^{j3t}')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, np.imag(x_t), label='Imaginary Part')
plt.title('Imaginary Part of x(t) = e^{j2t} + e^{j3t}')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
