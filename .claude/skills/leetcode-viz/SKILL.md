---
name: leetcode-viz
description: Generate an interactive Artifact that lets the user explore a LeetCode problem's actual mechanics hands-on (not a pre-solved walkthrough), with progressive hints and the full solution held behind an opt-in reveal. Use when the user asks to visualize, play with, or understand a LeetCode problem, or invokes /leetcode-viz. Not for plain text explanations (just answer those directly) — this is specifically for the interactive-artifact format.
---

# LeetCode Interactive Playground

Produces a self-contained Artifact built around a **playground**: a working simulation of the problem's actual rules that the user operates themselves (click stones, move pointers, feed inputs) to build intuition before seeing any answer. This is deliberately not a pre-solved animation — the point is the user works through it, the same way they'd work through it on paper, except the mechanics update live instead of by hand. Hints and the full solution exist too, but stay collapsed until the user asks for them.

There is no video model available — "visualization" here means a real interactive artifact, not a rendered video file.

## Input

`args` is a LeetCode problem number, name, URL, or "this file" / empty (use the currently open/selected file in the IDE context). If ambiguous, ask.

## Steps

1. **Understand the problem's raw mechanics before you touch the solution.** Read the problem (from the repo file if present, otherwise from what you know / the user's paste — do not fetch leetcode.com). Identify what the user actually *does* in the problem: which moves/operations are legal, what state changes, what triggers a win/loss/answer. This is what becomes the playground — you don't need the optimal algorithm figured out yet to build it, only the rules.

2. **Design the playground as free play, not guided play.** The user should be able to take suboptimal or exploratory actions and see the honest consequence, not be railroaded toward the answer. Concretely:
   - Let them control input where it makes sense (edit the array/stones/string, randomize, or step through a few provided example inputs) so they can test multiple cases, not just one fixed trace.
   - Every action updates real state on screen immediately (running sum, current player, remaining items, pointer positions — whatever the problem tracks).
   - Enforce only the problem's actual rules (e.g. whose turn it is, terminal conditions) — never enforce "the optimal move," and never label a move as wrong just because it isn't part of the intended solution.
   - Detect and display the problem's real terminal/answer condition live (e.g. "Alice loses — sum divisible by 3" or "target found at index 4"), computed by *simulating the rule*, not by looking up a precomputed answer — hand-trace this yourself first so the simulation logic is correct before writing HTML/JS.

3. **Then, separately, solve it yourself in full** (intuition, optimal approach, complexity) — you still need this for hints and the reveal, but it must not leak into the playground's behavior or framing.

4. **Load `artifact-design`, then `artifact-diagramming`** before writing any HTML. If the visualization involves charts/heatmaps/stat tiles, also load `dataviz`. Follow their guidance for palette, theme-awareness (light/dark), and diagram legibility — do not freehand colors or SVG layout.

5. **Build the artifact** as a single HTML file, ordered top to bottom by reveal:
   - **Playground** (open by default, the main event): the interactive simulation from steps 1-2, with controls to reset/randomize/edit input.
   - **Hints** (collapsed `<details>` elements, 2-4 of them, ordered weakest → strongest): nudges toward the key insight without stating it outright — a question to ask themselves, a pattern to notice, a suggestion of what to try in the playground. The last hint can name the core idea but should still stop short of code.
   - **Full solution** (collapsed, closed by default, one `<details>` behind a clear "Reveal solution" label): the code, a synced trace/animation over one concrete example (this is where the old solved-walkthrough treatment belongs), and complexity. Same content bar as a normal walkthrough — just gated behind an explicit click so it can't be seen accidentally.
   No external requests (per Artifact constraints); keep it one file.

6. **Resources footer (optional, only if the user's request implies wanting links, not just visualization):** a short list of 2-4 external reference links — only include a URL you actually have from the user or high-confidence public knowledge (problem's canonical `leetcode.com/problems/<slug>/`); never fabricate a link.

7. **Publish** via the Artifact tool. Title = short problem name (e.g. "Stone Game IX"), favicon = a single fitting emoji, kept stable if the user asks you to regenerate/update the same problem later (use the same file path to redeploy rather than creating a new artifact).

8. Tell the user in 1-2 sentences what the playground lets them do — don't restate the hints or solution in chat, the artifact carries it, and stating it in chat defeats the point of gating it.

## What NOT to do

- Don't build a pre-solved animation as the primary experience — that's the old, wrong version of this skill. The playground comes first and is driven by the user's own clicks.
- Don't let the playground silently reference or depend on the optimal algorithm (e.g. don't grey out "non-optimal" moves, don't auto-play the best move) — it must reflect only the problem's stated rules.
- Don't skip the hand-trace of the simulation logic before writing it into HTML/JS — that's how off-by-one / wrong-terminal-condition bugs happen.
- Don't put the solution or its code anywhere visible before the user expands the reveal section — including in hint text, image alt text, or code comments in earlier sections.
- Don't build a multi-problem index/dashboard unless the user asks for one; one problem per invocation, one artifact per problem.
- Don't fetch leetcode.com or other external sites for the problem statement — work from what's in the repo file or what the user pasted.
