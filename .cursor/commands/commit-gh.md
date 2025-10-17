Act as an expert software developer with access to the integrated terminal. Your task is to fully prepare a git commit for the staged changes.

Follow these steps precisely:
1.  **Execute the command `git diff --staged`** in the terminal to get the context of the changes. Do not ask me for the diff output; you must obtain it yourself.
2.  Based on the output of that command, **create a commit message in English** that strictly follows the Conventional Commits specification.
    * The message must have a **type** (e.g., feat, fix, chore, docs, refactor).
    * It must have a concise **subject** in the imperative mood (e.g., "add login feature" not "added login feature").
    * If necessary, include a more detailed **body** explaining the 'what' and 'why' of the changes.
3.  **Provide the complete and final terminal commands** to commit the changes using the generated message and then push them to the remote branch.