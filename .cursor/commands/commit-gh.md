Act as an expert software developer with access to the integrated terminal. Your task is to analyze a summary of code modifications and prepare a complete git commit.

Follow these steps precisely:
1.  **Execute the command `git diff --stat`** to get a summary of all unstaged changes. This command provides a list of modified files without the full content diff. Do not ask for the output; obtain it yourself.
2.  Based on the file list and change summary from the command, **create a commit message in English** that strictly follows the Conventional Commits specification.
    * The message must have a **type** (e.g., feat, fix, chore, docs, refactor).
    * It must have a concise **subject** in the imperative mood (e.g., "add login feature").
    * Infer the purpose of the changes from the file paths and summary. If the intent isn't perfectly clear, create a reasonable and general message.
3.  **Provide the complete and final sequence of terminal commands** to:
    a) Stage all the changes (`git add .`).
    b) Commit them using the generated message.
    c) Push the commit to the remote branch.