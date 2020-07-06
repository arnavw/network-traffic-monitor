import pyshark
import matplotlib.pyplot as plt

timeout = 5
try:
    while True:
        capture = pyshark.LiveCapture(interface="en0")
        capture.sniff(timeout=timeout)
        plt.clf()

        if len(capture) / timeout > 150:
            # plt.ylabel("Packets/" + timeout + " Second")
            plt.bar("en0", len(capture) / timeout, color="red")
            plt.ylim(0, 200)
            plt.pause(0.05)

        elif (len(capture) / timeout > 75) & (len(capture) / timeout < 150):
            # plt.ylabel("Packets/" + timeout + " Second")
            plt.bar("en0", len(capture) / timeout, color="yellow")
            plt.ylim(0, 200)
            plt.pause(0.05)

        elif len(capture) / timeout < 75:
            # plt.ylabel("Packets/" + timeout + " Second")
            plt.bar("en0", len(capture) / timeout, color="green")
            plt.ylim(0, 200)
            plt.pause(0.05)

except KeyboardInterrupt:
    pass
