#!/usr/bin/env Rscript

# Bioinformatics Analysis in R
# Author: Your Name
# Date: 2024
# Description: Basic R functions for sequence analysis

# Load required libraries (install if needed)
required_packages <- c("Biostrings", "seqinr", "ggplot2", "dplyr", "tidyr")

for (pkg in required_packages) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg, repos = "https://cran.r-project.org")
    library(pkg, character.only = TRUE)
  }
}

# For Bioconductor packages
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

if (!require("Biostrings", quietly = TRUE))
  BiocManager::install("Biostrings")

# 1. FASTA File Processing
process_fasta <- function(file_path) {
  """
  Read and analyze a FASTA file
  """
  # Read FASTA file
  sequences <- readDNAStringSet(file_path)
  
  # Basic statistics
  n_seqs <- length(sequences)
  seq_lengths <- width(sequences)
  
  cat("\n=== FASTA File Statistics ===\n")
  cat("File:", file_path, "\n")
  cat("Number of sequences:", n_seqs, "\n")
  cat("Sequence lengths:\n")
  cat("  Min:", min(seq_lengths), "bp\n")
  cat("  Max:", max(seq_lengths), "bp\n")
  cat("  Mean:", round(mean(seq_lengths), 2), "bp\n")
  cat("  Median:", median(seq_lengths), "bp\n")
  
  return(list(
    sequences = sequences,
    n_seqs = n_seqs,
    lengths = seq_lengths,
    names = names(sequences)
  ))
}

# 2. GC Content Calculation
calculate_gc_content <- function(sequences) {
  """
  Calculate GC content for each sequence
  """
  gc_content <- letterFrequency(sequences, letters = "GC", as.prob = TRUE) * 100
  
  # Create data frame
  gc_df <- data.frame(
    Sequence = names(sequences),
    Length = width(sequences),
    GC_Content = round(as.vector(gc_content), 2)
  )
  
  return(gc_df)
}

# 3. Nucleotide Composition
nucleotide_composition <- function(sequences) {
  """
  Calculate nucleotide frequencies
  """
  # Get alphabet frequencies
  alphabet_freq <- alphabetFrequency(sequences)
  
  # Extract A, C, G, T counts
  comp_df <- data.frame(
    Sequence = names(sequences),
    A = alphabet_freq[, "A"],
    C = alphabet_freq[, "C"],
    G = alphabet_freq[, "G"],
    T = alphabet_freq[, "T"],
    Other = alphabet_freq[, "other"]
  )
  
  # Add percentages
  comp_df$A_perc <- round(comp_df$A / rowSums(comp_df[,2:5]) * 100, 2)
  comp_df$C_perc <- round(comp_df$C / rowSums(comp_df[,2:5]) * 100, 2)
  comp_df$G_perc <- round(comp_df$G / rowSums(comp_df[,2:5]) * 100, 2)
  comp_df$T_perc <- round(comp_df$T / rowSums(comp_df[,2:5]) * 100, 2)
  
  return(comp_df)
}

# 4. Find Sequence Motifs
find_motifs <- function(sequences, pattern = "ATG") {
  """
  Find occurrences of a specific motif
  """
  results <- list()
  
  for (i in 1:length(sequences)) {
    seq_name <- names(sequences)[i]
    seq_str <- as.character(sequences[[i]])
    
    # Find all motif positions
    matches <- gregexpr(pattern, seq_str, perl = TRUE)[[1]]
    
    if (matches[1] != -1) {
      positions <- data.frame(
        Sequence = seq_name,
        Start = matches,
        End = matches + attr(matches, "match.length") - 1,
        Motif = pattern
      )
      results[[seq_name]] <- positions
    }
  }
  
  # Combine results
  if (length(results) > 0) {
    return(do.call(rbind, results))
  } else {
    return(data.frame())
  }
}

# 5. Sequence Translation
translate_sequences <- function(sequences) {
  """
  Translate DNA to protein sequences
  """
  # Translate (starts at first position)
  proteins <- translate(sequences)
  
  return(proteins)
}

# 6. Visualization Functions
plot_length_distribution <- function(lengths, output_file = NULL) {
  """
  Plot sequence length distribution
  """
  p <- ggplot(data.frame(Length = lengths), aes(x = Length)) +
    geom_histogram(bins = 30, fill = "steelblue", color = "black", alpha = 0.7) +
    theme_minimal() +
    labs(title = "Sequence Length Distribution",
         x = "Sequence Length (bp)",
         y = "Frequency") +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"))
  
  if (!is.null(output_file)) {
    ggsave(output_file, p, width = 8, height = 6)
  }
  
  return(p)
}

plot_gc_distribution <- function(gc_df, output_file = NULL) {
  """
  Plot GC content distribution
  """
  p <- ggplot(gc_df, aes(x = GC_Content)) +
    geom_histogram(bins = 30, fill = "darkgreen", color = "black", alpha = 0.7) +
    geom_vline(xintercept = mean(gc_df$GC_Content), 
               color = "red", linetype = "dashed", size = 1) +
    theme_minimal() +
    labs(title = "GC Content Distribution",
         x = "GC Content (%)",
         y = "Frequency",
         caption = paste("Mean GC:", round(mean(gc_df$GC_Content), 2), "%")) +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"))
  
  if (!is.null(output_file)) {
    ggsave(output_file, p, width = 8, height = 6)
  }
  
  return(p)
}

plot_nucleotide_composition <- function(comp_df, output_file = NULL) {
  """
  Plot nucleotide composition
  """
  # Reshape data for plotting
  comp_long <- comp_df %>%
    select(Sequence, A_perc, C_perc, G_perc, T_perc) %>%
    pivot_longer(cols = ends_with("_perc"), 
                 names_to = "Nucleotide", 
                 values_to = "Percentage") %>%
    mutate(Nucleotide = gsub("_perc", "", Nucleotide))
  
  p <- ggplot(comp_long, aes(x = Sequence, y = Percentage, fill = Nucleotide)) +
    geom_bar(stat = "identity", position = "stack") +
    scale_fill_manual(values = c("A" = "#FF6B6B", "C" = "#4ECDC4", 
                                 "G" = "#45B7D1", "T" = "#96CEB4")) +
    theme_minimal() +
    labs(title = "Nucleotide Composition",
         x = "Sequence",
         y = "Percentage (%)") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1),
          plot.title = element_text(hjust = 0.5, face = "bold"))
  
  if (!is.null(output_file)) {
    ggsave(output_file, p, width = 10, height = 6)
  }
  
  return(p)
}

# 7. Export Results
export_results <- function(data, filename, format = "csv") {
  """
  Export results to file
  """
  if (format == "csv") {
    write.csv(data, filename, row.names = FALSE)
  } else if (format == "tsv") {
    write.table(data, filename, sep = "\t", row.names = FALSE, quote = FALSE)
  }
  
  cat("\nResults exported to:", filename, "\n")
}

# 8. Main Analysis Pipeline
main_analysis <- function(fasta_file, output_dir = "results") {
  """
  Main pipeline for sequence analysis
  """
  # Create output directory
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)
    cat("Created output directory:", output_dir, "\n")
  }
  
  cat("\n=== Starting Bioinformatics Analysis ===\n")
  cat("Input file:", fasta_file, "\n")
  
  # Step 1: Read sequences
  cat("\n[1/6] Reading FASTA file...\n")
  seq_data <- process_fasta(fasta_file)
  
  # Step 2: Calculate GC content
  cat("[2/6] Calculating GC content...\n")
  gc_df <- calculate_gc_content(seq_data$sequences)
  export_results(gc_df, file.path(output_dir, "gc_content.csv"))
  
  # Step 3: Nucleotide composition
  cat("[3/6] Calculating nucleotide composition...\n")
  comp_df <- nucleotide_composition(seq_data$sequences)
  export_results(comp_df, file.path(output_dir, "nucleotide_composition.csv"))
  
  # Step 4: Find motifs (example: start codons)
  cat("[4/6] Finding motifs (ATG)...\n")
  motifs <- find_motifs(seq_data$sequences, "ATG")
  if (nrow(motifs) > 0) {
    export_results(motifs, file.path(output_dir, "motif_positions.csv"))
    cat("  Found", nrow(motifs), "motif occurrences\n")
  } else {
    cat("  No motifs found\n")
  }
  
  # Step 5: Translate sequences
  cat("[5/6] Translating sequences...\n")
  proteins <- translate_sequences(seq_data$sequences)
  writeXStringSet(proteins, file.path(output_dir, "translated_proteins.fasta"))
  
  # Step 6: Generate plots
  cat("[6/6] Generating plots...\n")
  plot_length_distribution(seq_data$lengths, 
                           file.path(output_dir, "length_distribution.png"))
  plot_gc_distribution(gc_df, 
                       file.path(output_dir, "gc_distribution.png"))
  plot_nucleotide_composition(comp_df, 
                              file.path(output_dir, "nucleotide_composition.png"))
  
  # Create summary report
  cat("\n=== Generating Summary Report ===\n")
  
  sink(file.path(output_dir, "analysis_summary.txt"))
  cat("BIOINFORMATICS ANALYSIS SUMMARY\n")
  cat("===============================\n\n")
  cat("Date:", date(), "\n")
  cat("Input file:", fasta_file, "\n\n")
  
  cat("SEQUENCE STATISTICS\n")
  cat("------------------\n")
  cat("Total sequences:", seq_data$n_seqs, "\n")
  cat("Total bases:", sum(seq_data$lengths), "bp\n")
  cat("Average length:", round(mean(seq_data$lengths), 2), "bp\n")
  cat("GC content range:", 
      round(min(gc_df$GC_Content), 2), "-", 
      round(max(gc_df$GC_Content), 2), "%\n")
  cat("Average GC content:", round(mean(gc_df$GC_Content), 2), "%\n\n")
  
  cat("NUCLEOTIDE COMPOSITION (average %)\n")
  cat("--------------------------------\n")
  cat("A:", round(mean(comp_df$A_perc), 2), "%\n")
  cat("C:", round(mean(comp_df$C_perc), 2), "%\n")
  cat("G:", round(mean(comp_df$G_perc), 2), "%\n")
  cat("T:", round(mean(comp_df$T_perc), 2), "%\n\n")
  
  cat("MOTIF ANALYSIS\n")
  cat("--------------\n")
  if (nrow(motifs) > 0) {
    cat("ATG motifs found:", nrow(motifs), "\n")
    cat("Sequences with motifs:", length(unique(motifs$Sequence)), "\n")
  } else {
    cat("No ATG motifs found\n")
  }
  
  sink()
  
  cat("\n✅ Analysis Complete!\n")
  cat("Results saved in:", output_dir, "\n")
  cat("Summary report:", file.path(output_dir, "analysis_summary.txt"), "\n")
}

# Run the analysis if script is executed directly
if (interactive()) {
  # For interactive R session
  cat("Please provide a FASTA file path:\n")
  # You can manually set your file path here
  # fasta_file <- "path/to/your/file.fasta"
  # main_analysis(fasta_file)
} else {
  # For command line usage
  args <- commandArgs(trailingOnly = TRUE)
  
  if (length(args) == 0) {
    cat("\nUsage: Rscript bioinformatics_basics.R <fasta_file> [output_dir]\n")
    cat("Example: Rscript bioinformatics_basics.R sequences.fasta results\n")
    quit(status = 1)
  }
  
  fasta_file <- args[1]
  output_dir <- ifelse(length(args) >= 2, args[2], "results")
  
  if (!file.exists(fasta_file)) {
    cat("\nError: File", fasta_file, "does not exist!\n")
    quit(status = 1)
  }
  
  main_analysis(fasta_file, output_dir)
}
