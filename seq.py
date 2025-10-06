class Seq:
    """Класс для работы с биологическими последовательностями."""

    protein_alphabet = set("ACDEFGHIKLMNPQRSTVWY")
    nuc_alphabet = set("ACGT")

    def init(self, sequence: str, inf: str):
        self.sequence = sequence.strip().replace(" ", "")
        self.inf = inf

    def str(self):
        return self.sequence

    def len(self):
        return len(self.sequence)

    def alph(self):
        seq_upper = self.sequence.upper()
        if all(x in self.protein_alphabet for x in seq_upper):
            return "protein"
        elif all(x in self.nuc_alphabet for x in seq_upper):
            return "nucleotide"
        else:
            return "unknown"