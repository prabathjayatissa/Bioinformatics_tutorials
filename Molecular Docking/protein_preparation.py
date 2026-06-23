# Install:
# pip install rdkit

from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem

# Silence RDKit warnings/errors to avoid noisy output during batch runs
RDLogger.DisableLog('rdApp.*')


def prepare_protein(mol):
    """
    Basic protein preparation using RDKit.

    Steps:
    - Validate molecule
    - Remove water molecules (simple heuristic)
    - Add hydrogens
    - Sanitize structure
    """

    if mol is None:
        print("Input molecule is None.")
        return None

    # Copy molecule
    mol_cleaned = Chem.Mol(mol)

    # -----------------------------
    # 1. Remove water molecules
    # -----------------------------
    # NOTE:
    # Real protein preparation should use PDB residue info.
    # This is only a simplified heuristic.

    water = Chem.MolFromSmiles("O")

    if water is not None:
        try:
            mol_cleaned = AllChem.DeleteSubstructs(mol_cleaned, water)
            Chem.SanitizeMol(mol_cleaned)
        except Exception as e:
            print(f"Warning during water removal: {e}")

    # -----------------------------
    # 2. Add hydrogens
    # -----------------------------
    try:
        mol_with_h = Chem.AddHs(mol_cleaned)
    except Exception as e:
        print(f"Failed to add hydrogens: {e}")
        return None

    # -----------------------------
    # 3. Optional geometry optimization
    # -----------------------------
    try:
        AllChem.EmbedMolecule(mol_with_h)
        AllChem.UFFOptimizeMolecule(mol_with_h)
    except Exception as e:
        print(f"Geometry optimization warning: {e}")

    # -----------------------------
    # 4. Final sanitization
    # -----------------------------
    try:
        Chem.SanitizeMol(mol_with_h)
    except Exception as e:
        print(f"Sanitization failed: {e}")
        return None

    print("Protein preparation complete.")
    return mol_with_h


if __name__ == "__main__":

    print("--- Protein Preparation Script Initialized ---")

    # Example placeholder molecule
    initial_smiles = "CC(C)NC(=O)NCC"

    input_mol = Chem.MolFromSmiles(initial_smiles)

    if input_mol is not None:

        print("\n[SUCCESS] Input molecule loaded.")

        prepped_protein = prepare_protein(input_mol)

        if prepped_protein is not None:

            print("\n=========================================")
            print("✅ Protein Preparation Complete!")

            # Save output
            try:
                writer = Chem.SDWriter("prepped_protein_output.sdf")
                writer.write(prepped_protein)
                writer.close()

                print(
                    "Structure successfully saved to "
                    "prepped_protein_output.sdf"
                )

            except Exception as e:
                print(f"Could not save SDF file: {e}")

        else:
            print("\n❌ Protein preparation failed.")

    else:
        print("\n🚨 Failed to create molecule from SMILES.")