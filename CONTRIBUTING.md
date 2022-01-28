So you want to contribute with thumbor vips engine? Awesome! Welcome aboard!

## Steps

There are a few things you'll need in order to properly start hacking on it.

1. [Fork it](http://help.github.com/fork-a-repo/)
2. Install dependencies and initialize environment
3. Hack, in no particular order:
   - Write enough code
   - Write tests for that code
   - Check that other tests pass
   - Repeat until you're satisfied
4. Submit a pull request

## Install Dependencies

We seriously advise you to use
[virtualenv](http://pypi.python.org/pypi/virtualenv) since it will keep
your environment clean of thumbor vips engine's dependencies and you can choose when
to "turn them on".

You also need to have docker available locally.

## Initializing the Environment

You can install thumbor-vips-engine dev dependencies with:

    $ make setup

## Running the Tests

Running the tests is as easy as:

    $ make test

You should see the results of running your tests after an instant.

## Linting your code

Please ensure that your editor is configured to use
[black](https://github.com/psf/black),
[flake8](https://flake8.pycqa.org/en/latest/) and
[pylint](https://www.pylint.org/).

Even if that's the case, don't forget to run `make flake pylint` before
commiting and fixing any issues you find. That way you won't get a
request for doing so in your PR.

In order to automate that, install pre-commit with:

```
$ pip install pre-commit
$ pre-commit install
```

After this, every commit will be linted before creation.

## Pull Requests

After hacking and testing your contribution, it is time to make a pull
request. Make sure that your code is already integrated with the `master`
branch of thumbor-vips-engine before asking for a pull request.

To add thumbor-vips-engine as a valid remote for your repository:

    $ git remote add thumbor-vips-engine git://github.com/thumbor/thumbor-vips-engine.git

To merge thumbor vips engine's master with your fork:

    $ git pull --rebase thumbor-vips-engine master

If there was anything to rebase, just run your tests again. If they pass,
[send a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
