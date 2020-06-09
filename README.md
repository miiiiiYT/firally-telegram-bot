# telegram-bot-balena 
This is a bot for telegram, running on [@hahaYesIAmRobot](https://t.me/hahaYesIAmRobot)

This as a balena project exists, but:
- It doesn't work(yet)
- Don't try it, it may break your device or balena Application
- You are free to make a pull request, if you get it fixed. (But we are also working on it.)
 
## Token_var
> [!TIP]
> You maybe saw the `from token_var import token_updater` line in the `runtime.py`.
> That is for safety, so the Telegram API Token isn't published.
> 
> There is a `token_var.py` file at the root directory, it contains:
> ```python
> token_updater="YOUR TOKEN HERE"
> ```
> That then imports the `token_updater` variable, so no token is exposed.