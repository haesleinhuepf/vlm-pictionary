# VLM Pictionary - with human in the loop

Play pictionary with Vision-Language-Models by drawing on an [ipycanvas](https://ipycanvas.readthedocs.io/en/latest/).

![](demo.gif)

Inspired by Paul Calcraft's [tweet](https://x.com/paul_cal/status/1850262678712856764) and Simon Willison's [post](https://bsky.app/profile/simon.fedi.simonwillison.net.ap.brid.gy/post/3l7erqn5dkby2).

## Installation

VLM Pictionary comes as a Jupyter Notebook and a set of requirements you can install using pip.

```
git clone https://github.com/haesleinhuepf/vlm-pictionary
cd vlm-pictionary
pip install -r requirements.txt
```

You also need to configure API keys to access the VLM service providers:
* `OPENAI_API_KEY`: [OpenAI (gpt-4o)](https://openai.com/blog/openai-api)
* `ANTHROPIC_API_KEY` [Anthropic (claude)](https://www.anthropic.com/api)
* `GOOGLE_API_KEY` [Google AI (gemini)](https://ai.google.dev/gemini-api/docs/api-key)

You can then execute it like this:
```
jupyter lab pictionary.ipynb
```
