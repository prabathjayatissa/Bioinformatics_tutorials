# %% [markdown]
# # Molecular docking of PDB ID 3DTC with AutoDock Vina (Python API)
# 
# This notebook:
# - Installs required packages
# - Downloads the 3DTC structure from RCSB
# - Splits receptor (protein) and ligand (co-crystallized small molecule)
# - Prepares PDBQT files (receptor & ligand)
# - Defines a docking box around the ligand
# - Runs AutoDock Vina docking and saves poses

# %% 
# STEP 0 – Install required packages (run once in a fresh environment)
# NOTE:
# - vina: AutoDock Vina Python API
# - biopython: to parse PDB
# - meeko: to generate ligand PDBQT from RDKit molecule
# - rdkit: chemistry toolkit (often installed via conda)
# If you're in a conda environment, it's usually easier to do:
#   conda install -c conda-forge rdkit meeko vina biopython
# Here we show pip commands, but rdkit via pip can be tricky.

import sys
import subprocess

def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# Comment out lines you don't need if already installed
# pip_install("vina")
# pip_install("biopython")
# pip_install("meeko")
# pip_install("rdkit-pypi")  # works on some platforms

# %% 
# STEP 1 – Imports

import os
import requests
from Bio.PDB import PDBParser, PDBIO, Select
from vina import Vina
from rdkit import Chem
from meeko import MoleculePreparation

# %% 
# STEP 2 – Download PDB structure 3DTC from RCSB
# We download the PDB file and save it locally as '3dtc.pdb'.

pdb_id = "3DTC"
pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
pdb_file = f"{pdb_id.lower()}.pdb"

if not os.path.exists(pdb_file):
    print(f"Downloading {pdb_id} from RCSB...")
    r = requests.get(pdb_url)
    r.raise_for_status()
    with open(pdb_file, "wb") as f:
        f.write(r.content)
    print(f"Saved to {pdb_file}")
else:
    print(f"{pdb_file} already exists, skipping download.")

# %% 
# STEP 3 – Inspect and split receptor and ligand
# We will:
# - Parse the PDB with Biopython
# - Define a selector for protein atoms (receptor)
# - Define a selector for the co-crystallized ligand (HETATM with a chosen residue name)
#
# IMPORTANT:
# - You must check the ligand residue name in 3DTC (e.g., via RCSB or by opening the PDB).
# - For demonstration, we assume the ligand residue name is 'DTQ' (replace with the actual one).
#   Open the PDB file and look for lines starting with "HETATM" to confirm.

ligand_resname = "DTQ"  # <-- CHANGE THIS to the actual ligand residue name in 3DTC

parser = PDBParser(QUIET=True)
structure = parser.get_structure(pdb_id, pdb_file)

class ProteinSelect(Select):
    """Select only standard amino acid residues (receptor)."""
    def accept_residue(self, residue):
        # Keep only residues that are standard amino acids
        # residue.get_resname() returns 3-letter code
        # We filter out water and hetero residues
        hetfield = residue.id[0].strip()
        if hetfield != "":  # HETATM, water, etc.
            return 0
        return 1

class LigandSelect(Select):
    """Select only the ligand with a given residue name."""
    def __init__(self, resname):
        super().__init__()
        self.resname = resname

    def accept_residue(self, residue):
        # Keep only residues whose name matches the ligand residue name
        if residue.get_resname().strip() == self.resname:
            return 1
        return 0

# Write receptor PDB
receptor_pdb = "3dtc_receptor.pdb"
io = PDBIO()
io.set_structure(structure)
io.save(receptor_pdb, ProteinSelect())
print(f"Receptor saved to {receptor_pdb}")

# Write ligand PDB
ligand_pdb = "3dtc_ligand.pdb"
io = PDBIO()
io.set_structure(structure)
io.save(ligand_pdb, LigandSelect(ligand_resname))
print(f"Ligand saved to {ligand_pdb}")

# %% 
# STEP 4 – Prepare ligand PDBQT using RDKit + Meeko
# - We read the ligand PDB with RDKit
# - Use Meeko to generate a PDBQT string
# - Save it as '3dtc_ligand.pdbqt'
#
# NOTE:
# - If RDKit fails to read the PDB, you may need to clean or protonate the ligand separately.
# - Meeko handles atom types and charges for Vina.

ligand_pdbqt = "3dtc_ligand.pdbqt"

# Read ligand with RDKit
ligand_mol = Chem.MolFromPDBFile(ligand_pdb, removeHs=False)
if ligand_mol is None:
    raise ValueError(
        "RDKit could not read the ligand PDB. "
        "Check ligand_resname or clean the PDB file."
    )

# Prepare ligand for Vina using Meeko
preparator = MoleculePreparation()
preparator.prepare(ligand_mol)
ligand_pdbqt_str = preparator.write_pdbqt_string()

with open(ligand_pdbqt, "w") as f:
    f.write(ligand_pdbqt_str)

print(f"Ligand PDBQT saved to {ligand_pdbqt}")

# %% 
# STEP 5 – Prepare receptor PDBQT
# For the receptor, there are several options:
# - Use external tools like MGLTools or pdb4amber + obabel to generate PDBQT
# - Or use Meeko's protein preparation (experimental)
#
# Here we show a simple approach using Meeko's protein preparation.
# For production work, many people still use AutoDockTools scripts.
#
# NOTE:
# - This is a simplified example. Carefully check protonation states and missing atoms for real projects.

from meeko import PDBQTMolecule

receptor_pdbqt = "3dtc_receptor.pdbqt"

# Meeko can convert a PDB file to PDBQT for proteins via PDBQTMolecule
receptor_mol = PDBQTMolecule.from_pdb_file(receptor_pdb)
receptor_pdbqt_str = receptor_mol.to_pdbqt()

with open(receptor_pdbqt, "w") as f:
    f.write(receptor_pdbqt_str)

print(f"Receptor PDBQT saved to {receptor_pdbqt}")

# %% 
# STEP 6 – Define docking box around the original ligand
# We:
# - Parse the ligand coordinates from the PDB
# - Compute the center of mass (simple average of atom coordinates)
# - Define a box size (e.g., 20 x 20 x 20 Å) around that center

from Bio.PDB import NeighborSearch

# Collect ligand atom coordinates
ligand_atoms = []
for model in structure:
    for chain in model:
        for residue in chain:
            if residue.get_resname().strip() == ligand_resname:
                for atom in residue:
                    ligand_atoms.append(atom)

if not ligand_atoms:
    raise ValueError("No ligand atoms found. Check ligand_resname.")

xs = [atom.coord[0] for atom in ligand_atoms]
ys = [atom.coord[1] for atom in ligand_atoms]
zs = [atom.coord[2] for atom in ligand_atoms]

center = [
    sum(xs) / len(xs),
    sum(ys) / len(ys),
    sum(zs) / len(zs),
]

# Define box size (in Å)
box_size = [20.0, 20.0, 20.0]

print("Docking box center (x, y, z):", center)
print("Docking box size (Å):", box_size)

# %% 
# STEP 7 – Run AutoDock Vina docking
# We:
# - Create a Vina object
# - Load receptor and ligand PDBQT files
# - Set the search space (center + box size)
# - Run docking with chosen exhaustiveness and number of poses
# - Save the top poses to an output PDBQT file

vina = Vina(sf_name="vina")  # scoring function: 'vina', 'ad4', or 'vinardo'

# Set receptor and ligand
vina.set_receptor(receptor_pdbqt)
vina.set_ligand_from_file(ligand_pdbqt)

# Define search space
vina.compute_vina_maps(center=center, box_size=box_size)

# Optional: score current pose (original ligand pose)
energy = vina.score()
print(f"Score before minimization: {energy[0]:.3f} kcal/mol")

# Optional: local optimization of current pose
energy_minimized = vina.optimize()
print(f"Score after minimization: {energy_minimized[0]:.3f} kcal/mol")

# Dock the ligand
vina.dock(exhaustiveness=16, n_poses=20)  # increase exhaustiveness for more thorough search

# Save top poses
out_pdbqt = "3dtc_ligand_vina_out.pdbqt"
vina.write_poses(out_pdbqt, n_poses=10, overwrite=True)
print(f"Docking finished. Poses saved to {out_pdbqt}")

# %% 
# STEP 8 – (Optional) Convert best pose to PDB for visualization
# Many visualization tools (PyMOL, ChimeraX, etc.) can read PDBQT directly,
# but sometimes it's convenient to convert the top pose to PDB.
#
# Here we:
# - Read the first pose from the output PDBQT
# - Convert it to PDB using Meeko
# - Save as '3dtc_ligand_vina_best.pdb'

from meeko import PDBQTParser

best_pose_pdb = "3dtc_ligand_vina_best.pdb"

with open(out_pdbqt, "r") as f:
    pdbqt_text = f.read()

parser = PDBQTParser()
poses = parser.parse(pdbqt_text)

# Take the first pose
first_pose = poses[0]
pdb_block = first_pose.to_pdb_block()

with open(best_pose_pdb, "w") as f:
    f.write(pdb_block)

print(f"Best docked pose saved as PDB to {best_pose_pdb}")
print("You can now visualize receptor + best_pose in PyMOL, ChimeraX, etc.")

