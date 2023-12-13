# making-a-PR

Repository for illustrative purposes on how to make a code contribution to a
large project.

## Steps:

For any of these steps, make sure to reach out the project maintainers if you
need help! There's almost always a channel for this (gitter, email, even
twitter), but you can also just make an issue asking for help, or maybe a
comment in the GitHub Discussions tab.

1. If it exists, read the `CODE-OF-CONDUCT.md` in the root of the repository to
   understand what's expected of you when working with the project.
2. If it exists, read `CONTRIBUTING.md` in the root of the repository. This
   should outline all the steps needed when making a new contribution. Any
   contradictions between that document and these steps -- though there should
   be few -- should be resolved by trusting whatever is in `CONTRIBUTING.md`.
   - It's possible these new contributor steps exist in a different place, e.g.
     the documentation. See this
     [nice guide on contributing to Matplotlib](https://matplotlib.org/devdocs/devel/contribute.html#start-contributing)
     for an example of this!
   - If there are no guidelines of any form, you can inspect past PRs to get an
     idea of how contributions look, and the interactions between the
     maintainers and contributors. In fact, _this is a good idea regardless!_

You should now have an idea on how to set up a local development environment.

3. Depending on the project, you should do one of two things:

- Directly clone the repo, and make a new branch with a _descriptive name_.
  Examples of this:
  - `feat/add-new-loss` is a good branch name: this branch clearly says that
    you're making a feature (feat), and the feature is to add a new loss. The
    shorthand is from the
    [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
    project.
  - `fix-model-parsing-tests` is also a good branch name, as it is clear what
    you're doing.
  - `makechange-nathan` is _not_ a good name. Noone knows what change this is
    for!
- Fork the repo, clone it locally, and make your new branch there instead. This
  is more likely to be the case if you're a first-timer: you won't have
  permissions to write a branch to the source repository.

Quick aside: if your project uses pre-commit, now is the time to install it. But
hopefully this was all in the contributing instructions for that project!

4. Make your changes. Every commit should have a description of what the changes
   made in that commit actually do -- this is much more important in big
   projects, where small bugs are much more likely to slip through with all the
   changes that are made.

- You can consult
  [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for
  ways to do this.
- Also, there's the possibility of
  [squashing commits](https://stackoverflow.com/questions/5189560/how-do-i-squash-my-last-n-commits-together)
  before making a PR if the project prefers a cleaner history.

5. For every change you make, write tests that validate your change exhibits the
   correct behaviour. **This is a crucial step for big projects, and key to make
   your contribution useful and merged!** Code without tests is hard to read
   (the tests tell me how to use it), and if I know that those tests are
   running, I can trust that I don't have to check every line you've written
   myself on my own machine.
6. Check to see how the repository structures tests so you can make them in the
   right place. Likely, if you added a new file, you should correspondingly make
   a new file in the test suite. If you edited an existing file, the tests
   should live in the existing test file for that.
7. Run the whole test suite locally. It's possible your new code accidentally
   introduced a subtle change that breaks the overall project without you
   realising.
8. Double-check any linting checks pass. You can run `pre-commit -a` to do this
   on most projects, but once again, delegate to their documentation.
9. Make the PR via the GitHub UI. Describe there in great detail every change
   you've made: this serves to incentivise people to review your code, and also
   to serve as documentation for others (remember that I advised you to look
   through PRs earlier!)
10. Fix any review comments/suggestions. This is the part you'll learn the most,
    since you have experts going through what you've written!
11. Repeat steps 5-8 until all comments are addressed.
12. You should get merge permissions after reviews pass! If so, make sure to
    delete your branch after merging (it pops up after you click merge).
