# Foundational model references: Wendling et al. 2002 (neural mass) and Jirsa et al. 2014 (Epileptor) [FOUNDATIONAL / OLDER]

## Citation & Link
1. Wendling F, Bartolomei F, Bellanger JJ, Chauvel P. "Epileptic fast activity can be explained by a model of impaired GABAergic dendritic inhibition." *European Journal of Neuroscience* 15(9):1499-1508 (2002). DOI: https://doi.org/10.1046/j.1460-9568.2002.01985.x — [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json)
2. Jirsa VK, Stacey WC, Quilichini PP, Ivanov AI, Bernard C. "On the nature of seizure dynamics." *Brain* 137(Pt 8):2210-2230 (2014). DOI: https://doi.org/10.1093/brain/awu133 ; open access PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/

## Venue type
Peer-reviewed journals (Eur J Neurosci; Brain). Foundational modelling papers, not forecasting studies.

## Problem
- Wendling 2002: explain the low-voltage fast (gamma) activity at focal seizure onset with a neural mass model. — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json)
- Jirsa 2014: give a minimal dynamical taxonomy of seizure onset and offset (bifurcations) and a generic model, the Epileptor. — [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)

## Dataset
- Wendling 2002: model simulations compared qualitatively with human intracerebral (SEEG) recordings. — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json)
- Jirsa 2014: in vitro mouse hippocampi, with the model's bifurcation signatures checked across species and brain regions. — [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)

## Approach
- Wendling 2002: extends Jansen-Rit by adding a **fast somatic (GABA_A,fast) inhibitory loop** alongside slow dendritic inhibition. Parameters: excitatory gain A, slow dendritic inhibitory gain B, and fast somatic inhibitory gain G. — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json) (parameter naming from memory of the model's standard formulation)
- Jirsa 2014: **Epileptor**. "Only five state variables" connected by integral-differential equations describe onset, time course and offset. A slow permittivity variable drives the system across a separatrix; onset and offset are bifurcations. — [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)

## Evaluation protocol
Qualitative and structural matching of simulated to recorded signals (Wendling). Bifurcation classification of recorded seizures (Jirsa). No forecasting.

## Key results (numbers)
- Wendling 2002: the model generates "strikingly realistic" activity. The transition from interictal to fast ictal activity is explained by **impaired dendritic (slow) inhibition**. — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json)
- Jirsa 2014: seizure onset occurs when normal trajectories collide with the separatrix. Onset and offset are bifurcations, confirmed across species and regions. Five state variables suffice. — [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)

## Limitations
These papers are models, not predictors. Wendling-type models have many parameters with limited identifiability from a single channel. The Epileptor's slow variable is phenomenological and not directly an E/I ratio.

## Relevance to our project
- **Which model to fit on TUSZ:** Wendling 2002 is the best-established neural mass model for focal seizures and gives interpretable E/I parameters: A (excitation), and B and G (slow and fast inhibition). The ratio A/B or A/(B+G) is a natural "E/I estimate". Jansen-Rit (as in Karoly 2018) is simpler and better suited to Kalman tracking.
- The Epileptor supports the **slow-variable / bifurcation view**. A pre-ictal drift toward a bifurcation should produce critical slowing (link to Maturana 2020 and Chang 2018). This can be used to justify combining CSD features with neural mass parameters.
- An Epileptor-type slow variable cannot be directly estimated from scalp EEG without strong assumptions. Treat it as theory, not as a feature.
