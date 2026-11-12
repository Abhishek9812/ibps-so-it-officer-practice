# Scale II Test Desk

Practice and timed mock tests for the IBPS RRB Officer Scale II (IT Officer) exam.

- **Practice mode:** the answer and solution appear as soon as you choose an option.
- **Timed mode:** sectional clock, question palette, mark for review, solutions after submit.
- **Scoring:** exam marking, with 25% negative marking. English and Computer Knowledge carry 0.5 marks per question.
- Attempts and scorecards are saved in your own browser only.

## Structure

- `index.html` – the whole app (no build step)
- `tests/index.json` – list of tests
- `tests/day1.json` – Day 1 set: 6 sections × 50 questions
- `tools/` – question sources and scripts that build the test files

## Rebuild the questions

```
cd tools
python3 gen.py     # quant and reasoning, answers computed by script
python3 build.py   # writes ../tests/day1.json and ../tests/index.json
```

Questions are original practice questions written to the exam pattern. They are not official IBPS questions.
