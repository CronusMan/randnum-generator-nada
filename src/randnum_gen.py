from nada_dsl import *


def nada_main():
    party_alice = Party(name="Alice")
    # Define range
    max_num = SecretInteger(Input(name="max_num", party=party_alice))
    min_num = SecretInteger(Input(name="min_num", party=party_alice))

    # Get random number in given range
    random_int = min_num + SecretInteger.random() % (max_num-min_num)

    return [
        Output(random_int, "rand_num", party_alice)
    ]
