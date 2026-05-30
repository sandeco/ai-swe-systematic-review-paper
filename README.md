# From Prompt to Process: A Systematic Review of AI-Assisted Software Development Frameworks

Systematic literature review (multivocal, Kitchenham + Garousi grey-literature guidelines) of a corpus of 37 studies on AI-assisted software development frameworks that shift the unit of work from the isolated prompt to a structured process. The review proposes a six-dimension taxonomy (specification, context, roles, execution, validation, portability), validates it empirically against the corpus through a hybrid thematic synthesis of six themes, and derives a process-oriented research agenda.

- **Author:** Sanderson Oliveira de Macedo (Federal Institute of Goias)
- **Language:** English
- **Target venue:** arXiv preprint (cs.SE; cross-list cs.AI)
- **Status:** complete draft, validated and ready to compile.

## Structure

- `main.tex`: LaTeX entry point.
- `tex/sections/`: the paper sections (abstract, introduction, review method, related work, taxonomy, results and synthesis, discussion, research agenda, limitations, conclusion).
- `refs.bib`: bibliography. Every entry carries a verified DOI (40 corpus and method references plus one anchor systematic review).
- `figures/`: methodology figure (Kitchenham funnel) at 96 DPI.
- `systematic-review/`: reproducibility package, that is, the review protocol, search descriptors, screening logs, snowballing scripts, the structured extraction matrix, and the thematic synthesis.
- `PAPER.md`: SCIENTEX process memory and source of truth.
- `AUTONOMOUS_RUN.md`: autonomous run audit log (every automatic decision, the citation and critic loops, and the validation gate).
- `critic/`: paper-critic state and review log.

## Reproducibility note

The full-text PDFs of the reviewed studies are not redistributed here for copyright reasons; the corpus is fully identified by DOI in `refs.bib` and in `systematic-review/extracted/extraction-matrix.csv`. The screening logs, extraction records, synthesis, and pipeline scripts are included so the review can be inspected and re-run.

## Companion study

The focused characterization of the support frameworks for development on top of an agent (BMAD, Reversa, GitHub Spec Kit, OpenSpec, Get Shit Done, Spec Kitty) is reported in a companion paper.
