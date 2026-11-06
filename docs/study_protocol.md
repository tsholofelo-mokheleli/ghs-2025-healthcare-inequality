
# STUDY PROTOCOL — GHS 2025 HEALTHCARE ACCESS INEQUALITY

**Version:** 2.0  
**Date:** 5 November 2026  
**Status:** Revised analytical protocol — multidimensional healthcare access study

**Working title:**  
**Who Is Being Left Behind? Socioeconomic and Geographic Inequalities in Healthcare Access in South Africa**

**Dataset:** Statistics South Africa General Household Survey (GHS) 2025 — Household and Person datasets.

**Research orientation:** Population health equity, healthcare accessibility, healthcare utilisation, socioeconomic inequality and policy-relevant statistical analysis.

**Methodological approach:** Survey-weighted descriptive and inferential statistics, inequality measurement, multivariable regression, intersectional analysis and population profiling.

**Machine learning:** Not included. The study prioritises interpretable, design-based statistical inference.

---

## 1. Study overview

### 1.1 Background

Equitable healthcare access remains an important public health and policy concern in South Africa. Healthcare access may vary according to household economic resources, demographic circumstances, geographic location, healthcare coverage and the characteristics of available services.

Nationally representative household surveys provide an opportunity to examine how these inequalities are distributed across the population and how different forms of disadvantage overlap.

This study uses the 2025 General Household Survey to investigate socioeconomic, demographic and geographic inequalities in healthcare accessibility, healthcare sector reliance and reported healthcare utilisation.

The study is motivated by the question:

**Who is being left behind by South Africa's healthcare system, and how are socioeconomic and geographic disadvantages associated with unequal access?**

### 1.2 Central proposition

Healthcare access disadvantage is multidimensional.

Geographic accessibility, economic resources, healthcare coverage, healthcare sector reliance and reported utilisation represent related but distinct dimensions.

Socioeconomic and geographic disadvantages may intersect, producing inequalities that are not adequately represented by examining individual characteristics in isolation.

The study will identify the magnitude and distribution of these inequalities and the population groups experiencing overlapping disadvantages.

Because the GHS is cross-sectional, findings will be interpreted as associations rather than causal effects.

### 1.3 Scientific contribution

The study aims to contribute:

1. A nationally representative assessment of socioeconomic, demographic and geographic inequalities in healthcare access.
2. An examination of multiple empirically measurable healthcare access dimensions.
3. Survey-adjusted estimates of associations between household circumstances and healthcare access outcomes.
4. An intersectional assessment of overlapping socioeconomic and geographic disadvantage.
5. Policy-relevant identification of population groups experiencing particularly high access burdens.
6. A reproducible statistical analysis pipeline using Python and appropriate complex-survey methods.

The study will not claim to measure dimensions that cannot be operationalised from the GHS questionnaire.

---

## 2. Research aim and questions

### 2.1 Overall aim

To investigate socioeconomic, demographic and geographic inequalities in healthcare access in South Africa using nationally representative GHS 2025 data, and to identify population groups experiencing intersecting forms of healthcare access disadvantage.

### 2.2 Research questions

**RQ1 — Distribution of healthcare access inequality**

What socioeconomic, demographic and geographic inequalities characterise healthcare accessibility and public/private healthcare sector reliance in South Africa?

**RQ2 — Factors associated with healthcare access disadvantage**

Which socioeconomic, demographic, geographic and household characteristics are associated with healthcare access disadvantage after adjustment for other observed factors?

**RQ3 — Intersecting disadvantage and population profiles**

How do socioeconomic and geographic disadvantages intersect, and which population groups experience the greatest combined burden of healthcare access disadvantage?

### 2.3 Research objectives

**Objective 1:** Describe national and provincial patterns in healthcare accessibility, sector reliance and measurable utilisation.

**Objective 2:** Quantify absolute and relative inequalities across socioeconomic, demographic and geographic groups.

**Objective 3:** Estimate adjusted associations between observed household and individual characteristics and healthcare access outcomes.

**Objective 4:** Investigate whether associations differ across geographic and socioeconomic contexts.

**Objective 5:** Identify population profiles experiencing overlapping healthcare access disadvantages.

**Objective 6:** Translate the empirical findings into appropriately qualified policy recommendations for improving healthcare equity in South Africa.

---

## 3. Conceptual framework

The study adopts a multidimensional healthcare access inequality framework.

### 3.1 Explanatory domains

**Socioeconomic circumstances**
- Household income or expenditure
- Food insecurity
- Employment and education, where applicable
- Household economic resources

**Demographic characteristics**
- Age
- Sex
- Household composition
- Other defensible demographic variables available in the dataset

**Geographic circumstances**
- Province
- Settlement type
- Metropolitan versus non-metropolitan location

**Enabling resources and constraints**
- Medical aid coverage
- Household vehicle ownership
- Transport mode
- Other relevant resources supported by the questionnaire

### 3.2 Healthcare access domains

The analysis distinguishes three potential outcome domains.

**Domain A — Geographic healthcare accessibility**

Measures household-reported travel time to the healthcare facility described in the GHS questionnaire.

Primary candidate variable: `hhw_time`.

Primary binary outcome:

`travel30_hh = 1` for travel time of 30 minutes or more.

`travel30_hh = 0` for travel time below 30 minutes.

Unknown and unspecified responses will be coded as missing.

This outcome measures reported travel-time accessibility, not the full healthcare access construct.

**Domain B — Healthcare sector reliance**

Examines reported reliance on public versus private healthcare facilities.

Candidate variable: `hhw_hltfac`.

A binary public/private outcome will be constructed only after validating the complete response categories and official questionnaire wording.

Healthcare sector reliance will not automatically be interpreted as evidence of adequate or inadequate access.

**Domain C — Reported healthcare utilisation**

Examines person-level healthcare consultation or utilisation indicators, if suitable variables exist.

The specific variables, recall periods, eligible populations and coding will be established through the official questionnaire and data audit.

If the supplied extracts do not support a valid utilisation outcome, this domain will be removed or explicitly limited rather than approximated using an inappropriate variable.

### 3.3 Analytical distinction

Healthcare access outcomes must remain conceptually distinct from potential explanatory variables.

For example:
- Medical aid is an enabling resource or coverage indicator.
- Vehicle ownership is a household transport resource.
- Transport mode describes how a household travels.
- Public/private facility reliance describes healthcare sector use or preference, subject to questionnaire wording.
- Travel time measures one dimension of geographic accessibility.

A composite healthcare disadvantage index will not be created unless its conceptual basis, component compatibility and measurement validity can be justified.

---

## 4. Data source and study population

### 4.1 Data source

Statistics South Africa General Household Survey 2025.

Input files:

`data/raw/ghs-2025-household-v1.csv`

`data/raw/ghs-2025-person-v1.csv`

### 4.2 Verified source dimensions

The initial data audit established:

| Dataset | Records | Variables |
|---|---:|---:|
| Household | 20,095 | 207 |
| Person | 67,748 | 124 |

Both datasets contain 20,095 unique household identifiers.

### 4.3 Household-person linkage

Household linkage identifier: `uqnr`.

Person identifier within household: `personnr`.

Completed checks established:
- No duplicate household identifiers.
- No duplicate `(uqnr, personnr)` combinations.
- No missing linkage identifiers.
- No unmatched household or person records.
- No discrepancies between `hholdsz` and the number of linked persons.

The analysis will retain separate household and person datasets.

Person-level records must not be treated as independent household observations.

### 4.4 Survey design

Available design variables:

- `psu`
- `stratum`
- `house_wgt`
- `person_wgt`

Initial audit results:

| Characteristic | Result |
|---|---:|
| Strata | 248 |
| PSUs | 3,226 |
| Invalid household weights | 0 |
| Invalid person weights | 0 |
| Singleton strata in full extracts | 0 |
| PSUs assigned to multiple strata | 0 |

Approximate weighted totals:
- Households: 20.11 million
- Persons: 64.07 million

These totals and the correct variance-estimation procedure must be checked against the official GHS 2025 methodology.

Household estimands will use household weights.

Person estimands will use person weights.

Confidence intervals and regression inference must account for the verified complex survey design.

---

## 5. Variable operationalisation

### 5.1 Geographic accessibility

Candidate variable: `hhw_time`.

Verified observed categories:

- Less than 15 minutes
- 15–29 minutes
- 30–89 minutes
- 90 minutes and more
- DO NOT KNOW
- Unspecified

Derived variables:

`travel_time_group`: Four substantive travel-time categories.

`travel30_hh`: Binary travel-time burden indicator.

Completed initial outcome validation:

| Category | Households |
|---|---:|
| Below 30 minutes | 16,887 |
| 30 minutes or more | 3,184 |
| Unknown or unspecified | 24 |

Valid travel-time sample: 20,071 households.

Preliminary household-weighted prevalence of travel time of 30 minutes or more: approximately 14.48% among valid responses.

This is a descriptive estimate; design-based confidence intervals remain to be calculated.

The 30–89-minute category does not permit construction of an exact 60-minute threshold.

### 5.2 Healthcare sector reliance

Candidate variable: `hhw_hltfac`.

Tasks:
- Inspect all response categories.
- Verify public and private facility classifications.
- Identify unknown, unspecified and inapplicable responses.
- Establish the question's reference population and meaning.
- Construct a sector indicator if defensible.

### 5.3 Healthcare utilisation

Inspect the complete person dataset and official documentation for variables measuring:
- Healthcare consultation
- Healthcare service use
- Consultation reference periods
- Potential barriers to obtaining care, if available

Do not assume that medical aid membership or usual facility type measures actual utilisation.

### 5.4 Socioeconomic variables

Candidate household variables:

- `totmhinc`
- `fin_exp`
- `hwl_vehicle`
- Food insecurity variables beginning with `fsd_`

Candidate person variables:

- `education`
- `employ_Status1`
- `hlt_medi`

Economic indicators must be defined using documented response codes.

The primary economic ranking measure must be selected before examining substantive inequality results.

Where appropriate, household size or composition may be considered when interpreting economic resources.

### 5.5 Food insecurity

Candidate variables:

- `fsd_worried`
- `fsd_healthy`
- `fsd_fewfoods`
- `fsd_skipped`
- `fsd_ateless`
- `fsd_ranout`
- `fsd_hungry`
- `fsd_whlday`

Observed response codes:
- `1. Yes`
- `2. No`
- `9. Unspecified`

Before constructing a food-insecurity indicator:
1. Verify official question wording and recall period.
2. Examine missingness and response distributions.
3. Determine whether an established scoring approach is applicable.
4. Otherwise construct a clearly labelled, transparent proxy.
5. Document how incomplete responses are handled.

Do not present an exploratory count or binary indicator as a validated food-insecurity scale.

### 5.6 Geographic variables

Candidate variables:
- `prov`
- `geotype`
- `metro`

Verify all official categories and their relationships before modelling.

Do not assume that `geotype` codes 1, 2 and 3 have particular meanings without documentation.

### 5.7 Medical aid coverage

Person-level candidate variable: `hlt_medi`.

Observed categories:
- Yes
- No
- DO NOT KNOW
- Unspecified

Person-level medical aid indicators will be constructed directly from verified codes.

Household-level coverage indicators will be derived through aggregation of linked person records.

A household with all confirmed No responses may be classified as having no covered members.

A household with at least one confirmed Yes may be classified as having at least one covered member.

Unknown responses must not automatically be interpreted as No.

---

## 6. Statistical analysis plan

### 6.1 Analysis principles

The analysis will prioritise:
- Nationally representative estimates
- Correct survey weighting
- Design-based uncertainty
- Transparent outcome definitions
- Interpretable associations
- Absolute differences alongside relative measures
- Population profiles with adequate sample sizes
- Reproducible computational methods

No machine-learning classification, XGBoost, LightGBM or SHAP analysis is planned.

### 6.2 RQ1 — Descriptive inequalities

Calculate survey-weighted prevalence and 95% confidence intervals for each validated healthcare access outcome.

Compare estimates by:
- Province
- Settlement type
- Metropolitan status
- Household economic position
- Food insecurity
- Medical aid coverage
- Demographic characteristics, where relevant

Report:
- Weighted prevalence
- Unweighted sample size
- Survey-adjusted confidence intervals
- Absolute percentage-point gaps
- Relative prevalence ratios, where appropriate

For ordered socioeconomic groups, consider the Slope Index of Inequality and Relative Index of Inequality only when their assumptions and ranking definitions are justified.

Avoid interpreting differences based only on statistical significance.

### 6.3 RQ2 — Multivariable regression

Fit separate survey-adjusted regression models for each validated outcome.

For binary outcomes, use survey-weighted logistic regression.

Proposed household model sequence:

**M0 — Geographic characteristics**
- Province
- Settlement type
- Metropolitan status, if not redundant

**M1 — Socioeconomic and household characteristics**
- M0 variables
- Economic position
- Validated food insecurity measure
- Relevant household composition characteristics

**M2 — Enabling resources**
- M1 variables
- Vehicle ownership
- Household medical aid coverage

**M3 — Extended or sensitivity model**
- Additional variables such as transport mode, where conceptually appropriate

Do not automatically include variables that may be consequences or components of the outcome.

For person-level utilisation, develop a separate model appropriate to the eligible person population and questionnaire definition.

Report:
- Adjusted odds ratios
- 95% confidence intervals
- Design-based statistical tests
- Standardised predicted probabilities
- Average marginal effects or adjusted percentage-point contrasts

Interpret odds ratios carefully, particularly for common outcomes.

Check model convergence, sparse cells, collinearity and sample exclusions.

Use the official sampling design for inference, preferably through R's `survey` package or another demonstrably equivalent implementation.

### 6.4 RQ3 — Intersecting inequalities

Investigate whether socioeconomic disadvantage is associated with different access burdens across geographic contexts.

Candidate interactions:

- Economic disadvantage × settlement type
- Food insecurity × settlement type
- Economic disadvantage × province
- Medical aid coverage × geographic context

Select a small number of primary interactions before examining their results.

Other interactions will be explicitly exploratory.

Use design-based joint tests and model-based predicted probabilities.

Report contrasts on the probability scale, including uncertainty.

Do not interpret an interaction on the odds scale as automatically demonstrating an interaction on the probability scale.

### 6.5 Population vulnerability profiles

Construct transparent profiles using combinations of validated characteristics.

Candidate dimensions:
- Household economic position
- Food insecurity
- Settlement type
- Medical aid coverage
- Vehicle ownership

Estimate the prevalence of each healthcare access outcome within relevant profiles.

Profiles must have adequate sample sizes and survey support.

Do not create arbitrary vulnerability severity labels or claim that profiles represent causal mechanisms.

Where appropriate, estimate the weighted population size represented by each disadvantaged profile.

Distinguish groups with high disadvantage prevalence from groups contributing the greatest number of disadvantaged households.

### 6.6 Robustness and sensitivity

Evaluate:
- Alternative valid travel-time thresholds
- Alternative socioeconomic measures
- Alternative defensible food-insecurity definitions
- Missing-data assumptions
- Geographic model specifications
- Inclusion or exclusion of enabling-resource variables
- Sparse population profiles
- Differences between household-level and person-level findings

All sensitivity analyses must preserve the appropriate survey design.

---

## 7. Computational environment

### 7.1 Development environment

Primary environment: Visual Studio Code.

Primary language: Python.

Recommended libraries:
- pandas
- numpy
- pyarrow
- matplotlib
- scipy
- statsmodels
- pyyaml
- jupyter
- ipykernel

Use R with the `survey` package for complex survey estimation where required.

Python and R results must be linked through reproducible scripts and saved outputs.

### 7.2 Data storage

Raw CSV files must remain unchanged.

Processed datasets will be saved in compressed Parquet format.

Primary outputs:

`data/processed/household_analysis.parquet`

`data/processed/person_analysis.parquet`

Each dataset must retain the variables necessary for its corresponding estimand and survey design.

### 7.3 Reproducibility

Record:
- Original file hashes
- Software versions
- Variable definitions
- Inclusion and exclusion rules
- Survey design specifications
- Model specifications
- Deviations from the protocol
- Final analytical sample sizes

All analysis notebooks must run from top to bottom without manual alteration of intermediate results.

---

## 8. Notebook architecture

The project will use five notebooks.

### Notebook 01 — `01_data_preparation.ipynb`

**Title:** Data audit, linkage and analytical preparation.

**Research question:** Can the supplied household and person extracts support valid multidimensional healthcare access estimands?

**Inputs:**
- Household CSV
- Person CSV
- Official GHS questionnaire and metadata
- Project configuration

**Tasks:**
1. Audit file hashes, dimensions, duplicates and column names.
2. Validate household-person linkage.
3. Compare reported household sizes with linked person counts.
4. Validate survey weights, strata and PSUs.
5. Examine missingness and special response codes.
6. Validate healthcare travel-time categories.
7. Construct the primary travel-time outcome.
8. Audit and define public/private healthcare sector reliance.
9. Identify and validate person-level healthcare utilisation variables.
10. Construct socioeconomic and demographic indicators.
11. Construct defensible food-insecurity variables.
12. Derive household medical aid indicators from person records.
13. Calculate outcome-specific analytical sample flows.
14. Save compressed household and person Parquet datasets.
15. Run data integrity and transformation tests.

**Tables:**
- `T01_source_inventory.csv`
- `T02_linkage_integrity.csv`
- `T03_missingness_and_codes.csv`
- `T04_analysis_sample_flow.csv`
- `T05_variable_dictionary.csv`
- Additional audit tables where necessary

**Figures:**
- `F01_sample_flow.png/pdf`
- `F02_missingness_overview.png/pdf`, if meaningful

**Primary outputs:**
- `household_analysis.parquet`
- `person_analysis.parquet`

**Stop conditions:**

Stop or reduce scope if identifiers, survey design, healthcare outcome definitions or essential variable coding cannot be validated.

**Completed progress:**

Initial source inventory, linkage integrity, missingness audit, survey-design audit and travel-time outcome construction have been completed successfully.

These completed cells must be retained.

The next priority is to expand the healthcare outcome audit before continuing with food-insecurity construction.

---

### Notebook 02 — `02_descriptive_inequalities.ipynb`

**Title:** Healthcare access patterns and population inequalities.

**Research question:** How are healthcare accessibility, sector reliance and utilisation distributed across South African population groups?

**Inputs:**
- Household analysis Parquet
- Person analysis Parquet
- Verified survey design
- Variable dictionary

**Tasks:**
1. Describe the household and person analytical populations.
2. Estimate national healthcare travel-time burden.
3. Compare geographic accessibility across provinces and settlement types.
4. Examine socioeconomic travel-time inequalities.
5. Estimate public/private healthcare sector reliance.
6. Analyse person-level healthcare utilisation, if valid.
7. Compare healthcare outcomes across demographic and economic groups.
8. Calculate absolute and relative inequality measures.
9. Produce publication-quality descriptive figures.

**Tables:**
- `T06_population_characteristics.csv`
- `T07_geographic_accessibility.csv`
- `T08_socioeconomic_access_inequalities.csv`
- `T09_healthcare_sector_reliance.csv`
- `T10_healthcare_utilisation.csv`, if supported
- `T11_inequality_measures.csv`

**Figures:**
- `F03_provincial_accessibility.png/pdf`
- `F04_geographic_access_gaps.png/pdf`
- `F05_socioeconomic_access_gradients.png/pdf`
- `F06_healthcare_sector_inequalities.png/pdf`
- `F07_utilisation_inequalities.png/pdf`, if supported

**Primary output:**

A nationally representative description of healthcare access inequalities across multiple validated dimensions.

---

### Notebook 03 — `03_statistical_modelling.ipynb`

**Title:** Factors associated with healthcare access disadvantage.

**Research question:** Which socioeconomic, demographic, geographic and household factors are associated with healthcare access outcomes after adjustment?

**Inputs:**
- Processed datasets
- Survey design
- Prespecified model variables

**Tasks:**
1. Establish outcome-specific model populations.
2. Fit nested survey-weighted regression models.
3. Examine geographic and socioeconomic associations.
4. Evaluate enabling-resource associations.
5. Analyse healthcare sector reliance separately.
6. Analyse person-level utilisation separately, if valid.
7. Calculate adjusted odds ratios and confidence intervals.
8. Calculate average marginal effects.
9. Calculate standardised predicted probabilities.
10. Diagnose sparse cells, collinearity and model instability.

**Tables:**
- `T12_model_sample_flow.csv`
- `T13_nested_model_results.csv`
- `T14_adjusted_associations.csv`
- `T15_marginal_effects.csv`
- `T16_adjusted_probabilities.csv`

**Figures:**
- `F08_adjusted_associations_forest.png/pdf`
- `F09_adjusted_access_probabilities.png/pdf`

**Primary output:**

Interpretable, survey-adjusted evidence on characteristics associated with healthcare access disadvantage.

---

### Notebook 04 — `04_moderation_vulnerability.ipynb`

**Title:** Intersecting inequalities and disadvantaged population profiles.

**Research question:** How do socioeconomic and geographic disadvantages intersect, and which population groups experience the greatest healthcare access burden?

**Inputs:**
- Processed datasets
- Verified interaction variables
- Survey-adjusted model specifications

**Tasks:**
1. Fit prespecified socioeconomic × geographic interactions.
2. Conduct design-based joint interaction tests.
3. Calculate adjusted probabilities across relevant groups.
4. Estimate absolute differences between population profiles.
5. Construct interpretable household vulnerability profiles.
6. Compare profiles across geographic contexts.
7. Identify profiles with high access burden.
8. Estimate weighted population burden where appropriate.
9. Evaluate sparse cells and statistical uncertainty.

**Tables:**
- `T17_interaction_tests.csv`
- `T18_intersectional_probability_contrasts.csv`
- `T19_vulnerability_profiles.csv`
- `T20_profile_population_burden.csv`

**Figures:**
- `F10_intersectional_access_probabilities.png/pdf`
- `F11_vulnerability_profile_heatmap.png/pdf`
- `F12_population_disadvantage_profiles.png/pdf`

**Primary output:**

An evidence-based identification of population groups experiencing overlapping socioeconomic and geographic healthcare access disadvantage.

---

### Notebook 05 — `05_robustness_publication.ipynb`

**Title:** Robustness analysis, synthesis and publication outputs.

**Research question:** Are the main inequality findings robust, interpretable and suitable for policy translation?

**Inputs:**
- Processed datasets
- Model outputs
- Descriptive results
- Interaction results

**Tasks:**
1. Evaluate alternative travel-time thresholds.
2. Compare alternative economic measures.
3. Evaluate food-insecurity operationalisation.
4. Assess missing-data sensitivity.
5. Compare alternative regression specifications.
6. Check the stability of intersectional profiles.
7. Reconcile sample sizes and survey-weighted estimates.
8. Produce final manuscript tables and figures.
9. Summarise findings against each research question.
10. Develop a policy implications matrix.
11. Document limitations and analytical decisions.
12. Produce reproducibility and quality-control reports.

**Tables:**
- `T21_robustness_results.csv`
- `T22_results_summary.csv`
- `T23_sample_reconciliation.csv`
- `T24_policy_implications.csv`

**Figures:**
- `F13_sensitivity_analysis.png/pdf`, if informative

**Primary outputs:**
- `outputs/manuscript/manuscript_results_outline.md`
- `outputs/manuscript/policy_implications_matrix.csv`
- `outputs/manuscript/reproducibility_report.md`
- `outputs/manuscript/figure_table_manifest.csv`

---

## 9. Notebook execution and output rules

Each notebook must:

1. State its scientific objective.
2. Use the exact verified dataset variables.
3. Display all final tables inline using pandas.
4. Export final tables as CSV files to `outputs/tables/`.
5. Display figures inline using Matplotlib.
6. Export figures as 300-dpi PNG and vector PDF to `outputs/figures/`.
7. Include appropriate sample sizes and denominators.
8. Distinguish weighted from unweighted results.
9. Include confidence intervals where inferential estimates are reported.
10. Document exclusions, missingness and important limitations.
11. Run validation checks before saving final outputs.
12. Avoid fabricated codes, results, variable definitions or unsupported statistical assumptions.

Keep code straightforward and readable.

Use separate cells for distinct tasks.

Develop and validate one notebook at a time.

Do not generate unnecessary figures or tables.

---

## 10. Publication strategy

### 10.1 Intended contribution

The manuscript will examine healthcare inequality as a multidimensional population-health problem rather than reducing access to a single travel-time measure.

Its main contribution will be to identify:

- How healthcare access differs across socioeconomic and geographic groups.
- Whether geographic disparities persist after statistical adjustment.
- How healthcare sector reliance and utilisation vary across population groups.
- Which socioeconomic and geographic characteristics overlap in disadvantaged populations.
- Which groups may require greater policy attention.

### 10.2 Policy relevance

The study will consider implications for:
- Equitable geographic access to healthcare
- Public-sector healthcare planning
- Socioeconomic barriers to accessing care
- Healthcare coverage inequalities
- Rural and underserved communities
- National Health Insurance equity objectives
- Targeted healthcare access interventions

Policy recommendations must be grounded in empirical findings and should not imply that the cross-sectional analysis establishes causality or evaluates NHI implementation.

### 10.3 Potential journals

Candidate journals:
- International Journal for Equity in Health
- SSM – Population Health
- Health Policy and Planning

Journal scope, current quartile classification, manuscript requirements and recent related publications must be verified before submission.

A Q1 submission is a target, not a guaranteed outcome.

### 10.4 Manuscript structure

1. Introduction
2. Conceptual background and healthcare access inequalities
3. Data and methods
4. Results
   - Population characteristics
   - Geographic accessibility inequalities
   - Socioeconomic inequalities
   - Healthcare sector reliance
   - Healthcare utilisation, if measurable
   - Adjusted associations
   - Intersecting disadvantages
   - Population profiles
5. Discussion
6. Policy implications
7. Strengths and limitations
8. Conclusion

---

## 11. Quality-control and scientific safeguards

### 11.1 Measurement validity

Every outcome must correspond to an identifiable GHS question.

Do not substitute healthcare coverage, facility type or travel time for actual healthcare utilisation.

### 11.2 Survey validity

Use appropriate household or person weights and design-based variance estimation.

Avoid treating the linked person records as independent households.

### 11.3 Statistical validity

Use confidence intervals, absolute contrasts and appropriately specified regression models.

Avoid unnecessary significance testing and uncontrolled exploration of many interactions.

### 11.4 Interpretation

Cross-sectional associations must not be described as causal effects.

Adjusted associations do not establish structural mechanisms or intervention effectiveness.

### 11.5 Reproducibility

Preserve raw data, document transformations, export results consistently and retain the complete analytical decision record.

### 11.6 Novelty

Complete a focused literature review to establish how the study extends existing South African healthcare access inequality research.

Novelty must be demonstrated, not assumed.

---

## 12. Immediate implementation plan

**Current position:** Notebook 01, Cell 8 completed.

Completed:
- Raw data loading
- Source inventory
- Household-person linkage checks
- Missingness and response-code audit
- Survey design validation
- Travel-time category validation
- Binary travel-time outcome construction

**Next action:**

Before constructing food insecurity or other explanatory variables, audit all available healthcare-related variables in the household and person datasets.

Determine whether the extracts support:
1. Geographic healthcare accessibility
2. Public/private healthcare sector reliance
3. Person-level healthcare utilisation
4. Other defensible access outcomes

Then finalise the outcome register and continue Notebook 01.

**Decision gate:**

Do not proceed to substantive inequality modelling until the healthcare outcome definitions, analytical populations and survey methodology have been validated.

---

## 13. Instructions for AI-assisted notebook development

This protocol is the governing analytical specification for the project.

When generating notebook code:

- Follow the five-notebook architecture.
- Work one cell at a time.
- Do not overcomplicate the code.
- Explain each cell's purpose.
- Use actual observed variable names and response categories.
- Inspect data before recoding variables.
- Preserve all completed valid analysis work.
- Do not invent missing variables or response codes.
- Use appropriate survey weights and design-based inference.
- Display and export final tables and figures.
- Include simple validation assertions.
- Stop and request clarification when a critical variable cannot be defensibly defined.
- Keep household and person estimands separate.
- Do not introduce machine learning or SHAP.
- Prioritise scientifically defensible, policy-relevant results.

**Final research objective:**

Produce a rigorous, reproducible and policy-relevant study that identifies the socioeconomic, demographic and geographic inequalities shaping healthcare access in South Africa, with particular attention to population groups experiencing intersecting forms of disadvantage.
