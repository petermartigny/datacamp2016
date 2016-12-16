# DataCamp2016 @ Ecole polytechnique
In this challenge, we are given Raman spectra for 1000 chemical solutions with different containers, solutes, molecules (4 different molecules for chemiotherapy usage) and concentrations.
Administering the right molecule at the right concentration is a crucial point for the chemiotherapy to be successful.

This project is about optimizing these two problems: 

### Classification task
Predict the molecule present in the solution

### Regression task
Predict the concentration of the molecules

### Metrics used
Classification: 0/1 loss
Regression: MARE
Combined: 2/3 * clf + 1/3 * reg

#### Scores (combined)
Frome the starting kit: 0.15
Final individual score: 0.053
Score after collaborative session: 0.040
