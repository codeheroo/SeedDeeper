from bip_utils import Bip39SeedGenerator, Bip32Slip10Secp256k1

def generate_private_key(seed, derivation_path):


    seed_bytes = Bip39SeedGenerator(seed).Generate()
    bip32_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)


    derived_key = bip32_ctx.DerivePath(derivation_path)


    private_key = derived_key.PrivateKey().Raw().ToHex()

    return private_key

if __name__ == "__main__":
    text = "Enter deep: "

    derivation_path = f"m/44'/60'/0'/0/{input(text)}"


    try:
        with open('seeds.txt', 'r') as f:
            seeds = f.read().splitlines()
    except FileNotFoundError:
        print("Error: 'seeds.txt' file not found.")
        exit(1)


    with open('privatekeys.txt', 'w') as f_out:

        for seed in seeds:

            if not seed.strip():
                continue
            try:

                private_key = f"0x{generate_private_key(seed.strip(), derivation_path)}"

                f_out.write(f"{private_key}\n")
            except Exception as e:
                print(f"Error processing seed: '{seed}'. Exception: {e}")

    print("Private keys have been generated and saved to 'privatekeys.txt'.")
