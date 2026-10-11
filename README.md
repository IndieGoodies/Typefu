# Typefu Actions

Community actions for Typefu, the macOS text expander with a selection bar. Select text in any app, and an action searches it, rewrites it, or sends it to another app.

Each action is one JSON file in [`actions/`](actions), named after its id. Typefu ships with every action in this repository; you can also install one yourself, or write your own and send a pull request.

## Install an action

1. Download the action's `.json` file (open it, then **Download raw file**).
2. In Typefu, open **Library ▸ Custom Actions** and choose **Import Actions…** in the toolbar.
3. Arrange it in **Settings ▸ Selection Bar ▸ Layout**.

Actions in this repository also appear in the **Gallery** sections of **Library ▸ Custom Actions** in the next Typefu release. Choose one and click the **+** button (Add to My Actions).

Typefu asks before importing an action that runs a shell script or AppleScript. Those run with your user account's access, so only import ones you trust.

## Write an action

```json
{
  "$schema": "https://raw.githubusercontent.com/indiegoodies/Typefu/main/schema.json",
  "schemaVersion": 1,
  "id": "reverse-words",
  "version": "1.0.0",
  "name": "Reverse Words",
  "summary": "Reverses the order of the words.",
  "icon": "arrow.left.arrow.right",
  "category": "text",
  "author": "Your Name",
  "kind": "javaScript",
  "script": "text.split(/\\s+/).reverse().join(\" \")",
  "output": "replace"
}
```

| Key | Required | Meaning |
|---|---|---|
| `schemaVersion` | yes | Always `1` for now. |
| `id` | yes | A kebab-case name that never changes, such as `reverse-words`. The file is `actions/<id>.json`. |
| `version` | yes | The action's version. Bump it when you change the action. |
| `name`, `summary` | yes | Shown in the selection bar and the gallery. |
| `icon` | yes | An [SF Symbol](https://developer.apple.com/sf-symbols/) name. |
| `category` | yes | `text`, `markdown`, `developer`, `search`, `reference`, `maps` or `apps`. Groups the action in Typefu's gallery and the list below. |
| `author` | yes | Your name. |
| `kind` | yes | `url`, `javaScript`, `shell`, `appleScript` or `shortcut`. |
| `script` | yes | The URL, code or Shortcut name. See below. |
| `output` | no | `replace` (default for scripts), `insertAfter`, `copy`, `show` or `none` (default for URLs). |
| `requirements` | no | When the action is offered: `minLength`, `maxLength`, `regex` (must match the whole selection), `isURL`, `isEmail`, `isPath`, `includeApps`, `excludeApps`. |
| `timeout` | no | Seconds before a shell, AppleScript or Shortcut action is stopped. Default 10. |
| `minAppVersion` | no | The oldest Typefu that can run the action. |

[`schema.json`](schema.json) describes the format. Editors that understand JSON Schema check your file as you type when it has the `$schema` line.

### Kinds

- **url**: opens a URL. `{text}` becomes the selection, URL-encoded. Add Typefu pipes to change it first, like `{text | lower}`.
- **javaScript**: runs in JavaScriptCore with no file or network access. The selection is in `text`, and the value of the last expression is the result. You can also `return` a value, or define `function run(text) { … }`. A `typefu` object offers `typefu.input.text`, `typefu.openURL(url)` and `typefu.copy(text)`. Throw an error to fail without changing the text. If the script uses `return` anywhere, Typefu runs it as a function body, so a `return` inside a callback isn't enough: return the final value at the top level, or use `function run(text)`.
- **shell**: runs with `zsh`. The selection is on standard input and in `$EXPANDER_TEXT`; standard output is the result.
- **appleScript**: the selection is in `selectedText`; the script's result is the result.
- **shortcut**: runs the named Shortcut with the selection as input; its output is the result.

### Check your file

```sh
python3 scripts/validate.py
```

The same check runs on every pull request.

## Actions

### Text

| Action | What it does | Kind |
|---|---|---|
| [Alternating Case](actions/alternating-case.json) | wRiTeS tHe SeLeCtIoN lIkE tHiS. | JavaScript |
| [Comma List](actions/comma-list.json) | Turns lines into a comma-separated list, or a comma-separated list into lines. | JavaScript |
| [Join Lines](actions/join-lines.json) | Joins the lines into one, separated by spaces. | JavaScript |
| [Remove Empty Lines](actions/remove-empty-lines.json) | Removes blank lines. | JavaScript |
| [Reverse Lines](actions/reverse-lines.json) | Reverses the order of the lines. | JavaScript |
| [ROT13](actions/rot13.json) | Shifts letters by 13 places. Run it again to undo. | JavaScript |
| [Shuffle Lines](actions/shuffle-lines.json) | Puts the lines in random order. | JavaScript |
| [Slugify](actions/slugify.json) | Turns the selection into a URL slug. | JavaScript |
| [Straighten Quotes](actions/straighten-quotes.json) | Replaces curly quotes with straight ones. | JavaScript |
| [Sum Numbers](actions/sum-numbers.json) | Adds up every number in the selection. | JavaScript |
| [Wrap in Parentheses](actions/wrap-parentheses.json) | Wraps the selection in parentheses. | JavaScript |
| [Wrap in Quotes](actions/wrap-quotes.json) | Wraps the selection in curly quotes. | JavaScript |

### Markdown

| Action | What it does | Kind |
|---|---|---|
| [Blockquote](actions/markdown-blockquote.json) | Quotes the selection in Markdown. | JavaScript |
| [Bullet List](actions/markdown-bullet-list.json) | Turns lines into a Markdown bullet list. | JavaScript |
| [Checklist](actions/markdown-checklist.json) | Turns lines into a Markdown checklist. | JavaScript |
| [Code Block](actions/markdown-code-block.json) | Wraps the selection in a fenced code block. | JavaScript |
| [Inline Code](actions/markdown-inline-code.json) | Wraps the selection in backticks. | JavaScript |
| [Markdown Link](actions/markdown-link.json) | Turns a link into a Markdown link. | JavaScript |
| [Numbered List](actions/markdown-numbered-list.json) | Turns lines into a numbered Markdown list. | JavaScript |

### Developer

| Action | What it does | Kind |
|---|---|---|
| [Apple Developer](actions/search-apple-developer.json) | Searches Apple's developer documentation for the selection. | URL |
| [Escape HTML](actions/escape-html.json) | Escapes &, <, >, and quotes as HTML entities. | JavaScript |
| [Extract Email Addresses](actions/extract-emails.json) | Copies every email address in the selection, one per line. | JavaScript |
| [Extract Links](actions/extract-urls.json) | Copies every link in the selection, one per line. | JavaScript |
| [MDN](actions/search-mdn.json) | Searches the MDN web docs for the selection. | URL |
| [Open GitHub Repo](actions/open-github-repo.json) | Opens a GitHub repository from owner/repo. | URL |
| [Search GitHub](actions/search-github.json) | Searches GitHub for the selection. | URL |
| [Stack Overflow](actions/search-stackoverflow.json) | Searches Stack Overflow for the selection. | URL |
| [Toggle # Comment](actions/toggle-hash-comment.json) | Comments or uncomments lines with #. | JavaScript |
| [Toggle // Comment](actions/toggle-line-comment.json) | Comments or uncomments lines with //. | JavaScript |
| [Unescape HTML](actions/unescape-html.json) | Turns HTML entities back into characters. | JavaScript |
| [Unicode Code Points](actions/unicode-code-points.json) | Shows the Unicode code point of each character. | JavaScript |
| [Unix Timestamp to Date](actions/unix-timestamp.json) | Converts a Unix timestamp in seconds or milliseconds to an ISO 8601 date. | JavaScript |
| [Validate JSON](actions/validate-json.json) | Checks whether the selection is valid JSON. | JavaScript |

### Search

| Action | What it does | Kind |
|---|---|---|
| [Amazon](actions/search-amazon.json) | Searches Amazon for the selection. | URL |
| [Bing](actions/search-bing.json) | Searches Bing for the selection. | URL |
| [DuckDuckGo](actions/search-duckduckgo.json) | Searches DuckDuckGo for the selection. | URL |
| [Google](actions/search-google.json) | Searches Google for the selection. | URL |
| [IMDb](actions/search-imdb.json) | Searches IMDb for the selection. | URL |
| [Kagi](actions/search-kagi.json) | Searches Kagi for the selection. | URL |
| [Reddit](actions/search-reddit.json) | Searches Reddit for the selection. | URL |
| [YouTube](actions/search-youtube.json) | Searches YouTube for the selection. | URL |

### Reference

| Action | What it does | Kind |
|---|---|---|
| [Google Translate](actions/google-translate.json) | Translates the selection to English in Google Translate. | URL |
| [Merriam-Webster](actions/merriam-webster.json) | Looks up a word in Merriam-Webster. | URL |
| [Open DOI](actions/doi.json) | Opens the paper for a DOI like 10.1000/182. | URL |
| [Urban Dictionary](actions/urban-dictionary.json) | Looks up slang on Urban Dictionary. | URL |
| [Wayback Machine](actions/wayback-machine.json) | Shows archived copies of a link on the Wayback Machine. | URL |
| [Wikipedia](actions/wikipedia.json) | Looks up the selection on English Wikipedia. | URL |
| [Wolfram Alpha](actions/wolfram-alpha.json) | Asks Wolfram Alpha about the selection. | URL |

### Maps

| Action | What it does | Kind |
|---|---|---|
| [Apple Maps](actions/apple-maps.json) | Finds the selection in Apple Maps. | URL |
| [Google Maps](actions/google-maps.json) | Finds the selection in Google Maps. | URL |
| [OpenStreetMap](actions/openstreetmap.json) | Finds the selection on OpenStreetMap. | URL |

### Apps

| Action | What it does | Kind |
|---|---|---|
| [Add to Things](actions/things-add.json) | Adds the selection as a to-do in Things. | URL |
| [New Bear Note](actions/bear-create.json) | Creates a Bear note with the selection. | URL |
| [New Draft](actions/drafts-create.json) | Creates a draft in Drafts with the selection. | URL |
| [New Mail Message](actions/mail-new-message.json) | Starts a new email with the selection as the body. | URL |
| [Run in Terminal](actions/run-in-terminal.json) | Runs the selection as a command in a new Terminal window. | AppleScript |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). By sending a pull request you agree that your action is released under the [MIT License](LICENSE) and may ship inside Typefu.
