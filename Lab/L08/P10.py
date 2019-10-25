"""
Write a function named fire.
The function takes 2 filenames:
one is for covalence bond energies and
another is for the reaction specifying amounts of reactant
and product bonds.
The function reads both files for necessary information,
then calculates activation energy, releasing energy,
and the different energy
and appends the result at the end of the second file
---the reaction-bond file.
"""


def fire(fbond, fcombust):

    # Write your code here!!

    #################################
    # Get bond-energy information
    #################################

    bond_energy = {}

    with open(fbond, 'r') as file:
        for line in file:
            e = [x.rstrip() for x in line.split()]
            bond_energy[e[0]] = int(e[1])
    # print(bond_energy)

    # Check if we get bond energy ok
    # hint: having energy as a number is more convenient later
    # print(bond_energy)

    #################################
    # Get combustion information
    #################################

    with open(fcombust, 'r+') as f:
        f.readline()                    # read out the header
        #################
        # Reactants
        #################

        ###################################################
        # 1. Get reactant part, e.g., ["4 C-H", "2 O=O"]
        ###################################################

        reactant = f.readline()         # read the reactant line (2nd line)
        if reactant[-1] == '\n':
            reactant = reactant[:-1]    # remove nuisance '\n'

        reactant = reactant.split('+')  # separate each pair of number-symbol

        # print(reactant)

        ###################################################
        # 2. Compute E1
        # E.g., E1 = 4 x energy['C-H'] + 2 x energy['O=O']
        ###################################################

        E1 = 0  # Initialize activation energy
        for b in reactant:
            pair = b.strip()            # remove extra space
            num_bonds, bond_symbol = pair.split()
            bond_symbol = bond_symbol.strip()  # clean the whitespace out

            # num_bonds, e.g., 4
            # bond_symbol, e.g., 'C-H'

            # Get bond energy
            energy = bond_energy[bond_symbol]  # bond_energy[bond_symbol]

            # Check if we have everything
            # print('* reactant:', num_bonds, bond_symbol, energy)

            E1 += energy * float(num_bonds)

        # Check if we are doing OK with E1 calculation
        # print('E1 = ', E1)

        #################
        # Products
        # This is similar to Reactants.
        # We can even put these into another function,
        # and re-use it.
        #################

        # Need working code here!!!

        product = f.readline()         # read the product line (2nd line)
        if product[-1] == '\n':
            product = product[:-1]    # remove nuisance '\n'

        product = product.split('+')  # separate each pair of number-symbol

        # print(product)

        E2 = 0

        # Need working code here!!!

        for b in product:
            pair = b.strip()            # remove extra space
            num_bonds, bond_symbol = pair.split()
            bond_symbol = bond_symbol.strip()  # clean the whitespace out

            # num_bonds, e.g., 4
            # bond_symbol, e.g., 'C-H'

            # Get bond energy
            energy = bond_energy[bond_symbol]  # bond_energy[bond_symbol]

            # Check if we have everything
            # print('* product:', num_bonds, bond_symbol, energy)

            E2 += energy * float(num_bonds)

        # Check if we are doing OK with E2 calculation
        # print('E2 = ', E2)

        total_E = E1 - E2
        msg = '\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(
            E1, E2, total_E)

        # print(msg)
        f.write(msg)  # See it first, write later when done


if __name__ == '__main__':
    fire('bond_energy.txt', 'methane1.txt')
