#!/usr/bin/env python

import cProfile, pstats, StringIO

import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt

def toneWithNoise(Fs=2048.0, nFFT=2048):
    length = 1.0  # seconds
    freq = 100.0  # Hz

    t = np.arange(0, length, 1.0/Fs)
    sig = np.cos(2 * np.pi * freq * t)

    x = np.arange(-Fs/2.0, Fs/2.0, Fs/nFFT)

    #noise = np.random.normal(0, 1, nFFT)
    #data = 10 * np.log10(np.power(np.abs(np.fft.fftshift(np.fft.fft(sig + noise))), 2) / (nFFT * Fs))

    while True:
        noise = np.random.normal(0, 1, nFFT)
        yield x, 10 * np.log10(np.power(np.abs(np.fft.fftshift(np.fft.fft(sig + noise))), 2) / (nFFT * Fs))

        #yield x, data

def run(niter=1000, doblit=True):
    fig, ax = plt.subplots(1, 1)
    #ax.set_aspect('equal')
    #fig.patch.set_facecolor('black')
    #ax.set_xlim(-512, 512)
    ax.set_ylim(-40, 10)
    ax.patch.set_facecolor('black')
    ax.hold(True)

    rw = toneWithNoise()
    x, sig = rw.next()

    ax.set_xlim(np.min(x), np.max(x))

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    points = ax.plot(x, sig, color="green")[0]
    tic = time.time()

    for ii in xrange(niter):
        # update the data
        x, sig = rw.next()
        points.set_data(x, sig)

        if doblit:
            # restore background
            fig.canvas.restore_region(background)

            # redraw just the points
            ax.draw_artist(points)

            # fill in the axes rectangle
            fig.canvas.blit(ax.bbox)
        else:
            # redraw everything
            fig.canvas.draw()

    plt.close(fig)
    print "Duration: " + str(time.time() - tic)
    print "Blit = %s, average FPS: %.2f" % (
        str(doblit), niter / (time.time() - tic))

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

#    run(doblit=False)
    run(doblit=True)

    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()
