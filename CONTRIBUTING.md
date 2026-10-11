# Contributing an action

Thanks for sharing an action. Every accepted action ships inside Typefu, so each one is reviewed by hand.

## Steps

1. Fork this repository.
2. Add your file as `actions/<id>.json`, where the id is a short kebab-case name for the action, like `reverse-words`. If the name is taken, pick a more specific one.
3. Add a row for it to the table in the README, under its category.
4. Test it in Typefu: **Library ▸ Custom Actions ▸ Import Actions…**, then use **Try It** in the editor.
5. Run `python3 scripts/validate.py`.
6. Open a pull request. Say what the action does, and give a sample selection with the result you expect.

To change an existing action, edit its file and bump `version`. Never change an `id`; Typefu uses it to match installed copies and the user's bar layout.

## What gets accepted

- **It does one clear thing** that isn't already covered by Typefu's built-in actions or another file here.
- **Prefer `url` and `javaScript`.** They can't touch your files. `shell` and `appleScript` actions are accepted when there's no other way, and get a closer review. Explain why in the pull request.
- **No secrets.** Don't put API keys, tokens, passwords or private URLs in a file.
- **No network calls from scripts.** Opening a website with a `url` action is fine; sending the selection somewhere in the background isn't, for now.
- **Readable code.** No minified or obfuscated scripts.
- **Say what leaves the Mac.** If the action opens a website with the selection, the summary should make that clear (for example "Searches Google for the selection").
- **Names and icons:** a short name in Title Case, and an SF Symbol that exists in the current macOS. Don't use other companies' logos.

Some ideas can't be data. Actions that need their own UI, live results on the button, or access to Typefu's own data (snippets, lists, AI presets) are built into the app in Swift. Open an issue to suggest one of those instead.

## License

By contributing you agree that your action is released under the MIT License in [LICENSE](LICENSE) and may be included in Typefu.
