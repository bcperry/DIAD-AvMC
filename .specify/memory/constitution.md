<!--
  Sync Impact Report
  ===================
  Version change: N/A → 1.0.0 (initial ratification)
  Modified principles: N/A (initial version)
  Added sections:
    - Core Principles (5 principles)
    - Content & Data Constraints
    - Delivery Workflow
    - Governance
  Removed sections: N/A
  Templates requiring updates:
    - .specify/templates/plan-template.md ✅ no conflicts
    - .specify/templates/spec-template.md ✅ no conflicts
    - .specify/templates/tasks-template.md ✅ no conflicts
  Follow-up TODOs: None
-->

# DIAD-AMC Constitution

## Core Principles

### I. Audience-First Design
All content MUST be tailored to the DEVCOM Aviation & Missile Center
(AvMC) workforce: engineers, scientists, analysts, and program
managers at Redstone Arsenal and satellite locations. Scenario
narratives, sample data, and visual examples MUST use defense
R&D/engineering domain language (readiness, sustainment, platforms,
test events) rather than commercial sales/marketing terminology.
Every design choice MUST answer: "Does this resonate with an AvMC
professional's day-to-day work?"

### II. Data Fidelity with Synthetic Safety
All datasets MUST be entirely synthetic — no real program data, PII,
FOUO, CUI, or classified information. Synthetic data MUST nonetheless
be structurally realistic: correct column types, plausible value
ranges, and schema complexity sufficient to teach every Power BI
concept covered in the original DIAD curriculum. Data files MUST
preserve the original CSV schema contract (column count and types)
so that lab instructions require minimal rewiring.

### III. Preserve Pedagogical Structure
The original Microsoft Dashboard in a Day lab sequence (Labs 1–5,
Final Report) MUST remain intact as the instructional backbone.
Modifications MUST be limited to re-theming content (branding,
scenario, data) — not restructuring lesson flow, removing labs, or
adding new Power BI concepts beyond what the base DIAD covers.
Optional demos (Copilot in Power BI, Power BI Service) MUST be
retained as-is unless they contain VanArsdel-specific references
that need swapping.

### IV. Visual & Brand Consistency
All deliverables MUST use a unified DEVCOM AvMC visual identity:
- Color palette derived from Army branding guidelines
- DEVCOM AvMC logo replacing VanArsdel logo
- Background imagery appropriate to the defense engineering context
- Power BI theme JSON MUST be updated to reflect the new palette
  and applied consistently across all .pbix solution files

### V. Traceability of Changes
Every modification to original DIAD content MUST be traceable.
A change log MUST document what was changed, why, and which original
file it maps to. This enables future maintainers to re-baseline
against updated Microsoft DIAD releases. File naming and directory
structure MUST mirror the original DIAD layout.

## Content & Data Constraints

- **Platform scope**: Power BI Desktop and Power BI Service only.
  No custom development, no DAX beyond what DIAD teaches.
- **Data volume**: Synthetic datasets SHOULD approximate the row
  counts of the originals (~4M US rows, ~3M international rows)
  to ensure realistic performance behavior during labs.
- **Scenario domain**: Aviation and missile lifecycle management.
  Suggested entities: Platform (Apache, Black Hawk, Chinook, GMLRS,
  HIMARS, THAAD, Patriot), Installation (Redstone Arsenal, Corpus
  Christi Army Depot, Letterkenny Army Depot, Fort Novosel),
  Metrics (engineering hours, work orders, test events, readiness
  rate).
- **International reframe**: Replace country-based sales data with
  allied nation Foreign Military Sales (FMS) support data or
  depot-level maintenance by location, consistent with AMCOM's
  role as the Army's FMS leader.
- **No CUI/FOUO**: All content MUST be suitable for distribution
  on unclassified networks (NIPRNet). No references to specific
  program costs, actual readiness figures, or controlled data.

## Delivery Workflow

- **Asset creation order**: (1) Synthetic CSV datasets →
  (2) Branding assets (logo, background, theme JSON) →
  (3) Rebuilt .pbix solution files → (4) Updated PowerPoint deck →
  (5) Revised demo/trainer scripts.
- **Validation gate**: Each .pbix solution file MUST open without
  errors and reproduce the equivalent visualizations from the
  original DIAD labs using the new dataset.
- **Review checkpoint**: The updated PowerPoint deck MUST be
  reviewed for any residual VanArsdel or commercial-scenario
  references before delivery.

## Governance

This constitution supersedes ad-hoc decisions about content changes.
All pull requests and reviews MUST verify compliance with the five
core principles. Amendments to this constitution require:
1. A written proposal documenting the change and rationale.
2. Agreement from the project lead.
3. Version bump per semantic versioning (MAJOR for principle
   removals/redefinitions, MINOR for additions, PATCH for
   clarifications).

**Version**: 1.0.0 | **Ratified**: 2026-04-26 | **Last Amended**: 2026-04-26
