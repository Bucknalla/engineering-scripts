import math

data = [1,2,-3,4,-5,6,7,8]

def fourier(data):
    N = len(data)
    frequencies = []
    freq = 0
    t = 0

    # for every frequency...
    for freq in range(freq, freq < N, 1):
        re = 0
        im = 0

        # for every point in time...
        for t in range(t, t < N, 1):

            # Spin the signal _backwards_ at each frequency (as radians/s, not Hertz)
            rate = -1 * (2 * math.pi) * freq

            # How far around the circle have we gone at time=t?
            time = t / N
            distance = rate * time

            # datapoint * e^(-i*2*pi*f) is complex, store each part
            re_part = data[t] * math.cos(distance)
            im_part = data[t] * math.sin(distance)

            # add this data point's contribution
            re += re_part
            im += im_part

        # Close to zero? You're zero.
        if (math.fabs(re) < 1e-10):
            re = 0
        if (math.fabs(im) < 1e-10):
            im = 0

        # Average contribution at this frequency
        re = re / N
        im = im / N

        frequencies = {
            're': re,
            'im': im,
            'freq': freq,
            'amp': math.sqrt(re*re + im*im),
            'phase': math.atan2(im, re) * 180 / math.pi     # in degrees
        }

    print frequencies
    return frequencies

fourier(data)
