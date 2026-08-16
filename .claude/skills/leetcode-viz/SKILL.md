---
name: leetcode-viz
description: Generate an animated, interactive walkthrough of a LeetCode problem's solution as a published Artifact. Use when the user asks to be taught/explained a LeetCode problem visually, asks for a "video tutorial" or "animated walkthrough" of a problem, or invokes /leetcode-viz. Not for plain text explanations (just answer those directly) — this is specifically for the animated-artifact teaching format.
---

# LeetCode Visual Walkthrough

Produces a self-contained animated Artifact that teaches one LeetCode problem: play/pause/step controls driving a visualization of the algorithm on a concrete example, synced to highlighted source code and a written explanation. This is a *substitute* for a video — there is no video model available, so the teaching happens through generated animation, not a rendered file.

## Input

`args` is a LeetCode problem number, name, URL, or "this file" / empty (use the currently open/selected file in the IDE context). If ambiguous, ask.

## Steps

1. **Solve it yourself first, in full, before designing anything.** Read the problem (from the repo file if present, otherwise from what you know / the user's paste — do not fetch leetcode.com). Work out the intuition, the optimal approach, and complexity. If the repo file has an empty method stub, fill it in with a correct, idiomatic solution and a short explanatory comment only where the reasoning is non-obvious (per this project's usual comment policy).

2. **Pick ONE concrete example to animate** — small enough to step through by hand (e.g. an example from the problem statement, or a minimal one you construct). The animation must show *this exact example* executing, not an abstract diagram. Trace through your own solution by hand first so every animated frame is actually correct — do not improvise frames while writing HTML.

3. **Load `artifact-design`, then `artifact-diagramming`** before writing any HTML. If the visualization involves charts/heatmaps/stat tiles, also load `dataviz`. Follow their guidance for palette, theme-awareness (light/dark), and diagram legibility — do not freehand colors or SVG layout.

4. **Build the artifact** as a single HTML file with three synced regions:
   - **Stage**: the animation itself (array cells, tree nodes, pointers, stack/queue, whatever fits the problem's actual data structure) with Play / Pause / Step / Reset and a speed control. Each step should update state visibly (highlight the cell being touched, show a running variable like `sum` or `cnt[]` updating live).
   - **Code panel**: the final solution code, with the current line highlighted in sync with the animation step. Plain `<pre>`/`<code>` with a highlighted-line class is enough — no syntax-highlighting library (CSP blocks external scripts).
   - **Explanation panel**: 3-6 short sections — intuition, why the naive approach is too slow (if relevant), the key insight, complexity. Terse, not a textbook.
   Keep it to one HTML file, no external requests (per Artifact constraints).

5. **Resources footer (optional, only if the user's request implies wanting links, not just video):** a short list of 2-4 external reference links (e.g. the official LeetCode problem URL if known from the user, NeetCode-style pattern name) as plain `<a>` text — only include a URL if you actually have it from the user or high confidence public knowledge (problem's canonical `leetcode.com/problems/<slug>/`); never fabricate a link.

6. **Publish** via the Artifact tool. Title = short problem name (e.g. "Stone Game IX"), favicon = a single fitting emoji, kept stable if the user asks you to regenerate/update the same problem later (use the same file path to redeploy rather than creating a new artifact).

7. Tell the user in 1-2 sentences what the artifact covers — don't restate the whole explanation in chat, the artifact carries it.

## What NOT to do

- Don't claim it's a "video" — call it an animated/interactive walkthrough.
- Don't skip step 2's hand-trace and wing the animation logic directly in HTML/JS — that's how off-by-one frames happen.
- Don't build a multi-problem index/dashboard unless the user asks for one; one problem per invocation, one artifact per problem.
- Don't fetch leetcode.com or other external sites for the problem statement — work from what's in the repo file or what the user pasted.
