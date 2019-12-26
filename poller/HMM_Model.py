import collections

class Markov_Model:

    def __init__(self, series, window_size=3):
        self.cardinality = len(set(series))
        self.states = set(series)
        self.series_length = len(series)
        self.transition_probability = dict()
        self.emission_probability = dict()
        self.tag_probability = {}

        counter = collections.Counter(series)
        for tag in self.states:
            self.tag_probability[tag] = counter[tag] / self.series_length

        for i in range(self.cardinality):
            self.transition_probability[i + 1] = dict()
            for j in range(self.cardinality):
                self.transition_probability[i + 1][j + 1] = 0.0

        for i in range(self.series_length - 1):
            current_state = series[i]
            next_state = series[i + 1]
            self.transition_probability[current_state][next_state] += 1

        for i in range(self.cardinality):
            sum = 0.0
            for j in range(self.cardinality):
                sum += self.transition_probability[i + 1][j + 1]
            for j in range(self.cardinality):
                self.transition_probability[i + 1][j + 1] /= sum

        for i in range(self.series_length - window_size):
            current_window = []
            for j in range(window_size):
                current_window.append(series[i + j])
            current_window = repr(current_window)
            if current_window in self.emission_probability:
                if series[i + window_size] in self.emission_probability[current_window]:
                    self.emission_probability[current_window][series[i + window_size]] += 1.0
                else:
                    self.emission_probability[current_window][series[i + window_size]] = 1.0
            else:
                self.emission_probability[current_window] = dict()
                self.emission_probability[current_window][series[i + window_size]] = 1.0

        for key in self.emission_probability:
            sum = 0.0
            for key2 in self.emission_probability[key]:
                sum += key2
            for key2 in self.emission_probability[key]:
                self.emission_probability[key][key2] /= sum
                self.emission_probability[key][key2] /= sum