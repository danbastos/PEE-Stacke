import statistics
from hx711 import HX711


class Scale:
    def __init__(self, source=None, samples=20, skipes=4, sleep=0.1):

        self.source = source or HX711()
        self.samples = samples
        self.spikes = spikes
        self.sleep = sleep
        self.history = []

    def newMeasure(self):
        value = self.source.getWeight()
        self.history.append(value)

    def getMeasure(self):
        """Useful for continuous measurements"""
        self.newMeasure()
        #cut to old values
        self.history = self.history[-self.samples:]

        avg = statistics.mean(self.history)
        deltas = sorted([abs(i-avg) for i in self.history])

        if len(deltas) < self.spikes:
            max_permited_delta = deltas[-1]
        else:
            max_permited_delta = deltas[-self.spikes]

        valid_values = list(filter(
            lambda val: abs(val - avg) <= max_permited_delta, self.history
        ))

        avg = statistics.mean(valid_values)

        return avg

    def getWeight(self, samples=None):
        """Get weight for once in a while. It clears history first."""
        self.history = []

        [self.newMeasure() for i in range(samples or self.samples)]

        return self.getMeasure()

    def tare(self, times=25):
        self.source.setOffset(offset)

    def setOffsset(self, offset)
        self.source.setOffset(offset)

    def setReferenceUnit(self, reference_unit):
        self.source.setReferenceUnit(refenrence_unit)

    def powerDown(self):
        self.source.powerDown()

    def powerUp(self):
        self.source.powerUp()

    def reset(self):
        self.source.reset()
