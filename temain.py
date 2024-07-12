import numpy as np

# Measurement and Valve Global Variables
XMEAS = [0]*41
XMV = [0]*12

# Disturbance vector Global Variables
IDV = [0]*20

# Controller Global Variables
SETPT = 0.0
GAIN = 0.0
TAUI = 0.0
ERROLD = 0.0
DELTAT = 0.0

# Initialize Process (this function will have to be created with the correct logic)

def TEINIT(nn):
    # Initialization
    xmeas = np.zeros(41)
    xmv = np.zeros(12)
    idv = np.zeros(20, dtype=int)
    g = 4651207995.0
    uclr = np.zeros(8)
    ucvv = np.zeros(8)
    vcv = np.zeros(12)
    ivst = np.zeros(12, dtype=int)
    hspan = np.zeros(12)
    szero = np.zeros(12)
    vrng = np.zeros(12)
    vta = np.zeros(12)
    hwr = 7060.0
    hws = 11138.0
    sfr = np.zeros(8)
    xst = np.zeros((8, 13))
    tst = np.zeros(13)
    cpflmx = 280275.0
    cpprmx = 1.3

    # Array assignments
    xmw = np.array([2.0, 25.4, 28.0, 32.0, 46.0, 48.0, 62.0, 76.0])
    avp = np.array([0.0, 0.0, 0.0, 15.92, 16.35, 16.35, 16.43, 17.21])
    bvp = np.array([0.0, 0.0, 0.0, -1444.0, -2114.0, -2114.0, -2748.0, -3318.0])
    cvp = np.array([0.0, 0.0, 0.0, 259.0, 265.5, 265.5, 232.9, 249.6])
    ad = np.array([1.0, 1.0, 1.0, 23.3, 33.9, 32.8, 49.9, 50.5])
    bd = np.array([0.0, 0.0, 0.0, -0.0700, -0.0957, -0.0995, -0.0191, -0.0541])
    cd = np.array([0.0, 0.0, 0.0, -0.0002, -0.000152, -0.000233, -0.000425, -0.000150])
    ah = np.array([1.0e-6, 1.0e-6, 1.0e-6, 0.960e-6, 0.573e-6, 0.652e-6, 0.515e-6, 0.471e-6])
    bh = np.array([0.0, 0.0, 0.0, 8.70e-9, 2.41e-9, 2.18e-9, 5.65e-10, 8.70e-10])
    ch = np.array([0.0, 0.0, 0.0, 4.81e-11, 1.82e-11, 1.94e-11, 3.82e-12, 2.62e-12])
    av = np.array([1.0e-6, 1.0e-6, 1.0e-6, 86.7e-6, 160.0e-6, 160.0e-6, 225.0e-6, 209.0e-6])
    ag = np.array([3.411e-6, 0.3799e-6, 0.2491e-6, 0.3567e-6, 0.3463e-6, 0.3930e-6, 0.170e-6, 0.150e-6])
    bg = np.array([7.18e-10, 1.08e-9, 1.36e-11, 8.51e-10, 8.96e-10, 1.02e-9, 0.0, 0.0])
    cg = np.array([6.0e-13, -3.98e-13, -3.93e-14, -3.12e-13, -3.27e-13, -3.12e-13, 0.0, 0.0])

    # State initialization
    yy = np.zeros(nn)
    yp = np.zeros(nn)
    time = 0.0

    yy_values = [
        10.40491389, 4.363996017, 7.570059737, 0.4230042431, 24.15513437, 2.942597645, 154.3770655,
        159.1865960, 2.808522723, 63.75581199, 26.74026066, 46.38532432, 0.2464521543, 15.20484404,
        1.852266172, 52.44639459, 41.20394008, 0.5699317760, 0.4306056376, 0.0079906200783,
        0.9056036089, 0.016054258216, 0.7509759687, 0.088582855955, 48.27726193, 39.38459028,
        0.3755297257, 107.7562698, 29.77250546, 88.32481135, 23.03929507, 62.85848794, 5.546318688,
        11.92244772, 5.555448243, 0.9218489762, 94.59927549, 77.29698353, 63.05263039, 53.97970677,
        24.64355755, 61.30192144, 22.21000000, 40.06374673, 38.10034370, 46.53415582, 47.44573456,
        41.10581288, 18.11349055, 50.00000000
    ]

    for i in range(nn):
        yy[i] = yy_values[i]

    for i in range(12):
        xmv[i] = yy[i + 38]
        vcv[i] = xmv[i]
        ivst[i] = 0

    vrng[0] = 400.00
    vrng[1] = 400.00
    vrng[2] = 100.00
    vrng[3] = 1500.00
    vrng[6] = 1500.00
    vrng[7] = 1000.00
    vrng[8] = 0.03
    vrng[9] = 1000.00
    vrng[10] = 1200.00
    vtr = 1300.0
    vts = 3500.0
    vtc = 156.5
    vtv = 5000.0

    htr = np.array([0.06899381054, 0.05])
    sfr = np.array([0.99500, 0.99100, 0.99000, 0.91600, 0.93600, 0.93800, 0.058000, 0.030100])

    xst = np.array([
        [0.0, 0.0, 0.0, 0.4850, 0.0, 0.0, 0.0, 0.0],
        [0.0001, 0.0, 0.0, 0.0050, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.5100, 0.0, 0.0, 0.0, 0.0],
        [0.9999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.9999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ])

    tst = np.array([
        0.0, 0.0, 0.0, 32.0, 52.0, 69.0, 40.0, 45.0, 28.0, 25.0, 43.0, 36.0, 50.0
    ])

    return {
        'xmeas': xmeas,
        'xmv': xmv,
        'idv': idv,
        'g': g,
        'uclr': uclr,
        'ucvv': ucvv,
        'vcv': vcv,
        'ivst': ivst,
        'hspan': hspan,
        'szero': szero,
        'vrng': vrng,
        'vta': vta,
        'hwr': hwr,
        'hws': hws,
        'sfr': sfr,
        'xst': xst,
        'tst': tst,
        'cpflmx': cpflmx,
        'cpprmx': cpprmx,
        'xmw': xmw,
        'avp': avp,
        'bvp': bvp,
        'cvp': cvp,
        'ad': ad,
        'bd': bd,
        'cd': cd,
        'ah': ah,
        'bh': bh,
        'ch': ch,
        'av': av,
        'ag': ag,
        'bg': bg,
        'cg': cg,
        'yy': yy,
        'yp': yp,
        'time': time
    }

# Constants
AVP = np.zeros(8)
BVP = np.zeros(8)
CVP = np.zeros(8)
AH = np.zeros(8)
BH = np.zeros(8)
CH = np.zeros(8)
AG = np.zeros(8)
BG = np.zeros(8)
CG = np.zeros(8)
AV = np.zeros(8)
AD = np.zeros(8)
BD = np.zeros(8)
CD = np.zeros(8)
XMW = np.zeros(8)

def TESUB1(Z, T, ITY):
    H = 0.0
    if ITY == 0:
        for I in range(8):
            HI = T * (AH[I] + BH[I] * T / 2.0 + CH[I] * T**2 / 3.0)
            HI = 1.8 * HI
            H += Z[I] * XMW[I] * HI
    else:
        for I in range(8):
            HI = T * (AG[I] + BG[I] * T / 2.0 + CG[I] * T**2 / 3.0)
            HI = 1.8 * HI
            HI += AV[I]
            H += Z[I] * XMW[I] * HI
    if ITY == 2:
        R = 3.57696e-6
        H -= R * (T + 273.15)
    return H

def TESUB2(Z, T, H, ITY):
    TIN = T
    for J in range(100):
        HTEST = TESUB1(Z, T, ITY)
        ERR = HTEST - H
        DH = TESUB3(Z, T, ITY)
        DT = -ERR / DH
        T += DT
        if abs(DT) < 1e-12:
            break
    T = TIN
    return T

def TESUB3(Z, T, ITY):
    DH = 0.0
    if ITY == 0:
        for I in range(8):
            DHI = AH[I] + BH[I] * T + CH[I] * T**2
            DHI = 1.8 * DHI
            DH += Z[I] * XMW[I] * DHI
    else:
        for I in range(8):
            DHI = AG[I] + BG[I] * T + CG[I] * T**2
            DHI = 1.8 * DHI
            DH += Z[I] * XMW[I] * DHI
    if ITY == 2:
        R = 3.57696e-6
        DH -= R
    return DH

def TESUB4(X, T):
    V = 0.0
    for I in range(8):
        V += X[I] * XMW[I] / (AD[I] + (BD[I] + CD[I] * T) * T)
    R = 1.0 / V
    return R

def TESUB5(S, SP, ADIST, BDIST, CDIST, DDIST, TLAST, TNEXT, HSPAN, HZERO, SSPAN, SZERO, SPSPAN, IDVFLAG):
    I = -1
    H = HSPAN * TESUB7(I) + HZERO
    S1 = SSPAN * TESUB7(I) * IDVFLAG + SZERO
    S1P = SPSPAN * TESUB7(I) * IDVFLAG
    ADIST = S
    BDIST = SP
    CDIST = (3.0 * (S1 - S) - H * (S1P + 2.0 * SP)) / H**2
    DDIST = (2.0 * (S - S1) + H * (S1P + SP)) / H**3
    TNEXT = TLAST + H
    return ADIST, BDIST, CDIST, DDIST, TNEXT

def TESUB6(STD):
    X = 0.0
    for I in range(12):
        X += TESUB7(I)
    X = (X - 6.0) * STD
    return X

def TESUB7(I):
    global G
    G = (G * 9228907.0) % 4294967296.0
    if I >= 0:
        return G / 4294967296.0
    else:
        return 2.0 * G / 4294967296.0 - 1.0

def TESUB8(I, T):
    H = T - TLAST[I]
    return ADIST[I] + H * (BDIST[I] + H * (CDIST[I] + H * DDIST[I]))

# Example Disturbance (this function will have to be created with the correct logic)
def TEFUNC(NN, TIME, YY, YP):
    pass

def CONTRL():
    global SETPT, GAIN, TAUI, ERROLD, DELTAT, XMEAS, XMV
    
    ERR = SETPT - XMEAS[14] # Indices are offset by one in Python (starting at 0)
    
    DXMV = GAIN * ((ERR - ERROLD) + ERR * DELTAT * 60.0 / TAUI)
    
    XMV[7] -= DXMV # Indices are offset by one in Python (starting at 0)
    
    ERROLD = ERR

def OUTPUT():
    print(f'Reac Temp = {XMEAS[8]:6.2f}  Stripper Lev = {XMEAS[14]:6.2f}  Stripper Underflow = {XMV[7]:6.2f}')

def INTGTR(NN, TIME, DELTAT, YY, YP):
    TEFUNC(NN, TIME, YY, YP)
    
    TIME += DELTAT
    
    for i in range(NN):
        YY[i] += YP[i] * DELTAT
    
    return TIME

# Driver code to simulate the process
def simulate_process():
    global SETPT, GAIN, TAUI, ERROLD, DELTAT, XMEAS, XMV, IDV
    
    NN = 50
    NPTS = 1000
    DELTAT = 1.0 / 3600.0
    TIME = 0.0
    YY = [0.0]*NN
    YP = [0.0]*NN
    
    initial_values = TEINIT(NN)
    XMEAS = initial_values['xmeas']
    XMV = initial_values['xmv']
    IDV = initial_values['idv']
    
    SETPT = XMEAS[14] + 15.0
    GAIN = 2.0
    TAUI = 5.0
    ERROLD = 0.0
    XMV[9] = 38.0
    
    for i in range(20):
        IDV[i] = 0
    
    for i in range(NPTS):
        CONTRL()
        OUTPUT()
        TIME = INTGTR(NN, TIME, DELTAT, YY, YP)
        
simulate_process()