import numpy as np
def DFT_1D(fx):                      #Discrete Fourier Transform
    fx = np.asarray(fx, dtype=complex)
    M = fx.shape[0]
    fu = fx.copy()

    for i in range(M):
        u = i
        sum = 0
        for j in range(M):
            x = j
            tmp = fx[x]*np.exp(-2j*np.pi*x*u*np.divide(1, M, dtype=complex))
            sum += tmp
        fu[u] = sum
  

    return fu


def inverseDFT_1D(fu):
    fu = np.asarray(fu, dtype=complex)
    M = fu.shape[0]
    fx = np.zeros(M, dtype=complex)

    for i in range(M):
        x = i
        sum = 0
        for j in range(M):
            u = j
            tmp = fu[u]*np.exp(2j*np.pi*x*u*np.divide(1, M, dtype=complex))
            sum += tmp
        fx[x] = np.divide(sum, M, dtype=complex)

    return fx


def FFT_1D(fx):            #Fast Fourier Transform, amazing to think Gauss discovered it in the 1800s
    fx = np.asarray(fx, dtype=complex)
    M = fx.shape[0]
    minDivideSize = 4

    if M % 2 != 0:
        raise ValueError("the input size must be 2^n")

    if M <= minDivideSize:
        return DFT_1D(fx)
    else:
        fx_even = FFT_1D(fx[::2])  
        fx_odd = FFT_1D(fx[1::2])  
        W_ux_2k = np.exp(-2j * np.pi * np.arange(M) / M)

        f_u = fx_even + fx_odd * W_ux_2k[:M//2]

        f_u_plus_k = fx_even + fx_odd * W_ux_2k[M//2:]

        fu = np.concatenate([f_u, f_u_plus_k])

    return fu


def inverseFFT_1D(fu):
    fu = np.asarray(fu, dtype=complex)
    fu_conjugate = np.conjugate(fu)

    fx = FFT_1D(fu_conjugate)

    fx = np.conjugate(fx)
    fx = fx / fu.shape[0]

    return fx


def FFT_2D(fx):             #2-Dimensional Transform, For Matrices
    h, w = fx.shape[0], fx.shape[1]

    fu = np.zeros(fx.shape, dtype=complex)

    if len(fx.shape) == 2:
        for i in range(h):
            fu[i, :] = FFT_1D(fx[i, :])

        for i in range(w):
            fu[:, i] = FFT_1D(fu[:, i])
    elif len(fx.shape) == 3:
        for ch in range(3):
            fu[:, :, ch] = FFT_2D(fx[:, :, ch])

    return fu


def inverseDFT_2D(fu):
    h, w = fu.shape[0], fu.shape[1]

    fx = np.zeros(fu.shape, dtype=complex)

    if len(fu.shape) == 2:
        for i in range(h):
            fx[i, :] = inverseDFT_1D(fu[i, :])

        for i in range(w):
            fx[:, i] = inverseDFT_1D(fx[:, i])

    elif len(fu.shape) == 3:
        for ch in range(3):
            fx[:, :, ch] = inverseDFT_2D(fu[:, :, ch])

    fx = np.real(fx)
    return fx


def inverseFFT_2D(fu):
    h, w = fu.shape[0], fu.shape[1]

    fx = np.zeros(fu.shape, dtype=complex)

    if len(fu.shape) == 2:
        for i in range(h):
            fx[i, :] = inverseFFT_1D(fu[i, :])

        for i in range(w):
            fx[:, i] = inverseFFT_1D(fx[:, i])

    elif len(fu.shape) == 3:
        for ch in range(3):
            fx[:, :, ch] = inverseFFT_2D(fu[:, :, ch])

    fx = np.real(fx)
    return fx

def fft_v(x):              # Computing the Fourier transform, now using vectors in place of recursion
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if np.log2(N) % 1 > 0:
        raise ValueError("must be a power of 2")
        
    N_min = min(N, 2)
    
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))
    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        terms = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + terms * X_odd,
                       X_even - terms * X_odd])
    
    return X.ravel()
    #https://numpy.org/doc/stable/reference/index.html
    #http://pi.math.cornell.edu/~web6140/TopTenAlgorithms/FastFourierTransform.html
   