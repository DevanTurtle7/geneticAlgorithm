import dna

def test_dna_init():
    genome = "This is my genome"
    test_dna = dna.dna(genome, None)

    assert(test_dna.genome == genome)

def run_all_tests():
    test_dna_init()

run_all_tests()