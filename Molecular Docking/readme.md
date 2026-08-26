# Molecular Docking Tutorials



# # Molecular docking of PDB ID 3DTC with AutoDock Vina (Python API)
# 
## This notebook:
### - Installs required packages
### - Downloads the 3DTC structure from RCSB
### - Splits receptor (protein) and ligand (co-crystallized small molecule)
### - Prepares PDBQT files (receptor & ligand)
### - Defines a docking box around the ligand
### - Runs AutoDock Vina docking and saves poses

## STEP 0 – Install required packages (run once in a fresh environment)
# NOTE:
### - vina: AutoDock Vina Python API
### - biopython: to parse PDB
### - meeko: to generate ligand PDBQT from RDKit molecule
### - rdkit: chemistry toolkit (often installed via conda)
### If you're in a conda environment, it's usually easier to do:
###   conda install -c conda-forge rdkit meeko vina biopython
### Here we show pip commands, but rdkit via pip can be tricky.


## STEP 1 — Imports
import os import requests from Bio.PDB import PDBParser, PDBIO, Select from vina import Vina from rdkit import Chem from meeko import MoleculePreparation, PDBQTMolecule, PDBQTParser
