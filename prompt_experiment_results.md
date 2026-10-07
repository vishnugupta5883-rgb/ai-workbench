# Prompt Engineering Experiment — Results Template

Fill this in as you observe the output from each experiment.

## Experiment 1: Instruction Specificity

| Level | Word Count | Format | Usefulness (1-5) | Notes |
|-------|-----------|--------|-------------------|-------|
| Vague ("Summarize this") |137|free text |2|It's like generalize response to summarize the prompt |
| Specific ("3 bullet points") |163 | Bullet points | 3| It's lttlie speific and summarized in 3 bullet points|
| Highly specific ("3 bullets, <15 words, business focus") |151 |bullet points |5 |It's concise, proper formatted and business specific |

**My observation:**  
_What changes as specificity increases?_
When instruction is more specific and limiting the words then response would be more concised and to the point.

---

## Experiment 2: Persona / Audience

| Audience | Vocabulary Level | Depth | Tone | Notes |
|----------|-----------------|-------|------|-------|
| CEO |Advanced |Straight  |Professional |It's talking about AI business impact,opportunity and risk |
| 10-year-old |Basic |high | Basic| talking about AI impact in normal life |
| Software Engineer |Professional | technical | Professional | talking about AI challenges and governance|

**My observation:**  
_How does audience change the same information?_
It' huge difference in the response based on the audience.
---
## Experiment 3: Output Format

| Format | Parseable by code? | Structure | Best use case |
|--------|-------------------|-----------|---------------|
| Free text | No|free text |Brainstorming |
| JSON | Yes|JSON | It's good for Initial draft of newproposal|
| Markdown table | Yes|Table | Impact analysis |

**My observation:**  
_When would you use each format in a real application?_
Free from text : We can use for Brainstorming and no awareness about topic
JSON : Unstructured like log, audio, video,image we want to analyse.
Markdown table : structured data that we can use for depth analysis.
---

## Experiment 4: Temperature

| Temperature | Run 1 vs Run 2 | Creativity | Consistency |
|-------------|----------------|------------|-------------|
| 0.0 | Identical / Different |No | Yes|
| 0.7 | Identical / Different |Balanced |Yes |
| 1.5 | Identical / Different |Yes |No |

**My observation:**  
_What temperature would you use for: (a) a legal document? (b) a marketing tagline?_
(a) a Legal document - tempresture -0.0
(b) a marketing tagline - tempreature - 1.5
---

## Overall Key Findings

1. The variable with the BIGGEST effect on output quality was: tempreature
2. The most surprising result was: Specificity
3. One thing I'd do differently in my prompts from now on: Persona
