---
name: analyze
description: Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.
---

# /analyze — Answer Data Questions (Aleut Federal)

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

## Aleut Federal Context — Federal-Contractor Data Questions

Most analytical questions come from one of three buckets:

1. **Internal program / financial** — by-program P&L, indirect rate posture, ICS prep, billings vs revenue, EAC, backlog, headcount by clearance/CMMC/contract.
2. **External federal market** — SAM.gov solicitations, USAspending awards, FPDS, agency forecasts, competitor activity, GSA Schedule pricing.
3. **Compliance posture** — FAR 52.219-14 self-performance, FAPIIS status of subs, OFCCP utilization, mandatory-disclosure log counts, CMMC POA&M aging, CPARS trends.

Hard rules:

- **No CUI in unauthorized environments.** Don't pull CUI from production into a notebook on an uncontrolled endpoint or commercial AI tool.
- **PII** handled per Privacy Act and system PIA; minimum-necessary.
- **Audit trail** — assume access is logged (NIST 800-53 AU-2).
- **Source-selection sensitivity (FAR 3.104)** — analyses of competitor pursuits or our own proposal data are privileged and PIA-sensitive.
- **Aggregate / mark CUI** before sharing.
- **Records retention** per FAR 4.703 / agency.

Answer a data question, from a quick lookup to a full analysis to a formal report.

## Usage

```
/analyze <natural language question>
```

## Workflow

### 1. Understand the Question

Parse the user's question and determine:

- **Complexity level**:
 - **Quick answer**: Single metric, simple filter, factual lookup (e.g., "How many users signed up last week?")
 - **Full analysis**: Multi-dimensional exploration, trend analysis, comparison (e.g., "What's driving the drop in conversion rate?")
 - **Formal report**: Comprehensive investigation with methodology, caveats, and recommendations (e.g., "Prepare a quarterly business review of our subscription metrics")
- **Data requirements**: Which tables, metrics, dimensions, and time ranges are needed
- **Output format**: Number, table, chart, narrative, or combination

### 2. Gather Data

**If a data warehouse MCP server is connected:**

1. Explore the schema to find relevant tables and columns
2. Write SQL query(ies) to extract the needed data
3. Execute the query and retrieve results
4. If the query fails, debug and retry (check column names, table references, syntax for the specific dialect)
5. If results look unexpected, run sanity checks before proceeding

**If no data warehouse is connected:**

1. Ask the user to provide data in one of these ways:
 - Paste query results directly
 - Upload a CSV or Excel file
 - Describe the schema so you can write queries for them to run
2. If writing queries for manual execution, use the `sql-queries` skill for dialect-specific best practices
3. Once data is provided, proceed with analysis

### 3. Analyze

- Calculate relevant metrics, aggregations, and comparisons
- Identify patterns, trends, outliers, and anomalies
- Compare across dimensions (time periods, segments, categories)
- For complex analyses, break the problem into sub-questions and address each

### 4. Validate Before Presenting

Before sharing results, run through validation checks:

- **Row count sanity**: Does the number of records make sense?
- **Null check**: Are there unexpected nulls that could skew results?
- **Magnitude check**: Are the numbers in a reasonable range?
- **Trend continuity**: Do time series have unexpected gaps?
- **Aggregation logic**: Do subtotals sum to totals correctly?

If any check raises concerns, investigate and note caveats.

### 5. Present Findings

**For quick answers:**
- State the answer directly with relevant context
- Include the query used (collapsed or in a code block) for reproducibility

**For full analyses:**
- Lead with the key finding or insight
- Support with data tables and/or visualizations
- Note methodology and any caveats
- Suggest follow-up questions

**For formal reports:**
- Executive summary with key takeaways
- Methodology section explaining approach and data sources
- Detailed findings with supporting evidence
- Caveats, limitations, and data quality notes
- Recommendations and suggested next steps

### 6. Visualize Where Helpful

When a chart would communicate results more effectively than a table:

- Use the `data-visualization` skill to select the right chart type
- Generate a Python visualization or build it into an HTML dashboard
- Follow visualization best practices for clarity and accuracy

## Examples

**Quick answer:**
```
/analyze How many new users signed up in December?
```

**Full analysis:**
```
/analyze What's causing the increase in support ticket volume over the past 3 months? Break down by category and priority.
```

**Formal report:**
```
/analyze Prepare a data quality assessment of our customer table -- completeness, consistency, and any issues we should address.
```

## Tips

- Be specific about time ranges, segments, or metrics when possible
- If you know the table names, mention them to speed up the process
- For complex questions, Claude may break them into multiple queries
- Results are always validated before presentation -- if something looks off, Claude will flag it
